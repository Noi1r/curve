import sage

from sys import version_info
if version_info[0] < 3:
    from exceptions import ValueError
from sage.functions.log import log
from sage.functions.other import ceil, sqrt
from sage.arith.misc import XGCD, xgcd, gcd
from sage.arith.functions import lcm
from sage.misc.functional import cyclotomic_polynomial
from sage.rings.integer import Integer
from sage.rings.integer_ring import Z, ZZ
from sage.rings.rational_field import Q, QQ
from sage.rings.number_field.number_field import CyclotomicField
from sage.rings.number_field.number_field import NumberField
from sage.rings.finite_rings.finite_field_constructor import FiniteField, GF
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing
from sage.schemes.elliptic_curves.ell_finite_field import EllipticCurve_finite_field
from sage.schemes.elliptic_curves.constructor import EllipticCurve

import tnfs
import tnfs.curve.pairing_friendly_curve
from tnfs.curve.pairing_friendly_curve import get_curve_parameter_b_j0, get_curve_generator_order_r_j0
from tnfs.curve.pairing_friendly_curve import get_curve_parameter_a_j1728, get_curve_generator_order_r_j1728
from tnfs.curve.pairing_friendly_curve import compute_beta_lambda
from tnfs.curve.pairing_friendly_curve import BrezingWeng

#possible embedding degrees
allowed_k = [20, 22]

def polynomial_params(k: int, D: int, l: int, exp_tr: int):
    """
    Returns the polynomial parameters px, rx, cx, tx, yx, betapx, lambrx, and D
    for the Brezing-Weng construction of pairing-friendly curves.
    eprint 2003/143 DCC vol 37 (1) pp. 133--141, 2005 10.1007/s10623-004-3808-4
    Choose r(x) = Phi_k(x) or Phi_{k*l}(x) so that -D is a square mod r(x),
    define t(x) = x^{e*l}+1 where e is co-prime to k,
    get y(x) = (t(x)-2)/sqrt(-D), then
    p(x) = (t^2(x) + D*y^2(x))/4

    this function lists precomputed values for k, l, exp_tr, such that p(x) and r(x) generate primes.

    INPUT
    k: embedding degree
    D: discriminant (abs)
    l: small integer (1, 2, 3) so that -D is a square modulo Phi_{k*l}(x)
       multiplier of the degree of the cyclotomic polynomial
       e.g. for D=3, l = 3/gcd(3,k)
            for D=1, l = 4/gcd(4,l)
    exp_tr: choice of exponent of the trace t(x) = (x^l)^exp_tr + 1 mod r(x)
    """
    QQx = QQ['x']; (x,) = QQx._first_ngens(1)
    Phi_k = QQx(cyclotomic_polynomial(k))
    automorphisms = [] # automorphisms other than identity
    m = 1
    u_m = [0]
    cofactor_r = [1]
    if k==20 and D==1 and l==1 and exp_tr==1: # actually this is FST 64 k=20
        k = 20
        D = 1
        l = 1
        exp_tr = 1
        rho = 3/2        
        tx = x + 1
        rx = x**8 - x**6 + x**4 - x**2 + 1
        px = (x**12 - 2*x**11 + x**10 + x**2 + 2*x + 1)/4
        yx = x**6 - x**5
        cx = (x - 1)**2 * (x**2 + 1)/4
        betapx = (x**11 - 3*x**10 + 4*x**9 - 4*x**8 + 4*x**7 - 4*x**6 + 2*x**5 + x + 1)/2
        lambrx = x**5
        m = 2
        u_mod_m = [1]
    if k==22 and D==1 and l==2 and exp_tr==1: # this is FST 6.3
        k = 22
        D = 1
        l = 2
        exp_tr = 1
        rho = 13/10 # 1.3
        tx = x**2 + 1
        rx = x**20 - x**18 + x**16 - x**14 + x**12 - x**10 + x**8 - x**6 + x**4 - x**2 + 1
        px = (x**26 - 2*x**24 + x**22 + x**4 + 2*x**2 + 1)/4
        yx = x**13 - x**11
        cx = (x**4 - 1) * (x**2 - 1)/4
        lambrx = x**11
        betapx = (x**25 - 3*x**23 + 4*x**21 - 4*x**19 + 4*x**17 - 4*x**15 + 4*x**13 - 2*x**11 + x**3 + x)/2 # (t-2)/y mod px
        m = 2
        u_mod_m = [1]
    elif k==22 and D==3 and l==3 and exp_tr==1: # this is FST 6.6
        k = 22
        D = 3
        l = 3
        exp_tr = 1
        rho = 7/5 # 1.4
        tx = x**3 + 1
        rx = x**20 + x**19 - x**17 - x**16 + x**14 + x**13 - x**11 - x**10 - x**9 + x**7 + x**6 - x**4 - x**3 + x + 1
        px = (x**28 - 2*x**25 + x**22 - x**17 + 2*x**14 - x**11 + x**6 + x**3 + 1)/3
        yx = (2*x**14 - 2*x**11 - x**3 + 1)/3
        cx = (x**3 - 1)**2 * (x**2 - x + 1)/3
        lambrx = -x**11
        betapx = (2*x**27 + 4*x**26 - x**25 - 6*x**24 - 12*x**23 + 3*x**22 + 8*x**21 + 16*x**20 - 4*x**19 - 8*x**18 - 16*x**17 + 2*x**16 + 4*x**15 + 17*x**14 + 2*x**13 + 4*x**12 - 10*x**11 - 4*x**10 - 8*x**9 + 2*x**8 + 4*x**7 + 8*x**6 - 9*x**3 + 2*x**2 + 4*x - 1)/9
        m = 3
        u_mod_m = [1]
    else:
        raise ValueError("no configured set of parameters for Cyclotomic k={} D={} l={} exp_t={}".format(k, D, l, exp_tr))

    assert (Phi_k(tx-1) % rx) == 0, "Error k={},D={},l={},exp_tr={}, Phi_k(tx-1)%rx != 0, = {}, tx=x^({}*{})+1 mod rx = {}, rx={}".format(k, D, l, exp_tr, Phi_k(tx-1) % rx, l, exp_tr, tx, rx)
    px_denom = lcm([pi.denom() for pi in px.list()])
    assert ((px+1-tx) % rx) == 0, "Error (px+1-tx)%rx != 0, px={}*({}), tx={}, rx={}, (px+1-tx)={}".format(px_denom, px_denom*px, tx,rx, (px+1-tx).factor())
    assert cx == (px+1-tx) // rx
    assert (Phi_k(px) % rx) == 0, "Error k={}, Phi_k(px)%rx != 0, = {}".format(k, Phi_k(px) % rx)
    assert px.is_irreducible(), "Error px is not irreducible, px= {}".format(px.factor())
    assert rx.is_irreducible(), "Error rx is not irreducible, rx= {}".format(rx.factor())
    assert 4*px == (tx**2 + D*yx**2), "Error 4*px != tx^2+D*yx^2, {}*px = {}, tx={}, D={}, yx={}, tx^2+Dyx^2 = {}".format(px_denom, px_denom*px, tx, D, yx, tx**2+D*yx**2)

    return px, rx, tx, cx, yx, betapx, lambrx, D, l, exp_tr, m, u_m

def coeffs_params(k: int, D: int, l: int, exp_tr: int):
    px, rx, tx, cx, yx, betapx, lambrx, D, l, exp_tr, m, u_m = polynomial_params(k, D, l, exp_tr)
    Px_denom = Integer(lcm([ci.denom() for ci in px.list()]))
    Px = [Integer(ci) for ci in (Px_denom*px).list()]
    Rx_denom = Integer(lcm([ci.denom() for ci in rx.list()]))
    Rx = [Integer(ci) for ci in (Rx_denom*rx).list()]
    Tx_denom = Integer(lcm([ci.denom() for ci in tx.list()]))
    Tx = [Integer(ci) for ci in (Tx_denom*tx).list()]
    Cx_denom = Integer(lcm([ci.denom() for ci in cx.list()]))
    Cx = [Integer(ci) for ci in (Cx_denom*cx).list()]
    Yx_denom = Integer(lcm([ci.denom() for ci in yx.list()]))
    Yx = [Integer(ci) for ci in (Yx_denom*yx).list()]
    if betapx != 0 and lambrx != 0:
        BETAPx_denom = Integer(lcm([ci.denom() for ci in betapx.list()]))
        BETAPx = [Integer(ci) for ci in (BETAPx_denom*betapx).list()]
        LAMBRx_denom = Integer(lcm([ci.denom() for ci in lambrx.list()]))
        LAMBRx = [Integer(ci) for ci in (LAMBRx_denom*lambrx).list()]
    else:
        BETAPx_denom=0; BETAPx=0; LAMBRx_denom=0; LAMBRx=0
    return Px, Px_denom, Rx, Rx_denom, Tx, Tx_denom, Cx, Cx_denom, Yx, Yx_denom, BETAPx, BETAPx_denom, LAMBRx, LAMBRx_denom, D, l, exp_tr

def poly_cofactor_gt(k: int, D: int, l: int, exp_tr: int):
    """
    Computes the co-factors for GT: Phi_k(p(x))/r(x)
    Same inputs as for polynomial_params
    """
    QQx = QQ['x']; (x,) = QQx._first_ngens(1)
    px, rx, tx, cx, yx, betapx, lambrx, D, l, exp_tr, m, u_m = polynomial_params(k, D, l, exp_tr)
    ex = cyclotomic_polynomial(k)(px)
    assert (ex % rx) == 0
    ex = ex // rx
    return ex

class Cyclotomic(BrezingWeng):
    """A cyclotomic pairing-friendly curve of embedding degree k
    """
    # re-use the init function of class BrezingWeng
    def __init__(self, k, u, D, l, e0, a=None, b=None, cofactor_r=1, verbose_init=False):
        px, px_denom, rx, rx_denom, tx, tx_denom, cx, cx_denom, yx, yx_denom, betapx, betapx_denom, lambrx, lambrx_denom, D, l, exp_tr = coeffs_params(k, D, l, e0)
        super().__init__(k, D, u, px, px_denom, rx, rx_denom, tx, tx_denom, cx, cx_denom, yx, yx_denom, betapx, betapx_denom, lambrx, lambrx_denom, a, b, cofactor_r, verbose_init)
        self._l = l
        self._exp_tr = exp_tr

    def _repr_(self):
        return "Cyclotomic_k"+str(self._k)+"_D"+str(self._D)+"_l"+str(self._l)+"_e0"+str(self._exp_tr)+" p"+str(self._pbits)+" (pairing-friendly curve k="+str(self._k)+") with seed "+str(self._u)+"\n"+super(BrezingWeng, self)._repr_()
