import sage

from sys import version_info
if version_info[0] < 3:
    from exceptions import ValueError
from sage.functions.log import log
from sage.functions.other import ceil
from sage.arith.misc import XGCD, xgcd
from sage.arith.functions import lcm
from sage.misc.functional import cyclotomic_polynomial
from sage.rings.integer import Integer
from sage.rings.rational_field import Q, QQ
from sage.rings.finite_rings.finite_field_constructor import FiniteField
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing
from sage.schemes.elliptic_curves.ell_finite_field import EllipticCurve_finite_field
from sage.schemes.elliptic_curves.constructor import EllipticCurve

import tnfs.curve.pairing_friendly_curve
from tnfs.curve.pairing_friendly_curve import BrezingWeng
from tnfs.curve.pairing_friendly_curve import get_curve_parameter_a_j1728, get_curve_generator_order_r_j1728

def polynomial_params(k):
    """Returns the parameters of Construction 6.3 in [FST]
    this is 6.2 modified to work with even k, k=2 mod 4

    INPUT:
    - `k`: even embedding degree, k=2 mod 4

    RETURN: univariate polynomials px, rx, cx, tx, yx, betax, lambx, and discriminant D=1
    field characteristic, subgroup order, cofactor, elliptic curve trace, square part y(x), eigenvalues mod px, rx, D
    r(x) = Phi_{2k}(x) the 2*k-th cyclotomic polynomial
    t(x) = x^2+1
    p(x) = (t^2(x) + y^2(x))/4
    y(x) = (x^2-1)*x^(k//2)
    D = 1

    test:
    from tnfs.curve.fst63 import polynomial_params
    for k in [ki for ki in range(6, 55, 4) if (ki % 4) == 2]:
        px, rx, tx, cx, yx, betax, lambx, D = polynomial_params(k)
        x = px.variables()[0]
        print("k={} lcm(denom(px)) = {}".format(k, lcm([ci.denom() for ci in px.list()]) ))
        print("k={} lcm(denom(px(2*x))) = {}".format(k, lcm([ci.denom() for ci in (px(2*x)).list()]) ))
        print("k={} lcm(denom(px(2*x+1))) = {}".format(k, lcm([ci.denom() for ci in (px(2*x+1)).list()]) ))

    """
    if (k % 4) != 2:
        raise ValueError("Error k should be 2 mod 4 but k={}={} mod 4".format(k, k%4))
    m = 2
    u_mod_m = [1]
    if k==22:
        m = 22
        u_mod_m = [1, 21]
    QQx = QQ['x']; (x,) = QQx._first_ngens(1)
    rx = QQx(cyclotomic_polynomial(2*k))
    # zeta_k = x^2, and zeta_k^k = x^(2*k) = 1
    tx = QQx(x**2+1)
    yx = QQx(x**(k//2+2) - x**(k//2))
    # yx = (tx-2)/sqrt(-1) = (x^2-1)/sqrt(-1) and x^(k//2) = sqrt(-1) then yx = (x^2-1)*x^(k//2)
    # px = (tx^2 + yx^2)/4 = (x^2+1)^2 + (x^2-1)^2*x^k = x^4 + 2*x^2 + 1 + (x^4 - 2*x^2 + 1)*x^k
    px = QQx(x**(k+4) - 2*x**(k+2) + x**k + x**4 +2*x**2 + 1)/4
    D = 1
    assert (tx**2 + D*yx**2)/4 == px
    assert ((px+1-tx) % rx) == 0
    cx = (px+1-tx) // rx
    assert (cyclotomic_polynomial(k)(px) % rx) == 0
    assert px.is_irreducible()
    assert rx.is_irreducible()

    g,u,v = px.xgcd(yx)
    if g == 1:
        inv_yx = QQx(v)
    else:
        inv_yx = QQx(v)/QQ(g)
    # px = (tx^2 + D*yx^2) / 4
    # tx^2 = -D*yx^2
    # -D = (tx/yx)^2
    betax = QQx((inv_yx*tx) % px)
    lambx = QQx(x**(k//2))
    assert ((betax**2 + D) % px) == 0
    assert ((lambx**2 + 1) % rx) == 0
    return px, rx, tx, cx, yx, betax, lambx, D

def get_m_u_mod_m(k=None):
    """Return the congruence conditions m, u_mod_m on the seed x = u mod m
    so that the parameters are all integers and p(x), r(x) generate primes

    INPUT: None
    RETURN: modulus m (int), list of residues u mod m, and m=1, u_mod_m=[0] if no condition is required
    """
    m = 2
    u_mod_m = [1]
    if k is not None and k == 22:
        m = 22
        u_mod_m = [1, 21]
    return m, u_mod_m

def coeffs_params(k):
    """ Return the coefficients in ZZ of the polynomials together with the denominators """

    px, rx, tx, cx, yx, betax, lambx, D = polynomial_params(k)
    Px_denom = lcm([fi.denom() for fi in px.list()])
    Px = [Integer(fi) for fi in (Px_denom * px).list()]
    Rx_denom = lcm([fi.denom() for fi in rx.list()])
    Rx = [Integer(fi) for fi in (Rx_denom * rx).list()]
    Tx_denom = lcm([fi.denom() for fi in tx.list()])
    Tx = [Integer(fi) for fi in (Tx_denom * tx).list()]    
    Cx_denom = lcm([fi.denom() for fi in cx.list()])
    Cx = [Integer(fi) for fi in (Cx_denom * cx).list()]
    Yx_denom = lcm([fi.denom() for fi in yx.list()])
    Yx = [Integer(fi) for fi in (Yx_denom * yx).list()]

    Betax_denom = lcm([fi.denom() for fi in betax.list()])
    Betax = [Integer(fi) for fi in (Betax_denom * betax).list()]

    Lambx_denom = lcm([fi.denom() for fi in lambx.list()])
    Lambx = [Integer(fi) for fi in (Lambx_denom * lambx).list()]

    return Px, Px_denom, Rx, Rx_denom, Tx, Tx_denom, Cx, Cx_denom, Yx, Yx_denom, Betax, Betax_denom, Lambx, Lambx_denom, D

def poly_cofactor_gt(k):
    """Computes the co-factors for GT: Phi_k(p(x))/r(x)

    It is always irreducible:
    from tnfs.curve.fst63 import poly_cofactor_gt
    for k in [ki for ki in range(6, 55, 4) if (ki % 4) == 2]:
        print("\nFST63-k{}".format(k))
        c = poly_cofactor_gt(k)
        print(["(deg {})^{} ".format(ci.degree(), ei) if ei>1 else "(deg {})".format(ci.degree()) for (ci, ei) in c.factor()])
        x = c.variables()[0]
        print(lcm([ci.denom() for ci in (c(2*x+1)).list()]))
    """
    QQx = QQ['x']; (x,) = QQx._first_ngens(1)
    px, rx, tx, cx, yx, betax, lambx, D = polynomial_params(k)
    cx = cyclotomic_polynomial(k)(px)
    assert (cx % rx) == 0
    cx = cx // rx
    return cx

class FST63(BrezingWeng):
    """A FST63 pairing-friendly curve of embedding degree k = 2 mod 4
    """
    # re-use the init function of class BrezingWeng
    def __init__(self, k, u, a=None, cofactor_r=1, verbose_init=False):
        px, px_denom, rx, rx_denom, tx, tx_denom, cx, cx_denom, yx, yx_denom, betax, betax_denom, lambx, lambx_denom, D = coeffs_params(k)
        super().__init__(k, D, u, px, px_denom, rx, rx_denom, tx, tx_denom, cx, cx_denom, yx, yx_denom, betax, betax_denom, lambx, lambx_denom, a, 0, cofactor_r, verbose_init)
        # b=0
    def _repr_(self):
        return "FST63_k"+str(self._k)+"_D"+str(self._D)+" p"+str(self._pbits)+" (pairing-friendly curve k="+str(self._k)+") with seed "+str(self._u)+"\n"+super(BrezingWeng, self)._repr_()
