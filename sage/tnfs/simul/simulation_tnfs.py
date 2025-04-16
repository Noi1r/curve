"""
Simulation of the Special Tower Number Field Sieve
In particular, the yield of the relation collection

Author of the code: Aurore Guillevic, Inria Nancy

Method: a simulation of the elements in the relation collection
Monte-Carlo simulation with at least 10^5 samples taken at random
Computation of the error

Comparison of smoothess_proba(average norm)
to average(smoothness_proba(norm))

Reference:
On the alpha value of polynomials in the tower number field sieve algorithm
Aurore Guillevic and Shashank Singh
https://eprint.iacr.org/2019/885

Former simulation: [Barbulescu Duquesne 2018], Journal of Crypto
https://eprint.iacr.org/2017/334
https://dx.doi.org/10.1007/s00145-018-9280-5
"""

import sage
from sage.libs.pari import pari

from sys import version_info
if version_info[0] < 3:
    from exceptions import ValueError
from sage.functions.log import log
from sage.functions.other import ceil, floor, sqrt
from sage.rings.integer import Integer
from sage.rings.integer_ring import Z, ZZ
from sage.rings.real_mpfr import RR
from sage.misc.prandom import randint
from sage.arith.misc import gcd

from sage.functions.transcendental import dickman_rho
from sage.symbolic.constants import euler_gamma
from sage.functions.exp_integral import li, log_integral

from sage.rings.number_field.number_field import NumberField
from sage.rings.finite_rings.finite_field_constructor import FiniteField
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing

from tnfs.simul.polyselect import Polyselect

default_weight_per_row=200
barbulescu_duquesne_weight_per_row=128 # Barbulescu Duquesne assumes that the weight per row is 2^7 = 128
barbulescu_duquesne_cst_linalg = float(0.25) # Barbulescu-Duquesne paper assumes that there is a constant factor c_linalg = 1/4
machine_wordsize = 64 # assume the linear algebra step is run on a 64-bit architecture platform
# min and max according to appendix A in https://eprint.iacr.org/2019/431
cst_filtering_min = 9
cst_filtering_max = 382
default_cst_filtering = 20
# in Barbulescu-Duquesne, the cost of sieving is modeled as corr_sieve = 1
log2 = float(log(2.0))

def log2_L_N_alpha_c(log2N, alpha, c):
    logN = float(log2N)*log2
    return float(float(c)*(log2N)**(float(alpha))*(log(logN,2))**(float(1.0-alpha)))

def volume_sieving_space(A,deg_h):
    """
    Number of elements a_00 + a_01*y + ... + a_0d*y^d + x*(a_10 + a_11*y + ... + a_1d*y^d) where d = deg_h-1 and -A <= a_ij <= A, and strictly positive leading term 0 < a_1d <= A.

    :param A: bound (included) on the coefficients: -A <= a_ij <= A
    :param deg_h: degree of polynomial h. Elements sieved have 2*deg_h coefficients bounded by A.
    :returns: (2*A+1)^(2*deg_h)/2 this is divided by 2 assuming that the leading coeff is > 0.

    Except for cyclotomic polynomials (or related), the torsion units are {1,-1} only.
    """
    return (2*A+1)**(2*deg_h)/2

def lg2_volume_sieving_space(A,deg_h):
    """
    Number of elements a_00 + a_01*y + ... + a_0d*y^d + x*(a_10 + a_11*y + ... + a_1d*y^d) where d = deg_h-1 and -A <= a_ij <= A, and strictly positive leading term 0 < a_1d <= A.

    :param A: bound (included) on the coefficients: -A <= a_ij <= A
    :param deg_h: degree of polynomial h. Elements sieved have 2*deg_h coefficients bounded by A.
    :returns: log_2 ((2*A+1)^(2*deg_h)/2) this is divided by 2 assuming that the leading coeff is > 0.

    Except for cyclotomic polynomials (or related), the torsion units are {1,-1} only.
    """
    return float(RR((2.0*deg_h)*log(2.0*A+1.0, 2.0) - 1.0))

def core_volume_sieving_space(A, h, inv_zeta_Kh=1.0, compute_zeta_with_pari=False):
    """
    :param A: bound (included) on the coefficients -A <= a_ij <= A
    :param h: irreducible polynomial over Q
    :param inv_zeta_Kh: 1/zeta_Kh(2), precomputed or computed within the function with PARI
    :returns: volume_sieving_space(A,deg_h)*inv_zeta_Kh/w, w, inv_zeta_Kh \
    where w is the number of roots of unity up to multiplication by -1.

    Thanks to Paul Zimmermann (Inria Nancy) on how to compute zeta_Kh with PARI
    See also http://doc.sagemath.org/html/en/reference/number_fields/sage/rings/number_field/unit_group.html
    """
    deg_h = h.degree()
    if inv_zeta_Kh == 1.0 and compute_zeta_with_pari:
        inv_zeta_Kh = RR(1.0/(pari('lfun(' + str(h) + ', 2)')))
    Kh = NumberField(h, 'ah')
    w = get_w(Kh)
    return volume_sieving_space(A,deg_h)*inv_zeta_Kh/w, w, inv_zeta_Kh

def lg2_core_volume_sieving_space(A, h, inv_zeta_Kh=1.0, w=None, compute_zeta_with_pari=False):
    """
    :param A: bound (included) on the coefficients -A <= a_i <= A
    :param h: irreducible polynomial over Q
    :param inv_zeta_Kh: 1/zeta_Kh(2), precomputed or computed within the function with PARI
    :returns: log_2(volume_sieving_space(A,deg_h)*inv_zeta_Kh/w), w, inv_zeta_Kh \
    where w is the number of roots of unity up to multiplication by -1.
    """
    deg_h = h.degree()
    if inv_zeta_Kh == 1.0 and compute_zeta_with_pari:
        inv_zeta_Kh = RR(1.0/(pari('lfun(' + str(h) + ', 2)')))
    if w is None or w < 1:
        Kh = NumberField(h, 'ah')
        w = get_w(Kh)
    return float(RR(lg2_volume_sieving_space(A,deg_h) + log(inv_zeta_Kh,2.0) - log(w,2.0))), inv_zeta_Kh, w

def find_A(deg_h, target_cost, start_A, count_sieving_cost=False, log2_B=None, barbulescu_duquesne=False, w=1, aut=1):
    """ 
    Binary search on the value of A such that given h and an expected sieving cost, the sieving volume will be minimal.

    :param deg_h: int, degree of polynomial h
    :param target_cost: target cost in bits, formula: 2^target_cost = volume_sieving_space(A, deg_h)*(cost of sieving ~= log log B)
    :param start_A: int, a starting value for A
    :param log2_B: float
    :param barbulescu_duquesne: bool, if set to True: target_cost = (2*A+1)^(2*deg h)/(2 * w * automorphisms) * c_sieve
        where w = roots of unity up to +/- 1, automorphisms = aut(h) * aut(f,g), c_sieve = 1 (i.e. count_sieving_cost=False)
    :param w: number of roots of unity up to +/- 1. Barbulescu-Duquesne assume that is can be done efficiently to avoid enumerating the duplicate relations due to w.
    : aut: automorphisms that speed-up the relation collection

    Elements of Kh are considered as polynomials modulo h.
    The cost of sieving is estimated to be log(log(B)) in basis e (not in basis 2)
    where log log B = log (log_2 B * log(2))

    Barbulescu-Duquesne assumptions: ePrint 2017/334 Updating keysize estimations for pairings https://eprint.iacr.org/2017/334
    """
    print("find_A, target cost {:.2f}, count_sieving_cost is {}, w={}, aut={}, log2_B={:.3f}".format(float(target_cost), count_sieving_cost, w, aut, float(log2_B)))
    if barbulescu_duquesne:
        print("Barbulescu-Duquesne assumptions, w={}, aut={}, cost_relation_collection = (2*A+1)^(2*deg h)/(2 * w * aut) * c_sieve where c_sieve = 1".format(w, aut))
    lg2_aut = float(log(aut, 2.0)) # 0.0 if aut = 1
    A = start_A
    lg2_v = lg2_volume_sieving_space(A, deg_h)
    if barbulescu_duquesne:
        lg2_w = float(log(w, 2.0)) # 0.0 if w = 1
    else:
        lg2_w = float(0.0)
    # if count_sieving_cost then assume that the cost of sieving is log log B [Guillevic Singh 21, Section 6.1]
    if not barbulescu_duquesne and count_sieving_cost and log2_B is not None and log2_B > 1.0:
        # log log B = log (log_2 B * log(2))
        corr_log2_B = float(log(log(log2_B*log2),2.0))
    else:
        corr_log2_B = float(0.0)
    s = lg2_v + corr_log2_B - lg2_aut - lg2_w
    A_min = A
    A_max = A
    while s < target_cost: # increase A
        A = max(A+1, floor(1.1*A_min)) # if A < 9 it will loop if there is no max
        lg2_v = lg2_volume_sieving_space(A, deg_h)
        s = lg2_v + corr_log2_B - lg2_aut - lg2_w
        if s < target_cost:
            A_min = A
        else:
            A_max = A
    while s > target_cost: # decrease A
        A = min(A-1, floor(0.9*A_max))
        lg2_v = lg2_volume_sieving_space(A, deg_h)
        s = lg2_v + corr_log2_B - lg2_aut - lg2_w
        if s > target_cost:
            A_max = A
        else:
            A_min = A
    while ((A_max - A_min) > 1):
        A_mid = (A_min + A_max)//2
        lg2_v = lg2_volume_sieving_space(A_mid, deg_h)
        s = lg2_v + corr_log2_B - lg2_aut - lg2_w
        if s < target_cost:
            A_min = A_mid
        else:
            A_max = A_mid
    lg2_v1 = lg2_volume_sieving_space(A_min, deg_h)
    s1 = lg2_v1 + corr_log2_B - lg2_aut - lg2_w
    lg2_v2 = lg2_volume_sieving_space(A_max, deg_h)
    s2 = lg2_v2 + corr_log2_B - lg2_aut - lg2_w
    return A_min, s1, A_max, s2

def print_A(s_min, s_max, deg_h, start_A, count_sieving_cost=False, log2_B=None, barbulescu_duquesne=False, w=1, aut=1):
    print("params_A = {")
    A1 = start_A
    for vol in range(s_max-1, s_min-2, -1):
        A0, s0, A1, s1 = find_A(deg_h, vol, A1, count_sieving_cost, log2_B, barbulescu_duquesne, w, aut)
        print("    ({},{}): {},".format(deg_h, vol+1, A1))
    print("}")

def get_w(Kh):
    """
    :param Kh: number field over Q defined by a polynomial h
    :returns: # roots of unity / 2 (divides by #{1,-1})
    """
    number_of_other_roots_unity = len(Kh.roots_of_unity())//2
    # the number of distinct roots of unity w.r.t. multiplication by (-1)
    if number_of_other_roots_unity > 0:
        w = number_of_other_roots_unity
    else:
        w = 1
    # TODO: call pari-gp to compute the number of fondamental units
    # count those which have a small size of coefficients, for example when the constant coefficient of h(y) is +/-1, the element 'y' has a unit, it is an algebraic integer and a unit.
    return w

def time_linalg(log2_B, ell_word_size, weight_per_row=default_weight_per_row, cst_filtering=default_cst_filtering, barbulescu_duquesne=False, aut=None):
    """ Computes an estimate of the cost of the linear algebra step.

    :param log2_B: the log in basis 2 of the factor bound (relations involve primes <= B). Assume the same bound on both sides.
    :param ell_word_size: the number of machine-words (64-bit words) to write ell. The linear algebra operations are performed modulo ell.
    :param weight_per_row: the number of non-zero entries per row, arbitrarily 200. It is from 125 to 200 in recent computations.
    :param cst_filtering: a constant s.t. after the filtering step, the number of rows of the matrix is divided by this constant. Experimentally, 7.43 <= cst_filtering <= 386 in recent computations (< 10 years)
    :param barbulescu_duquesne: if True, apply Conjecture 1 in [BD19] claiming a variable cst_filtering = (log B)^(1+o(1))
    :returns log2_time_linalg, log2_size_FB, log2_size_matrix, logB (all float)

    Thanks to Emmanuel Thome (Inria Nancy).
    The size of the factor basis is estimated to be 2*log_integral(B)
    The number of rows of the matrix is the above size divided by a constant factor 'cst_filtering'
    or a variable factor log(B) if barbulescu_duquesne is set to True
    [BD19] Barbulescu, Duquesne, Updating key size estimations for pairings, Journal of Cryptology
    https://doi.org/10.1007/s00145-018-9280-5
    Conjecture 1:
        In the filtering step of NFS, one reduces the matrix by a
        factor (log B)^(1+o(1)), where B is the smoothness bound.

    The cost is estimated to be
    word_size(ell) * weight_per_row * (matrix size (=number of rows) after filtering step)^2
    """
    logB = float(log2_B*log2)
    if not barbulescu_duquesne:
        #log2_size_FB = log2(2*log_integral(B)) = 1 + log2(log_integral(B))
        log2_size_FB = float(1.0+log(log_integral(2.0**log2_B),2.0))
        # assume that the number of rows in the matrix is divided by a constant factor 'cst_filtering'
        log2_size_matrix = float(log2_size_FB - log(cst_filtering, 2.0))
        # assume that the time is (word_size(ell) * weight_per_row * (number_of_rows_matrix)^2)
        log2_time_linalg = float(log(ell_word_size,2.0) + log(weight_per_row,2.0) + 2.0*log2_size_matrix)
    else:
        log2_size_FB = float(1.0 + log2_B - log(logB,2.0))
        # assume that the number of rows in the matrix is divided by a variable factor log(B) according to Conjecture 1
        log2_size_matrix = float(log2_size_FB - log(logB, 2.0) - log(aut, 2.0))
        # assume that the time is (weight_per_row * (number_of_rows_matrix)^2)
        log2_time_linalg = float(log(barbulescu_duquesne_weight_per_row,2.0) + log(barbulescu_duquesne_cst_linalg,2.0) + 2.0*log2_size_matrix)
    return log2_time_linalg, log2_size_FB, log2_size_matrix, logB

def find_log2_B(log2_target_cost, start_log2B, prec, fct_time_linalg, ell_word_size, weight_per_row=default_weight_per_row, cst_filtering=default_cst_filtering, barbulescu_duquesne=False, aut=None):
    """ 
    Binary search on the value of log2(B) such that given a function on input B and word_size(ell) that computes the cost (as 2^c) of the linear algebra step, 
    find B such that the estimated cost is 2^log2_target_cost
    :param log2_target_cost: tageted cost of linear algebra is 2^log2_target_cost
    :param start_log2B: a hint on the starting value of log2(B)
    :param prec: the precision, stops when (B_max-B_min) <= prec
    :param fct_time_linalg: a function whose inputs are log2_B and ell_word_size and 1st output is the estimated cost of linear algebra (in bits)
    :param ell_word_size: the number of machine-words (64-bit words) to write ell. The linear algebra operations are performed modulo ell.
    :param weight_per_row: the number of non-zero entries per row, arbitrarily 200. It is from 125 to 200 in recent computations.
    :param cst_filtering: a constant s.t. after the filtering step, the number of rows of the matrix is divided by this constant. Experimentally, 7.43 <= cst_filtering <= 386 in recent computations (< 10 years)
    :param barbulescu_duquesne: if True, apply Conjecture 1 in [BD19] claiming a variable cst_filtering = (log B)^(1+o(1)), and a linear algebra cost of barbulescu_duquesne_weight_per_row*barbulescu_duquesne_cst_linalg = 128/4 = 2^5
    """
    B = start_log2B
    tt, FB, M, logB = fct_time_linalg(B, ell_word_size, weight_per_row, cst_filtering, barbulescu_duquesne, aut)
    #tt = float(tt)
    B_min = B
    B_max = B
    while tt < log2_target_cost:
        B = floor(1.1*B_min)
        tt, FB, M, logB = fct_time_linalg(B, ell_word_size, weight_per_row, cst_filtering, barbulescu_duquesne, aut)
        #tt = float(tt)
        if tt < log2_target_cost:
            B_min = B
        else:
            B_max = B
    while tt > log2_target_cost:
        B = floor(0.9*B_max)
        tt, FB, M, logB = fct_time_linalg(B, ell_word_size, weight_per_row, cst_filtering, barbulescu_duquesne, aut)
        #tt = float(tt)
        if tt > log2_target_cost:
            B_max = B
        else:
            B_min = B
    while ((B_max - B_min) > prec):
        B_mid = float((B_min + B_max)/2)
        tt, FB, M, logB = fct_time_linalg(B_mid, ell_word_size, weight_per_row, cst_filtering, barbulescu_duquesne, aut)
        #tt = float(tt)
        if tt < log2_target_cost:
            B_min = B_mid
        else:
            B_max = B_mid
    t1, FB, M, logB = fct_time_linalg(B_min, ell_word_size, weight_per_row, cst_filtering, barbulescu_duquesne, aut)
    t2, FB, M, logB = fct_time_linalg(B_max, ell_word_size, weight_per_row, cst_filtering, barbulescu_duquesne, aut)
    #t1 = float(t1)
    #t2 = float(t2)
    return B_min, t1, B_max, t2
    
def print_B(s_min, s_max, start_log2B, fct_time_linalg, ell_word_size, weight_per_row=default_weight_per_row, cst_filtering=default_cst_filtering, barbulescu_duquesne=False, aut=None):
    """
    how to call this function:
    print_B(100, 150, 83.5, time_linalg, 4)
    print_B(100, 150, 83.5, time_linalg, 48)
    """
    print("params_log2B_ell_w = {")
    B1 = start_log2B
    for t in range(s_max-1, s_min-2, -1):
        B0, t0, B1, t1 = find_log2_B(t, B1, 0.001, fct_time_linalg, ell_word_size, weight_per_row, cst_filtering, barbulescu_duquesne, aut)
        print("    ({0},{1}): {2:.3f},".format(ell_word_size, (t+1), float(B1)))
    print("}")

def get_parameters_A_log2B(cost, ell_wordsize, aut, deg_h, weight_per_row=default_weight_per_row, cst_filtering=default_cst_filtering, barbulescu_duquesne=False, count_sieving_cost=False, w=1):
    """ total expected cost in bits """
    cost = float(cost)
    prec = 0.0001
    start_log2B = float(cost/2.0 - log(cost/2.0))
    # time_linalg is a function
    # whose optional parameters are
    # cst_filtering, weight_per_row
    # maybe put these functions inside the class...
    B_min, t1, B_max, t2 = find_log2_B(cost-1, start_log2B, prec, time_linalg, ell_wordsize, weight_per_row, cst_filtering, barbulescu_duquesne, aut)
    log2_B = B_max

    # starting rough estimate: |a_i|^(2*deg_h) ~= 2^(cost-1) => A ~= 2^((cost-1)/(2*deg_h))
    start_A = floor(float(2.0)**(float((cost-1)/(2*deg_h))))
    A_min, s1, A_max, s2 = find_A(deg_h, float(cost-1.0), start_A, count_sieving_cost, log2_B, barbulescu_duquesne, w, aut)
    # we should have s1 <= cost <= s2 and A_min + 1 = A_max
    if abs(cost-1-s1) < 0.5 and abs(cost-1.0-s2) >= 0.5:
        A = A_min
    else:
        A = A_max
    return A, log2_B

# about the simulation itself

def random_vec(A,size):
    """
    :param A: bound (included) on the coefficients
    :param size: length of the tuple
    :returns: a list of length size and made of random integers in [-A, A]
    Careful: the documentation about randint() tells that the bounds are both included. No "+1" here.
    """
    a = [randint(-A,A) for i in range(size)]
    return a

def random_vec_positive_lc(A,size):
    """Returns a list of length ``size`` made of random integers in [-A,A].
    The number at index size-1 is strictly positive."""
    return [randint(-A,A) for i in range(size-1)] + [randint(1,A)]

def smoothness_proba(logN, logB, alpha=0.0, log_spq=0.0):
    """
    computes an estimation of the smoothness probability of a (pseudo-)norm (this is an integer) N to be B-smooth.
    Uses Brian A. Murphy's formula, see his PhD thesis 
    Polynomial selection for the number field sieve integer factorisation algorithm,
    Australian National University, 1999
    http://maths-people.anu.edu.au/~brent/pd/Murphy-thesis.pdf 4.2.2 p.71 (85/144)
    See also Nathan McNew, The Most Frequent Values of the Largest Prime Divisor Function, 
    Experimental Mathematics, vol 26 (2), pp 210-224, 2017 
    https://doi.org/10.1080/10586458.2016.1155188, preprint https://arxiv.org/abs/1504.05985
    (Thanks to Sary Drappeau for pointing out the reference)

    :param logN: ln(N) where N is a large integer (a pseudo-norm)
    :param logB: ln(B) where B is a smoothness bound
    :param alpha: correcting term, default 0 (a negative alpha makes the norm more likely to be smooth)
    :param log_spq: ln(special-q), default 0. Divides N by q (computes ln(N)-ln(q))
    """
    u = float((logN+alpha-log_spq)/logB)
    proba = float(dickman_rho(u)+(1.0-float(euler_gamma))*dickman_rho(u-1.0)/float(logN))
    return proba

def lg2_smoothness_proba(logN, logB, alpha=0.0, log_spq=0.0):
    """ returns log_2(smoothness_proba(...)), see documentation of smoothness_proba()"""
    u = float((logN+alpha-log_spq)/logB)
    return float(log(dickman_rho(u)+(1-RR(euler_gamma))*dickman_rho(u-1)/(logN),2))    

def statistics(h,f,g,Rxy,A,logB,samples,alpha_f=0.0,alpha_g=0.0,check_coprime=True):
        """See
        https://fr.wikipedia.org/wiki/Intervalle_de_confiance
        https://en.wikipedia.org/wiki/68%E2%80%9395%E2%80%9399.7_rule
        """
        deg_h=h.degree()
        log_Nf =[0.0 for i in range(samples)]
        log_Ng =[0.0 for i in range(samples)]
        proba_f = [0.0 for i in range(samples)]
        proba_g = [0.0 for i in range(samples)]
        Kh = NumberField(h, 'ah')
        
        #seed(ceil(pi*10**100))
        #seed() # random seed from os.urandom if available, otherwise current time
        #but it is not the seed corresponding to randint(), but to rand().
        # also computes experimentally the proportion of duplicates in case lfun(h,2) is not available
        duplicates = 0
        for i in range(samples):
            b=random_vec_positive_lc(A,deg_h)
            a=random_vec(A,deg_h)
            # when there is an automorphism in Kh y->-y or y->1/y, then uses
            #a=random_vec_positive_lc(A,deg_h)
            if check_coprime:
                coprime_ideal = (gcd(gcd(a), gcd(b)) == 1) and (Kh.ideal(Kh(a))+Kh.ideal(Kh(b))==Kh.ideal(1))
                while not coprime_ideal:
                    a=random_vec(A,deg_h)
                    b=random_vec_positive_lc(A,deg_h)
                    duplicates += 1
                    coprime_ideal = (gcd(gcd(a), gcd(b)) == 1) and (Kh.ideal(Kh(a))+Kh.ideal(Kh(b))==Kh.ideal(1))
            #a=(1+2*y) + (3+4*y)*x
            #h.resultant(a.resultant(f0,x),y)
            log_Nf[i] = log(RR(abs(h.resultant(f.resultant(Rxy([a,b]))))))
            log_Ng[i] = log(RR(abs(h.resultant(g.resultant(Rxy([a,b]))))))
            proba_f[i] = smoothness_proba(log_Nf[i], logB, alpha_f)
            proba_g[i] = smoothness_proba(log_Ng[i], logB, alpha_g)
        # end for loop -> now there are norms for all samples
        # average
        avrg_log_Nf = RR(sum(log_Nf) / samples)
        avrg_log_Ng = RR(sum(log_Ng) / samples)
        avrg_proba_f = RR(sum(proba_f) / samples)
        avrg_proba_g = RR(sum(proba_g) / samples)
        prod_proba = [RR(proba_f[i]*proba_g[i]) for i in range(samples)]
        avrg_proba = RR(sum(prod_proba)/samples)
        # variance: sum square of diff between values and mean value    
        variance_norm_f = RR(sum([(log_Nf[i]-avrg_log_Nf)**2 for i in range(samples)]))
        variance_norm_g = RR(sum([(log_Ng[i]-avrg_log_Ng)**2 for i in range(samples)]))
        variance_proba_f = RR(sum([(proba_f[i]-avrg_proba_f)**2 for i in range(samples)]))
        variance_proba_g = RR(sum([(proba_g[i]-avrg_proba_g)**2 for i in range(samples)]))
        variance_proba = RR(sum([(prod_proba[i]-avrg_proba)**2 for i in range(samples)]))
        # standard deviation
        std_dev_norm_f = RR(sqrt(variance_norm_f/(samples-1)))
        std_dev_norm_g = RR(sqrt(variance_norm_g/(samples-1)))
        std_dev_proba_f = RR(sqrt(variance_proba_f/(samples-1)))
        std_dev_proba_g = RR(sqrt(variance_proba_g/(samples-1)))
        std_dev_proba = RR(sqrt(variance_proba/(samples-1)))
        
        # error
        err_norm_f = float(100*std_dev_norm_f/sqrt(samples)/avrg_log_Nf)
        err_norm_g = float(100*std_dev_norm_g/sqrt(samples)/avrg_log_Ng)
        err_proba_f = float(100*std_dev_proba_f/sqrt(samples)/avrg_proba_f)
        err_proba_g = float(100*std_dev_proba_g/sqrt(samples)/avrg_proba_g)
        err_proba = float(100*std_dev_proba/sqrt(samples)/avrg_proba)
        
        # cost
        avrg_log_Nf = float(avrg_log_Nf)
        avrg_log_Ng = float(avrg_log_Ng)
        avrg_proba_f = float(avrg_proba_f)
        avrg_proba_g = float(avrg_proba_g)
        avrg_proba = float(avrg_proba)
        
        std_dev_norm_f = float(std_dev_norm_f)
        std_dev_norm_g = float(std_dev_norm_g)
        std_dev_proba_f = float(std_dev_proba_f)
        std_dev_proba_g = float(std_dev_proba_g)
        std_dev_proba = float(std_dev_proba)
    
        return avrg_log_Nf, avrg_log_Ng, avrg_proba_f, avrg_proba_g, avrg_proba, err_norm_f, err_norm_g, err_proba_f, err_proba_g, err_proba, std_dev_norm_f, std_dev_norm_g, std_dev_proba_f, std_dev_proba_g, std_dev_proba, float(RR(RR(samples)/RR(samples+duplicates))), min(log_Nf), max(log_Nf), min(log_Ng), max(log_Ng)


class Simulation_TNFS():

    def __init__(self, p, ell, Fp, Fpz, h, f, g, Rxy, log2_cost, automorphism,
                 inv_zeta_Kh=1.0, w=None,
                 A=None, log2_B=None,
                 alpha_f=None, alpha_g=None,
                 weight_per_row=None, cst_filtering=None,
                 count_sieving=None, label=None,
                 barbulescu_duquesne=False):
        """
        :param              p: prime integer defining a prime field
        :param            ell: prime integer, order of the mult. subgroup where to compute DL
                               (linear algebra is done modulo ell)
        :param             Fp: finite field of characteristic p
        :param            Fpz: polynomial ring of Fp
        :param              h: univariate irreducible monic polynomial
        :param              f: uni- or bivariate irreducible polynomial
        :param              g: uni- or bivariate irreducible polynomial
        :param            Rxy: bivariate polynomial ring over Q (or Z)
        :param      log2_cost: the cost in basis 2 of (S)TNFS
        :param   automorphism: number of relations obtained for free thanks to automorphisms of Kh and
                               Kf, Kg (these are not extra rels, this is only a time speed-up)
        :param    inv_zeta_Kh: 1/zeta(Kh,2) where zeta is Dedekind zeta function of number field Kh
        :param              w: number of roots of unity in Kh up to multiplication by {+-1}
        :param              A: bound on the coefficients a_ij in the relation collection -A <= a_ij <= A
        :param         log2_B: B is the smoothness bound (relations involve primes <= B)
        :param        alpha_f: alpha value of f/Kh
        :param        alpha_g: alpha value of g/Kh
        :param weight_per_row: default 200 (weight per row of the matrix)
        :param  cst_filtering: default 20, reduction factor of the matrix
        :param  count_sieving: True/False, whether count the cost of sieving or not
        :param          label: for printing (such as name of the pairing-friendly curve)
        :param barbulescu_duquesne: if True, apply Conjecture 1 in [BD19] claiming a variable cst_filtering = (log B)^(1+o(1))
        """
        self.p = p     #
        self.ell = ell
        self.ell_wordsize = ceil(RR(log(ell,2))/machine_wordsize)
        self.Fp = Fp   # there 3 params are in classes PFCurve (BN, BLS12, KSS18, BLS24)
        self.Fpz = Fpz #
        self.h = h
        self.deg_h = h.degree()
        self.f = f
        self.g = g
        self.Rxy=Rxy
        self.aut = automorphism
        self.inv_zeta_Kh = inv_zeta_Kh
        self.w = w
        self.list_cost_tested = list()

        if alpha_f is not None and alpha_g is not None:
            self.alpha_f = alpha_f
            self.alpha_g = alpha_g
            self.with_alpha = True
        else:
            self.alpha_f = 0.0
            self.alpha_g = 0.0
            self.with_alpha = False

        self.check_coprime_ideals=True
        #
        if weight_per_row is None or weight_per_row <= 0:
            if not barbulescu_duquesne:
                self.weight_per_row = default_weight_per_row
            else:
                self.weight_per_row = barbulescu_duquesne_weight_per_row
        else:
            self.weight_per_row = weight_per_row
        
        if cst_filtering is None or cst_filtering <= 0:
            if not barbulescu_duquesne:
                self.cst_filtering = default_cst_filtering
            else:
                self.cst_filtering = barbulescu_duquesne_cst_filtering
        else:
            self.cst_filtering = cst_filtering
        if count_sieving is None:
            if not barbulescu_duquesne:
                self.count_sieving = True
            else:
                self.count_sieving = False
        else:
            self.count_sieving = count_sieving
        self.label = label
        self.barbulescu_duquesne = barbulescu_duquesne

        self.set_cost(log2_cost, A=A, log2_B=log2_B)

    
    def set_cost(self, cost, A=None, log2_B=None):
        if cost <= 0:
            raise ValueError("Error cost: should be a strictly positive number but received {}".format(cost))        
        self.cost = cost
        if A is None or log2_B is None:
            self.A, self.log2_B = get_parameters_A_log2B(self.cost, self.ell_wordsize, self.aut, self.deg_h, self.weight_per_row, self.cst_filtering, self.barbulescu_duquesne, self.count_sieving, self.w)
        else:
            self.A = A
            self.log2_B = log2_B
        self.log2_core_vol_sieving_space, self.inv_zeta_Kh, self.w = lg2_core_volume_sieving_space(self.A, self.h, inv_zeta_Kh=self.inv_zeta_Kh, w=self.w)
        #self.core_vol_sieving_space, self.w, self.inv_zeta_Kh = core_volume_sieving_space(self.A, self.h, inv_zeta_Kh=self.inv_zeta_Kh)
        #self.vol_sieving_space = volume_sieving_space(self.A, self.deg_h)
        self.log2_vol_sieving_space = lg2_volume_sieving_space(self.A, self.deg_h)
        self.logB = float(self.log2_B*log2)
        self.loglogB = float(log(self.logB)) # log(log(B)) where log=ln is natural logarithm (log(e) = 1)
        if not self.barbulescu_duquesne:
            self.log2_time_relcol = float(self.log2_vol_sieving_space - log(float(self.aut),2.0))
        else:# assume that it is free to avoid the duplicates due to the units that are roots of unity
            self.log2_time_relcol = float(self.log2_vol_sieving_space - log(float(self.aut*self.w),2.0))
        # in both cases, we assume that it it inherent to the sieve to get a proportion of duplicates and the "core" unique relations are 1/zeta_kh(2) of the total relations
        if self.count_sieving:
            self.log2_time_relcol_sieving_cost = self.log2_time_relcol + float(log(self.loglogB,2.0))
        else:
            self.log2_time_relcol_sieving_cost = self.log2_time_relcol

        self.log2_time_linalg, self.log2_size_FB, self.log2_size_matrix, self.logB = time_linalg(self.log2_B, self.ell_wordsize, self.weight_per_row, self.cst_filtering, self.barbulescu_duquesne, self.aut)
        self.log2_total_time = float(log(2.0**self.log2_time_relcol + 2.0**self.log2_time_linalg, 2.0))
        self.log2_total_time_sieving_cost = float(log(2.0**self.log2_time_relcol_sieving_cost + 2.0**self.log2_time_linalg, 2.0))

        #in [BD19], the size of the factor basis uses the rough estimate 2*B/log B whose log_2 is 1 + log2_B - log_2(log B)
        # Equation 2 of the model of cost in Barbulescu-Dquesne
        # cost = {number of relations to collect} + {cost of linear algebra}
        # cost = 2*B/(aut*log(B)) / (dickman_rho(log_2(Nf)/log_2(B)) * dickman_rho(log_2(Ng)/log_2(B)))
        #        + 2^7 * (B/(aut*log(B)*log_2(B)))^2
        # where aut = number of automorphisms, <= eta*kappa/gcd(eta*kappa)
        #                                         where eta*kappa=k and eta=deg(h)
        # size of the matrix is expected to be (size of factor basis)/(filtering_factor * aut)
        # = (2*B/log(B))/(log_2(B) * aut)
        # the cost of linear algebra is expected to be
        # the size of the matrix squared, times the weight per row (the non-zero entries) times some factor c_linalg that can be modeled to be 1/4 (not 1 but 1/4), finally
        # ((2*B/log(B))/(log_2(B) * aut))^2 * 128 / 4
        # there is no factor (log2_r/wordsize) in Barbulescu-Duquesne cost model
        self.log2_size_FB_BD = float(1.0 + self.log2_B - log(self.logB, 2.0))
        # consider log_2 c_filter = log2_B + automorphisms
        self.log2_size_matrix_BD = float(self.log2_size_FB_BD - log(self.log2_B, 2.0) - log(self.aut, 2.0))
        self.log2_time_linalg_BD = float(log(barbulescu_duquesne_weight_per_row,2.0) + log(barbulescu_duquesne_cst_linalg,2.0) + 2.0*self.log2_size_matrix_BD)
        # where for Barbulescu-Duquesne, weight_per_row = 128 and c_linalg = 1/4, hence 128/4 = 32 = 2^5, explaining why this is 2^5 and not 2^7.
        self.log2_total_time_BD = float(log(2.0**self.log2_time_relcol + 2.0**self.log2_time_linalg_BD, 2.0))
            
    def print_params(self):
        #def run_simulation_tnfs(p,Fp, Fpz,h,f,g,Rxy,A,log2_B,ell_wordsize,samples=10**5,inv_zeta_Kh=1.0,aut=1,alpha_f=0.0,alpha_g=0.0,check_coprime=True):
        if self.barbulescu_duquesne:
            print("barbulescu_duquesne=True, weight_per_row={}, count_sieving={}".format(self.weight_per_row, self.count_sieving))
        print("cost = {0} bits, deg_h = {1}, A = {2}, ell_wordsize = {3}, B = 2^{4:.3f} \n".format(self.cost, self.deg_h, self.A, self.ell_wordsize, float(self.log2_B)))
        print("vol sieving space = 2^{0:.2f}, core vol sieving = 2^{1:.2f}, w = {2}, 1/zeta_Kh(2) = {3:.6f}".format(float(self.log2_vol_sieving_space), float(self.log2_core_vol_sieving_space), self.w, float(self.inv_zeta_Kh)))
        if self.with_alpha:
            print("alpha_f ={0:7.4f} (basis e), alpha_g ={1:7.4f} (basis e), sum ={2:7.4f}".format(float(self.alpha_f), float(self.alpha_g), float(self.alpha_f+self.alpha_g)))
            print("alpha_f ={0:7.4f} (basis 2), alpha_g ={1:7.4f} (basis 2), sum ={2:7.4f}".format(float(self.alpha_f/log2), float(self.alpha_g/log2), float(self.alpha_f/log2+self.alpha_g/log2)))

    def simulation(self, samples):
        """
        :param samples: number of random coprime tuples in the relation collection to compute an average smoothness probability
                        uses at least 10^6 (takes ~20 min to run) to get a high precision
        """
        self.samples = samples
        self.avrg_log_Nf, self.avrg_log_Ng, self.avrg_smooth_proba_f, self.avrg_smooth_proba_g, \
            self.avrg_proba, self.err_norm_f, self.err_norm_g, self.err_proba_f, self.err_proba_g, self.err_proba, \
            self.std_dev_norm_f, self.std_dev_norm_g, self.std_dev_proba_f, self.std_dev_proba_g, self.std_dev_proba, \
            self.inv_zeta_Kh_exp, self.min_log_Nf, self.max_log_Nf, self.min_log_Ng, self.max_log_Ng = \
                statistics(self.h,self.f,self.g,self.Rxy,self.A,self.logB,self.samples,self.alpha_f,self.alpha_g)
        self.proba_rough = smoothness_proba(self.avrg_log_Nf,self.logB,self.alpha_f)*smoothness_proba(self.avrg_log_Ng,self.logB,self.alpha_g)
        #self.rels = self.core_vol_sieving_space*self.avrg_proba
        #self.rels_rough = self.core_vol_sieving_space*self.proba_rough
        # in log2 basis
        self.log2_proba_rough = float(lg2_smoothness_proba(self.avrg_log_Nf,self.logB,self.alpha_f) + lg2_smoothness_proba(self.avrg_log_Ng,self.logB,self.alpha_g))
        self.log2_avrg_proba = float(log(self.avrg_proba, 2.0))
        self.log2_rels = float(self.log2_core_vol_sieving_space + self.log2_avrg_proba)
        self.log2_rels_rough = float(self.log2_core_vol_sieving_space + self.log2_proba_rough)

    def print_adjust_relcol_time(self):
        """
        Given A, the joint smoothness probability in the number fields, adjust the
        relation collection space size, especially for large degree h and small A.

        INPUT: None
        RETURN: None

        For polynomial h of large degree, decreasing A makes the volume of the sieving space decrease too much,
        an alternative is to consider (to sieve) only a fraction of the volume, without changing A.

        volume without duplicates is (2A+1)^(2 deg h)/(2 w Dedekind_zeta_Kh(2))
        self.log2_core_vol_sieving_space, ... = lg2_core_volume_sieving_space(A, h, ...)
        """
        if not self.barbulescu_duquesne and self.count_sieving:
            log2_cost_sieving = RR(log(self.loglogB,2.0))
        else:
            log2_cost_sieving = float(0.0)
        if self.log2_rels > self.log2_size_FB:
            # do not use the total space for the relation collection, stop when enough rels are obtained
            # time constraint: stop when the time consumed is cost/2 (log_2 cost - 1)
            # where to put the gain thanks to an automorphism?
            # where does w = number of roots of unity up to +-1 play a role?
            log2_target_relcol_cost = RR(self.cost-1)
            log2_total_time_relcol_cost = float(log(2.0**log2_target_relcol_cost + 2.0**self.log2_time_linalg,2.0))
            print("adjusting (shrinking) volume sieving space")
            print("time relcol = 2^{0:.4f}".format(float(log2_target_relcol_cost)))
            print("time linalg = 2^{0:.4f}".format(float(self.log2_time_linalg)))
            if self.count_sieving:
                print("total time  = 2^{0:.4f} (counting sieving cost as ln(ln(B)))".format(log2_total_time_relcol_cost))
            else:
                print("total time  = 2^{0:.4f} (counting sieving cost as free (c_sieve=1))".format(log2_total_time_relcol_cost))

            if self.barbulescu_duquesne: # cost_sieving = 1, log2_cost_sieving = 0.0
                log2_vol_sieving_space = log2_target_relcol_cost - log2_cost_sieving + RR(log(self.aut,2.0))
                log2_rels = RR(log(self.inv_zeta_Kh,2.0) + log2_vol_sieving_space + self.log2_avrg_proba)
            else:
                log2_vol_sieving_space = log2_target_relcol_cost - log2_cost_sieving + RR(log(self.aut,2.0))
                log2_rels = RR(log(self.inv_zeta_Kh/self.w,2.0) + log2_vol_sieving_space + self.log2_avrg_proba)
            print("relations obtained:                                  2^{:.4f}".format(float(log2_rels)))
            # now minimal time to ensure enough relations
            # (2*A+1)^(2 * deg h)/(2 * w * zeta_Kh(2)) * avgr_proba = needed relations = self.log2_size_FB
            # minimal_vol_sieving_space = (2*A+1)^(2 * deg h)/(2 * w)
            # minimal_vol_sieving_space*inv_zeta_Kh*avrg_proba = needed_relations
            # minimal_vol_sieving_space/aut * cost_sieving = minimal_time_relcol
            log2_minimal_vol_sieving_space = RR(self.log2_size_FB - log(self.inv_zeta_Kh,2.0) - self.log2_avrg_proba)
            if not self.barbulescu_duquesne:
                log2_minimal_time_relcol = RR(log2_minimal_vol_sieving_space + RR(log(self.w,2.0)) - RR(log(self.aut,2.0)) + log2_cost_sieving)
            else:
                log2_minimal_time_relcol = RR(log2_minimal_vol_sieving_space - RR(log(self.aut,2.0)) + log2_cost_sieving)
            # rels_min = inv_zeta_Kh * time_rel_col_sieving_cost/time_sieving * avrg_proba
            log2_rels_min = RR(log(self.inv_zeta_Kh,2.0) + log2_minimal_vol_sieving_space + self.log2_avrg_proba)
            print("time relcol = 2^{0:.4f}".format(float(log2_minimal_time_relcol)))
            print("time linalg = 2^{0:.4f}".format(float(self.log2_time_linalg)))
            log2_total_time_relcol_cost = float(log(2.0**log2_minimal_time_relcol + 2.0**self.log2_time_linalg,2.0))
            if self.count_sieving:
                print("total time  = 2^{0:.4f} (counting sieving cost as ln(ln(B)))".format(log2_total_time_relcol_cost))
            else:
                print("total time  = 2^{0:.4f} (counting sieving cost as free (c_sieve=1))".format(log2_total_time_relcol_cost))
            print("relations obtained:                                  2^{:.4f}".format(float(log2_rels_min)))
        else:
            print("not enough relations, should increase A.")
            print("For the same smoothness probability (i.e. not taking into account the increasing norms due to increased A),")
            # re-compute a volume such that proba_smoothness * new_volume >= old self.log2_rels
            target_log2_rels = self.log2_size_FB
            target_log2_vol_sieving_space = target_log2_rels - self.log2_avrg_proba - float(log(self.inv_zeta_Kh/self.w,2.0))
            if self.barbulescu_duquesne: # assume avoiding the duplicates due to w is free, and cost_sieving = 1
                log2_cost_rel_col = target_log2_vol_sieving_space - float(log(self.w * self.aut,2.0)) + log2_cost_sieving
            else:
                log2_cost_rel_col = target_log2_vol_sieving_space - float(log(self.aut,2.0)) + log2_cost_sieving
            Amin, s1, Amax, s2 = find_A(self.deg_h, log2_cost_rel_col, self.A, self.count_sieving, self.log2_B, self.barbulescu_duquesne, self.w, self.aut)
            print("the volume should be at least 2^{:.3f}, obtained with minimal A = {}, for which cost is {:.3f}".format(float(target_log2_vol_sieving_space), Amin, float(s1)))

    def print_results(self):
        print("experimental 1/zeta_Kh(2) = {:.8f}".format(float(self.inv_zeta_Kh_exp)))
        print("theoretical  1/zeta_Kh(2) = {:.8f}".format(float(self.inv_zeta_Kh)))
        #print("avrg_log2_Nf = {}\navrg_log2_Ng = {}\navrg_smooth_proba_f = {}\navrg_smooth_proba_g = {}\navrg_proba  = {}\n".format(float(self.avrg_log_Nf/log2), float(self.avrg_log_Ng/log2), self.avrg_smooth_proba_f, self.avrg_smooth_proba_g, self.avrg_proba))
        print("err_norm_f  = {}\nerr_norm_g  = {}\nerr_proba_f = {}\nerr_proba_g = {}\nerr_proba   = {}\n".format(self.err_norm_f, self.err_norm_g, self.err_proba_f, self.err_proba_g, self.err_proba))
        print("std_dev_norm_f = {}\nstd_dev_norm_g = {}\nstd_dev_proba_f = {}\nstd_dev_proba_g = {}\nstd_dev_proba   = {}\n".format(self.std_dev_norm_f, self.std_dev_norm_g, self.std_dev_proba_f, self.std_dev_proba_g, self.std_dev_proba))
        
        print("A = {0}, B = 2^{1:.3f}, deg(h) = {2}, #{{units}} = w = {3}, samples = {4}".format(self.A,float(self.log2_B),self.deg_h,self.w,self.samples))
        print("vol_sieving_space = (2*A+1)^(2*{0})/(2*{1}) = 2^{2:.3f}".format(self.deg_h, self.w, float(self.log2_vol_sieving_space)))
        print("avrg_log2_Nf = {0:9.4f} (bits) avrg_log2_Ng = {1:9.4f} (bits) sum = {2:9.4f} (bits)".format(float(self.avrg_log_Nf/log2), float(self.avrg_log_Ng/log2), float((self.avrg_log_Nf+self.avrg_log_Ng)/log2)))
        print(" min_log2_Nf = {0:9.4f} (bits)  min_log2_Ng = {1:9.4f} (bits)".format(float(self.min_log_Nf/log2), float(self.min_log_Ng/log2)))
        print(" max_log2_Nf = {0:9.4f} (bits)  max_log2_Ng = {1:9.4f} (bits)".format(float(self.max_log_Nf/log2), float(self.max_log_Ng/log2)))
        
        print("smooth_proba(avrg_Nf,logB,alpha_f) = smooth_proba({0:.2f},2^{1:.2f},{2:.4f}) = {3} = 2^{4:.4f}".format(float(self.avrg_log_Nf*log2),float(self.log2_B),float(self.alpha_f), float(smoothness_proba(self.avrg_log_Nf,self.logB,self.alpha_f)),float(log(smoothness_proba(self.avrg_log_Nf,self.logB,self.alpha_f),2.0))))
        print("smooth_proba(avrg_Ng,logB,alpha_g) = smooth_proba({0:.2f},2^{1:.2f},{2:.4f}) = {3} = 2^{4:.4f}".format(float(self.avrg_log_Ng*log2),float(self.log2_B),float(self.alpha_g), float(smoothness_proba(self.avrg_log_Ng,self.logB,self.alpha_g)),float(log(smoothness_proba(self.avrg_log_Ng,self.logB,self.alpha_g),2.0))))
        print("prod of smooth proba of avrg norms: {0} = 2^{1:.4f}".format(float(self.proba_rough),float(log(self.proba_rough,2.0))))
        print("avrg_proba = {0} = 2^{1:.4f}".format(float(self.avrg_proba), self.log2_avrg_proba))

        print("relations obtained: core_vol_sieving_space * proba = 2^{0:.4f}".format(float(self.log2_rels)))
        print("relations obtained: core_vol_sieving_space * (rough proba) = 2^{0:.4f}".format(float(self.log2_rels_rough)))
        print("#{{factor base}} =~ 2LogIntegral(B) = 2^{0:.4f}".format(self.log2_size_FB))
        print("#{{factor base}} ~ 2*B/log(B)       = 2^{0:.4f}".format(self.log2_size_FB_BD))
        if not self.barbulescu_duquesne:
            print("size matrix = size factor base (=2*log_integral(B)) / (cst_filtering={}) = 2^{:.4f} (worst case)".format(self.cst_filtering,self.log2_size_matrix))
        else:
            print("size matrix = size factor base (=2B/log B) / (ratio_filtering=log_2 B={} * aut={}) = 2^{:.4f} (worst case)".format(self.log2_B,self.aut,self.log2_size_matrix))
        
        if not self.count_sieving:
            print("time relcol = 2^{0:.4f}".format(self.log2_time_relcol))
        else:
            print("time relcol = 2^{0:.4f} (counting sieving cost as ln(ln(B)))".format(self.log2_time_relcol_sieving_cost))
        print("time linalg = 2^{0:.4f}".format(self.log2_time_linalg))
        if not self.count_sieving:
            print("total time  = 2^{0:.4f}".format(self.log2_total_time))
        else:
            print("total time  = 2^{0:.4f} (counting sieving cost as ln(ln(B)))".format(self.log2_total_time_sieving_cost))
        self.print_adjust_relcol_time()

    def adjust_cost(self,samples):
        self.list_cost_tested.append(self.cost)
        while (self.log2_rels < self.log2_size_FB) or (self.log2_rels > 0.6+self.log2_size_FB):
            cost_old = self.cost
            if self.log2_rels < self.log2_size_FB:
                # compute adjusted cost at least for relation collection
                if self.log2_rels >= self.log2_size_FB - 0.8:
                    cost = self.cost+1
                else:
                    if self.count_sieving:
                        log2_cost_sieving = RR(log(self.loglogB,2.0))
                    else:
                        log2_cost_sieving = float(0.0)
                    log2_minimal_vol_sieving_space = RR(self.log2_size_FB - log(self.inv_zeta_Kh,2.0) - self.log2_avrg_proba)
                    log2_minimal_time_relcol = RR(log2_minimal_vol_sieving_space - RR(log(self.aut,2.0)) + log2_cost_sieving)
                    cost = ceil(log2_minimal_time_relcol+1)
                if cost == cost_old:
                    cost = cost+1
                if cost in self.list_cost_tested:
                    break # there is a loop here
                print("not enough rels with cost={}, re-run with cost={}".format(cost_old, cost))
            else: #elif self.log2_rels > 0.6 + self.log2_size_FB:
                if self.log2_rels <= self.log2_size_FB + 1.5:
                    cost = self.cost-1
                else:
                    if self.count_sieving:
                        log2_cost_sieving = RR(log(self.loglogB,2.0))
                    else:
                        log2_cost_sieving = float(0.0)
                    log2_minimal_vol_sieving_space = RR(self.log2_size_FB - log(self.inv_zeta_Kh,2.0) - self.log2_avrg_proba)
                    log2_minimal_time_relcol = RR(log2_minimal_vol_sieving_space - RR(log(self.aut,2.0)) + log2_cost_sieving)
                    cost = ceil(log2_minimal_time_relcol+1)
                if cost == cost_old:
                    cost = cost-1
                if cost in self.list_cost_tested:
                    break # there is a loop here
                print("too many rels with cost={}, re-run with cost={}".format(cost_old, cost))
            self.list_cost_tested.append(cost)
            self.set_cost(cost)
            self.print_params()
            self.simulation(samples=samples)
            self.print_results()
            print("#::::::::::::::")

class Simulation_TNFS_BD18():
    
    def random_vec_bad_randint(A,size):
        # to investigate by how much a bad call to randint changes the results
        #:param A: bound on the integer coefficients to take at random
        #:param size: the length of the random tuple
        #:returns: a tuple of random integers in [-A,A+1]
        #
        a = [randint(-A,A+1) for i in range(size)]
        return a

    def statistics_BD18(h,f,g,Rxy,A,logB,samples,corrected_randint=False,check_coprime=False,alpha_f=0.0,alpha_g=0.0):
        #
        #statistics with conventions and formulas from [BarbulescuDuquesne18], Journal of Crypto
        #preprint http://eprint.iacr.org/2017/334
        #
        deg_h=h.degree()
        log_Nf =[0.0 for i in range(samples)]
        log_Ng =[0.0 for i in range(samples)]
        proba_f = [0.0 for i in range(samples)]
        proba_g = [0.0 for i in range(samples)]
        Kh = NumberField(h, 'ah')
        for i in range(samples):
            if not corrected_randint:
                a=random_vec_bad_randint(A,deg_h)
                b=random_vec_bad_randint(A,deg_h)
            else:
                # a cause for larger norms: randint(-A,A+1) instead of randint(-A,A)
                # use below to check the difference
                a=random_vec(A,deg_h)
                b=random_vec(A,deg_h)
                # this test is not in Barbulescu--Duquesne paper:
            if check_coprime:
                coprime_ideal=gcd(gcd(a), gcd(b)) == 1 and (Kh.ideal(Kh(a))+Kh.ideal(Kh(b))==Kh.ideal(1))
                while not coprime_ideal:
                    if not corrected_randint:
                        a=random_vec_bad_randint(A,deg_h)
                        b=random_vec_bad_randint(A,deg_h)
                    else:
                        a=random_vec(A,deg_h)
                        b=random_vec(A,deg_h)
                    coprime_ideal=(Kh.ideal(Kh(a))+Kh.ideal(Kh(b))==Kh.ideal(1))
            #a=(1+2*y) + (3+4*y)*x
            #h.resultant(a.resultant(f0,x),y)
            log_Nf[i] = log2*int(ceil(log(RR(abs(h.resultant(f.resultant(Rxy([a,b]))))),2)))
            log_Ng[i] = log2*int(ceil(log(RR(abs(h.resultant(g.resultant(Rxy([a,b]))))),2)))
            # the average norm is computed over ceil values of log_2(Nf), log_2(Ng)
            proba_f[i] = smoothness_proba(RR(log_Nf[i]), logB, alpha_f)
            proba_g[i] = smoothness_proba(RR(log_Ng[i]), logB, alpha_g)
        # average
        avrg_log_Nf = RR(sum(log_Nf) / samples)
        avrg_log_Ng = RR(sum(log_Ng) / samples)
        avrg_proba_f = RR(sum(proba_f) / samples)
        avrg_proba_g = RR(sum(proba_g) / samples)
        prod_proba = [RR(proba_f[i]*proba_g[i]) for i in range(samples)]
        avrg_proba = RR(sum(prod_proba)/samples)
        # variance: sum square of diff between values and mean value    
        variance_norm_f = RR(sum([(log_Nf[i]-avrg_log_Nf)**2 for i in range(samples)]))
        variance_norm_g = RR(sum([(log_Ng[i]-avrg_log_Ng)**2 for i in range(samples)]))
        variance_proba_f = RR(sum([(proba_f[i]-avrg_proba_f)**2 for i in range(samples)]))
        variance_proba_g = RR(sum([(proba_g[i]-avrg_proba_g)**2 for i in range(samples)]))
        variance_proba = RR(sum([(prod_proba[i]-avrg_proba)**2 for i in range(samples)]))
        # standard deviation
        std_dev_norm_f = RR(sqrt(variance_norm_f/(samples-1)))
        std_dev_norm_g = RR(sqrt(variance_norm_g/(samples-1)))
        std_dev_proba_f = RR(sqrt(variance_proba_f/(samples-1)))
        std_dev_proba_g = RR(sqrt(variance_proba_g/(samples-1)))
        std_dev_proba = RR(sqrt(variance_proba/(samples-1)))
        
        # error
        err_norm_f = float(RR(100*std_dev_norm_f/sqrt(samples)/avrg_log_Nf))
        err_norm_g = float(RR(100*std_dev_norm_g/sqrt(samples)/avrg_log_Ng))
        err_proba_f = float(RR(100*std_dev_proba_f/sqrt(samples)/avrg_proba_f))
        err_proba_g = float(RR(100*std_dev_proba_g/sqrt(samples)/avrg_proba_g))
        err_proba = float(RR(100*std_dev_proba/sqrt(samples)/avrg_proba))
        
        # cost
        avrg_log_Nf = float(avrg_log_Nf)
        avrg_log_Ng = float(avrg_log_Ng)
        avrg_proba_f = float(avrg_proba_f)
        avrg_proba_g = float(avrg_proba_g)
        avrg_proba = float(avrg_proba)
        
        std_dev_norm_f = float(std_dev_norm_f)
        std_dev_norm_g = float(std_dev_norm_g)
        std_dev_proba_f = float(std_dev_proba_f)
        std_dev_proba_g = float(std_dev_proba_g)
        std_dev_proba = float(std_dev_proba)
        
        return avrg_log_Nf, avrg_log_Ng, avrg_proba_f, avrg_proba_g, avrg_proba, err_norm_f, err_norm_g, err_proba_f, err_proba_g, err_proba, std_dev_norm_f, std_dev_norm_g, std_dev_proba_f, std_dev_proba_g, std_dev_proba, min(log_Nf), max(log_Nf), min(log_Ng), max(log_Ng)

    def run_simulation_tnfs_BD18(p,h,f,g,Rxy,A,log2_B,ell_wordsize,samples=10**5,inv_zeta_Kh=1.0,aut=1,alpha_f=0.0,alpha_g=0.0,BD18_estimates=False,corrected_randint=True,check_coprime=True):
    
        print("\nTHE SAME WITH [BarbulescuDuquesne18] TECHNIQUES\n")
    
        print("corrected_randint = {}".format(corrected_randint))
        print("check_coprime     = {}".format(check_coprime))
    
        avrg_log_Nf_BD, avrg_log_Ng_BD, avrg_smooth_proba_f_BD, avrg_smooth_proba_g_BD, avrg_proba_BD, err_norm_f_BD, err_norm_g_BD, err_proba_f_BD, err_proba_g_BD, err_proba_BD, std_dev_norm_f_BD, std_dev_norm_g_BD, std_dev_proba_f_BD, std_dev_proba_g_BD, std_dev_proba_BD, min_log_Nf, max_log_Nf, min_log_Ng, max_log_Ng = statistics_BD18(h,f,g,Rxy,A,logB,samples,corrected_randint=corrected_randint,check_coprime=check_coprime)
    
        print("avrg_log2_Nf_BD = {}\navrg_log2_Ng_BD = {}\navrg_smooth_proba_f_BD = {}\navrg_smooth_proba_g_BD = {}\navrg_proba_BD  = {}\n".format(float(avrg_log_Nf_BD/log2), float(avrg_log_Ng_BD/log2), avrg_smooth_proba_f_BD, avrg_smooth_proba_g_BD, avrg_proba_BD))
        print("err_norm_f_BD  = {}\nerr_norm_g_BD  = {}\nerr_proba_f_BD = {}\nerr_proba_g_BD = {}\nerr_proba_BD   = {}\n".format( err_norm_f_BD, err_norm_g_BD, err_proba_f_BD, err_proba_g_BD, err_proba_BD))
        print("std_dev_norm_f_BD = {}\nstd_dev_norm_g_BD = {}\nstd_dev_proba_f_BD = {}\nstd_dev_proba_g_BD = {}\nstd_dev_proba_BD   = {}\n".format(std_dev_norm_f_BD, std_dev_norm_g_BD, std_dev_proba_f_BD, std_dev_proba_g_BD, std_dev_proba_BD))
    
        print("A = {0}, B = 2^{1:.3f}, deg_h={2}, #{{roots of unity/+-1}} = w = {3}, samples = {4}".format(A,float(log2_B),deg_h,w,samples))
        print("vol_sieving_space = (2*A+1)^(2*{0})/(2*{1}) = 2^{2:.3f}".format(deg_h, w, float(log(vol_sieving_space, 2.0))))
        print("avrg_log2_Nf = {0:.4f} (bits) avrg_log2_Ng = {1:.4f} (bits)".format(float(avrg_log_Nf_BD/log2), float(avrg_log_Ng_BD/log2)))
        print(" min_log2_Nf = {0:.4f} (bits)  min_log2_Ng = {1:.4f} (bits)".format(float(min_log_Nf/log2), float(min_log_Ng/log2)))
        print(" max_log2_Nf = {0:.4f} (bits)  max_log2_Ng = {1:.4f} (bits)".format(float(max_log_Nf/log2), float(max_log_Ng/log2)))

        print("smooth_proba(avrg_Nf,logB,alpha_f) = {0} = 2^{1:.4f}".format(float(smoothness_proba(avrg_log_Nf_BD,logB,alpha_f)),float(log(smoothness_proba(avrg_log_Nf_BD,logB,alpha_f),2.0))))
        print("smooth_proba(avrg_Ng,logB,alpha_g) = {0} = 2^{1:.4f}".format(float(smoothness_proba(avrg_log_Ng_BD,logB,alpha_g)),float(log(smoothness_proba(avrg_log_Ng_BD,logB,alpha_g),2.0))))
        proba_rough_BD = float(smoothness_proba(avrg_log_Nf_BD,logB,alpha_f)*smoothness_proba(avrg_log_Ng_BD,logB,alpha_g))
        print("prod of smooth proba of avrg norms: {0} = 2^{1:.4f}".format(proba_rough_BD, float(log(proba_rough_BD,2.0))))
        print("avrg_proba = {0} = 2^{1:.4f}".format(float(avrg_proba_BD),float(log(avrg_proba_BD,2.0))))
        
        rels_BD = core_vol_sieving_space*avrg_proba_BD
        rels_rough_BD = core_vol_sieving_space*proba_rough_BD
        print("relations obtained: vol_sieving_space * proba = 2^{0:.4f}".format(float(log(rels_BD,2.0))))
        print("relations obtained: vol_sieving_space * (rough proba) = 2^{0:.4f}".format(float(log(rels_rough_BD,2.0))))
        print("#{{factor base}} =~ 2LogIntegral(B) = 2^{0:.4f}".format(log2_size_FB))
        print("#{{factor base}} ~ 2*B/log(B)       = 2^{0:.4f}".format(log2_size_FB_BD))
        print("size matrix = size factor base / log2_B = 2^{0:.4f} ".format(log2_size_matrix_BD))
        print("time linalg = 2^{0:.4f}".format(log2_time_linalg_BD))
        print("time relcol = 2^{0:.4f}".format(log2_time_relcol))
        print("total time  = 2^{0:.4f}".format(log2_total_time_BD))

