"""
Freeman's pairing-friendly curves of prime order and embedding degree 10
ANTS VII, 2006, LNCS 4076
https://link.springer.com/chapter/10.1007/11792086_32
https://eprint.iacr.org/2006/026

The curve parameters are obtained as
ZZx.<x> = ZZ[]
Phi10 = cyclotomic_polynomial(10)
k = 10
(Phi10(-5*x^2)).factor()
(25*x^4 - 25*x^3 + 15*x^2 - 5*x + 1) * (25*x^4 + 25*x^3 + 15*x^2 + 5*x + 1)

rx = 25*x^4 + 25*x^3 + 15*x^2 + 5*x + 1
zx = -5*x^2
for i in [i for i in range(k) if gcd(i,k) == 1]:
    tx = (zx^i % rx) + 1
    px = rx - 1 + tx
    print("i = {} tx = {} px = {}".format(i, tx, px))
    (tx^2 - 4*px).factor()


rx = 25*x^4 + 25*x^3 + 15*x^2 + 5*x + 1
tx = 10*x^2 + 5*x + 3
px = 25*x^4 + 25*x^3 + 25*x^2 + 10*x + 3
yx = 1
D = 15*x^2 + 10*x + 3
tx == ((-5*x^2)^3 % rx) + 1
px == rx - 1 + tx
tx^2 - 4*px == -D*yx^2
"""

import sage

from sys import version_info
if version_info[0] < 3:
    from exceptions import ValueError
from sage.functions.log import log
from sage.functions.other import ceil
from sage.arith.misc import XGCD, xgcd
from sage.rings.integer import Integer
from sage.rings.rational_field import Q, QQ
from sage.misc.functional import cyclotomic_polynomial
from sage.rings.finite_rings.finite_field_constructor import FiniteField
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing
from sage.schemes.elliptic_curves.ell_finite_field import EllipticCurve_finite_field
from sage.schemes.elliptic_curves.constructor import EllipticCurve

import tnfs.curve.pairing_friendly_curve
from tnfs.curve.pairing_friendly_curve import get_curve_generator_order_r

allowed_k = [10]

def polynomial_params(k=10):
    QQx = QQ['x']; (x,) = QQx._first_ngens(1)
    px = 25*x**4 + 25*x**3 + 25*x**2 + 10*x + 3
    rx = 25*x**4 + 25*x**3 + 15*x**2 + 5*x + 1
    tx = 10*x**2 + 5*x + 3
    cx = QQx(1)
    yx = QQx(1)
    Dx = 15*x**2 + 10*x + 3
    betax=None
    lambx=None
    return px, rx, tx, cx, yx, betax, lambx, Dx

def poly_cofactor_gt(k=10):
    """Computes the co-factors for GT: Phi_k(p(x))/r(x)
    It is always irreducible:
    from tnfs.curve.freeman import poly_cofactor_gt
    k = 10
    print("Feeman")
    c = poly_cofactor_gt(k)
    print(["(deg {})^{} ".format(ci.degree(), ei) if ei>1 else "(deg {})".format(ci.degree()) for (ci, ei) in c.factor()])
    print(lcm([ci.denom() for ci in c.list()]))
    """
    QQx = QQ['x']; (x,) = QQx._first_ngens(1)
    px, rx, tx, cx, yx, betax, lambx, D = polynomial_params(k)
    cx = cyclotomic_polynomial(k)(px)
    assert (cx % rx) == 0
    cx = cx // rx
    assert cx == 15625*x**12 + 46875*x**11 + 100000*x**10 + 143750*x**9 + 165000*x**8 + 147500*x**7 + 108250*x**6 + 63375*x**5 + 30100*x**4 + 11000*x**3 + 3060*x**2 + 555*x + 61
    return cx

def coeff_params():
    Px = [3, 10, 25, 25, 25]
    Px_denom = 1
    Rx = [1, 5, 15, 25, 25]
    Rx_denom = 1
    Cx = [1] # cofactor such that p+1-tr == c*r
    Cx_denom = 1
    Tx = [3, 5, 10]
    Tx_denom = 1
    Yx = [1] # such that Tx^2 - 4*Px = -3*Yx^2
    Yx_denom = 1
    BETAx = None
    BETAx_denom = None
    LAMBx = None
    LAMBx_denom = None
    Dx = [3, 10, 15]
    Dx_denom = 1
    return Px, Px_denom, Rx, Rx_denom, Tx, Tx_denom, Cx, Cx_denom, Yx, Yx_denom, BETAx, BETAx_denom, LAMBx, LAMBx_denom, Dx, Dx_denom

def poly_cofactor_twist_g1_g2(k=10):
    QQx = QQ['x']; (x,) = QQx._first_ngens(1)
    px, rx, tx, cx, yx, betax, lambx, Dx = polynomial_params()
    twx = px+1+tx # irreducible
    assert twx == 25*x**4 + 25*x**3 + 35*x**2 + 15*x + 7
    m = 1
    u_m = [0]
    # cx = 1 for Freeman curves
    #print("twx={}\n={}".format(twx,twx.factor()))
    # for G2, compute #E(Fp5) then compute its quadratic twist
    #QQqt.<q,t> = QQ[]
    #t1 = t
    #t2 = t^2 - 2*q
    #t3 = t*t2 - q*t1
    #t4 = t*t3 - q*t2
    #t5 = t*t4 - q*t3
    #t5 == t^5 - 5*q*t^3 + 5*q^2*t
    #y5 = t5^2 - 4*q^5
    #y5 == (t^2 - 4*q) * (t^4 - 3*q*t^2 + q^2)
    tx5 = tx**5 - 5*px*tx**3 + 5*px**2*tx
    yx5 = yx * (tx**4 - 3*px*tx**2 + px**2)
    assert yx5 == 3125*x**8 + 6250*x**7 + 7500*x**6 + 5625*x**5 + 3100*x**4 + 1175*x**3 + 340*x**2 + 60*x + 9
    px5 = px**5
    assert tx5**2 - 4*px5 == -Dx*yx5**2
    # now the quadratic twist that matches rx
    E2_order = px5+1+tx5
    assert (E2_order % rx) == 0
    g2cx = E2_order // rx # twx * irreducible
    assert (g2cx % twx) == 0
    g2cxa = g2cx // twx
    assert g2cxa.is_irreducible()
    assert g2cxa == 15625*x**12 + 46875*x**11 + 93750*x**10 + 128125*x**9 + 138125*x**8 + 116875*x**7 + 80875*x**6 + 44875*x**5 + 20225*x**4 + 7075*x**3 + 1880*x**2 + 325*x + 31
    g2twx = None # the quadratic twist of the twist is E itself
    cofactor_r = [1]
    polys_cofact_twists = [twx, g2cxa]
    label_factors = ["twx", "g2cxa"]
    small_cofactors = [1, 1]
    return m, u_m, cofactor_r, twx, g2cx, g2twx, polys_cofact_twists, label_factors, small_cofactors

class Freeman(EllipticCurve_finite_field):
    """
    A Freeman k=10 curve
    """
    def __init__(self, u, a, b, D, y=None, k=10, cofactor_r=1):
        """
        INPUT:
        - `u`: seed such that p=P(u), r=R(u) are primes
        - `a`,`b`: curve coefficients, s.t. y^2 = x^3 + a*x + b has exactly order r=R(u)
        - `D`: curve discriminant, square-free part in t^2 - 4*p = -D*y^2, D*y^2 = 15*u^2 + 10*u + 3
        - `y`: square part in t^2 - 4*p = -D*y^2
        - `k`: embedding degree 10
        - `cofactor_r`: in case the curve has not prime order, R(u) = r0*cofactor_r
        """
        self._u = Integer(u) # seed
        self._k = 10 # embedding degree
        self._a = Integer(a)
        self._b = Integer(b)
        self._D = Integer(D)
        self._px, self._px_denom, self._rx, self._rx_denom, self._tx, self._tx_denom, self._cx, self._cx_denom, self._yx, self._yx_denom, self._betax, self._betax_denom, self._lambx, self._lambx_denom, self._dx, self._dx_denom = coeff_params()

        #self._p = sum([Integer(self._px[i])*self._u**i for i in range(len(self._px))])
        self._p = 25*self._u**4 + 25*self._u**3 + 25*self._u**2 + 10*self._u + 3
        self._pbits = self._p.nbits()
        self._tr = 10*self._u**2 + 5*self._u + 3
        self._r = 25*self._u**4 + 25*self._u**3 + 15*self._u**2 + 5*self._u + 1
        self._c = Integer(1)
        if cofactor_r != 1 and (self._r % cofactor_r) == 0:
            self._c = Integer(cofactor_r)
            self._r = self._r // self._c
        self._Dy2 = 15*self._u**2 + 10*self._u + 3
        if y is not None:
            self._y = Integer(y)
            assert self._D*self._y**2 == self._Dy2
        else:
            assert (self._Dy2 % self._D) == 0
            assert (Integer(self._Dy2 // self._D)).is_square()
            self._y = Integer((Integer(self._Dy2 // self._D)).sqrt())

        # GLV parameter for fast scalar multiplication thanks to automorphism
        # there is no automorphism
        self._beta = None
        self._lamb = None
        try:
            self._Fp = FiniteField(self._p)
        except ValueError as err:
            print("ValueError creating Fp: {}".format(err))
            print("p= {}".format(self._p))
            raise
        except:
            print("Error creating Fp")
            raise
        if not self._r.is_prime():
            raise ValueError("Error r is not prime, r= {} cofactor_r = {}".format(r, cofactor_r))

        self._Fpz = PolynomialRing(self._Fp, names=('z',))
        (self._z,) = self._Fpz._first_ngens(1)

        if a is not None:
            try:
                a = Integer(a)
            except:
                raise
            self._a = a
            self._ap = self._Fp(a)
        if b is not None:
            try:
                b = Integer(b)
            except:
                raise
            self._b = b
            self._bp = self._Fp(b)
        try:
            # this init function of super inherits from class EllipticCurve_generic defined in ell_generic.py
            # __init__ method inherited from ell_generic
            EllipticCurve_finite_field.__init__(self, self._Fp, [0,0,0,self._ap,self._bp])
        except ValueError as err:
            print("ValueError at EllipticCurve_finite_field.__init__: {}".format(err))
            raise
        except:
            print("An error occupred when initialising the elliptic curve")
            raise
        #print("check order")
        #self.order_checked = super(Freeman,self).order() too slow
        #if self.order_checked != self._r:
        #    print("Error, wrong order")
        #    raise ValueError("Wrong curve order: this one is a twist")
        self.curve_order = self._p + Integer(1) - self._tr
        self.twist_order = self._p + Integer(1) + self._tr
        for i in range(10):
            P = self.random_element()
            if self.curve_order*P != self(0):
                if self.twist_order*P == self(0):
                    raise ValueError("Wrong curve order: this one is a twist: (p+1+tr)*P = 0\ntr={}\nr={}\np+1+tr={}\n".format(self._tr,self.curve_order,self.twist_order))
                else:
                    self.order_checked = super(Freeman,self).order()
                    raise ValueError("Wrong curve order:\np+1-tr        = {}\np+1+tr        = {}\nchecked order = {}\np             = {}\nchecked trace = {}\nexpected trace= {}".format(self.curve_order,self.twist_order,self.order_checked,self._p, self._p+Integer(1)-self.order_checked, self._tr))
        #print("ok")

        # computes a generator
        self._G = get_curve_generator_order_r(self)
        self._Gx = self._G[0]
        self._Gy = self._G[1]
        # note that there is no cofactor for Freeman curves because r=p+1-tr

    def _repr_(self):
        return "Freeman k=10 p"+str(self._pbits)+" curve with seed "+str(self._u)+"\n"+super(Freeman,self)._repr_()

    def u(self):
        return self._u
    def p(self):
        return self._p
    def r(self):
        return self._r
    def c(self):
        return self._c # cofactor is Integer(1) because r=p+1-tr and r is prime
    def tr(self):
        return self._tr
    def y(self):
        return self._y
    def D(self):
        return self._D
    def a(self):
        return self._a # Integer
    def ap(self):
        return self._ap # in Fp (finite field element)
    def b(self):
        return self._b # Integer
    def bp(self):
        return self._bp # in Fp (finite field element)
    def beta(self):
        return self._beta # None
    def lamb(self):
        return self._lamb # None

    def px(self):
        return self._px
    def rx(self):
        return self._rx
    def tx(self):
        return self._tx
    def cx(self):
        return self._cx
    def yx(self):
        return self._yx
    def Dx(self):
        return self._Dx

    def k(self):
        return self._k
    def Fp(self):
        return self._Fp
    def Fpz(self):
        return self._Fpz, self._z
    def G(self):
        return self._G

    def print_parameters(self):
        tnfs.curve.pairing_friendly_curve.print_parameters(self)

    def print_parameters_for_RELIC(self):
        tnfs.curve.pairing_friendly_curve.print_parameters_for_RELIC(self)
