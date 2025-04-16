import sys
import re
import os
import pprint

import tnfs

import tnfs.curve.kss
from tnfs.curve.kss import KSS
from tnfs.curve.kss import allowed_k as allowed_k_kss
import tnfs.curve.bls
from tnfs.curve.bls import BLS
from tnfs.curve.bls import allowed_k as allowed_k_bls
import tnfs.curve.bn
from tnfs.curve.bn import BN
from tnfs.curve.bn import allowed_k as allowed_k_bn
import tnfs.curve.freeman
from tnfs.curve.freeman import Freeman
from tnfs.curve.freeman import allowed_k as allowed_k_freeman
import tnfs.curve.aurifeuillean
from tnfs.curve.aurifeuillean import Aurifeuillean
from tnfs.curve.aurifeuillean import allowed_k as allowed_k_auri
import tnfs.curve.fotiadis_martindale
from tnfs.curve.fotiadis_martindale import FotiadisMartindale
from tnfs.curve.fotiadis_martindale import allowed_code as allowed_code_fm
from tnfs.curve.fst62 import FST62
from tnfs.curve.fst63 import FST63
from tnfs.curve.fst64 import FST64
from tnfs.curve.fst66 import FST66
from tnfs.curve.fst67 import FST67
from tnfs.curve.cyclotomic import Cyclotomic
from tnfs.curve.cyclotomic import allowed_k as allowed_k_cyclo

import tnfs.curve.pairing_friendly_curve

from tnfs.simul.polyselect import Polyselect
from tnfs.simul.polyselect_utils import automorphism_factor, is_even, is_palindrome, is_antipalindrome
from tnfs.simul.simulation_tnfs import Simulation_TNFS
from tnfs.simul.simulation_nfs import Simulation_NFS
from tnfs.alpha.alpha_tnfs_2d import alpha_TNFS_2d
from tnfs.alpha.alpha2d import alpha2d
from tnfs.alpha.alpha3d import alpha3d

# sage test_curves.sage --fst64 -k 28 -i 0 -samples 10000
# k=16 D=1 deg(px) = 16

args=sys.argv
print("usage: sage {} [--kss | --bls | --bn | --freeman | --cyclo | --auri | --fm | --fst62 | --fst63 | --fst64 | --fst66] [-choice_kss <choice>] [-code <code FM>] -k <k> -D <D> [-e0 <e0>] [-a <auri_a>] [--special | --conj | --jouxlercier | --sarkarsingh | --basem] [--lower_degree_px] [-deg_px_dec <deg_px_dec>] [-deg_h <deg_h>] [-cost <cost>] [-sievingdim <sieving_dim>] [--no-alpha] [--barbulescu_duquesne] -i <idx> [-samples <samples>]".format(args[0]))

curve = None # KSS or BLS or BN or Aurifeuillean or FotiadisMartindale
k = None
allowed_k = None
code = None # for FotiadisMartindale only
D = None
e0 = None
a_auri = None
choice_kss = None
idx = None
samples = None
cost = None
sieving_dim = None
barbulescu_duquesne=False

Special = True; Conj = False; JL = False; JLSV1 = False; SSingh = False; Base_m = False
deg_h = None
lower_degree_px = False
deg_px_dec = 2 # decrease the degree of px by a factor deg_px_dec -> P(z^deg_px_dec) = p(x)
compute_alpha = True

i=1
cmd_options = ["--kss", "--bls", "--bn", "--freeman", "--cyclo", "--auri", "--fm", "--fst62", "--fst63", "--fst64", "--fst66", "--fst67", "-choice_kss", "-code", "-k", "-D", "-e0", "-a", "--special", "--conj", "--jouxlercier", "--jlsv1", "--sarkarsingh", "--basem", "-deg_h", "-cost", "--lower_degree_px", "-deg_px_dec", "--no-alpha", "-sievingdim", "--barbulescu_duquesne"]

while i < len(args):
    if args[i] == "--bls":
        curve = BLS; str_curve = "BLS"; str_curve_lowcase = "bls"
        curve_path = tnfs.curve.bls
        allowed_k = allowed_k_bls
    elif args[i] == "--kss":
        curve = KSS; str_curve = "KSS"; str_curve_lowcase = "kss"
        curve_path = tnfs.curve.kss
        allowed_k = allowed_k_kss
    elif args[i] == "--bn":
        curve = BN; str_curve = "BN"; str_curve_lowcase = "bn"
        curve_path = tnfs.curve.bn
        allowed_k = allowed_k_bn
        k = 12
    elif args[i] == "--freeman":
        curve = Freeman; str_curve = "Freeman"; str_curve_lowcase = "freeman"
        curve_path = tnfs.curve.freeman
        allowed_k = allowed_k_freeman
        k = 10
    elif args[i] == "--auri":
        curve = Aurifeuillean; str_curve = "Auri"; str_curve_lowcase = "auri"
        curve_path = tnfs.curve.aurifeuillean
        allowed_k = allowed_k_auri
    elif args[i] == "--fm":
        curve = FotiadisMartindale; str_curve = "FM"; str_curve_lowcase = "fm"
        curve_path = tnfs.curve.fotiadis_martindale
        allowed_code = allowed_code_fm
    elif args[i] == "--fst62":
        curve = FST62; str_curve = "FST62_k"; str_curve_lowcase = "fst62_k"
        curve_path = tnfs.curve.fst62
    elif args[i] == "--fst63":
        curve = FST63; str_curve = "FST63_k"; str_curve_lowcase = "fst63_k"
        curve_path = tnfs.curve.fst63
    elif args[i] == "--fst64":
        curve = FST64; str_curve = "FST64_k"; str_curve_lowcase = "fst64_k"
        curve_path = tnfs.curve.fst64
    elif args[i] == "--fst66":
        curve = FST66; str_curve = "FST66_k"; str_curve_lowcase = "fst66_k"
        curve_path = tnfs.curve.fst66
    elif args[i] == "--fst67":
        curve = FST67; str_curve = "FST67_k"; str_curve_lowcase = "fst67_k"
        curve_path = tnfs.curve.fst67
    elif args[i] == "--special":
        Special = True;  Conj = False; JL = False; JLSV1 = False; SSingh = False; Base_m = False
    elif args[i] == "--conj":
        Special = False; Conj = True;  JL = False; JLSV1 = False; SSingh = False; Base_m = False
    elif args[i] == "--jouxlercier":
        Special = False; Conj = False; JL = True; JLSV1 = False;  SSingh = False; Base_m = False
    elif args[i] == "--jlsv1":
        Special = False; Conj = False; JL = False; JLSV1 = True;  SSingh = False; Base_m = False
    elif args[i] == "--sarkarsingh":
        Special = False; Conj = False; JL = False; JLSV1 = False; SSingh = True;  Base_m = False
    elif args[i] == "--basem":
        Special = False; Conj = False; JL = False; JLSV1 = False; SSingh = False; Base_m = True
    elif args[i] == "--lower_degree_px":
        lower_degree_px = True
    elif args[i] == "--no-alpha":
        compute_alpha = False
    elif args[i] == "--barbulescu_duquesne":
        barbulescu_duquesne = True
    elif args[i] == "-sievingdim" and (i+1) < len(args) and args[i+1] not in cmd_options:
        sieving_dim = Integer(args[i+1])
        i += 1
    elif args[i] == "-deg_px_dec" and (i+1) < len(args) and args[i+1] not in cmd_options:
        deg_px_dec = Integer(args[i+1])
        i += 1
    elif args[i] == "-deg_h" and (i+1) < len(args) and args[i+1] not in cmd_options:
        deg_h = Integer(args[i+1])
        i += 1
    elif args[i] == "-k" and (i+1) < len(args) and args[i+1] not in cmd_options:
        k = Integer(args[i+1])
        i += 1
    elif args[i] == "-code" and (i+1) < len(args) and args[i+1] not in cmd_options:
        code = Integer(args[i+1])
        i += 1
    elif args[i] == "-choice_kss" and (i+1) < len(args) and args[i+1] not in cmd_options:
        choice_kss = Integer(args[i+1])
        i += 1
    elif args[i] == "-D" and (i+1) < len(args) and args[i+1] not in cmd_options:
        D = Integer(args[i+1])
        i += 1
    elif args[i] == "-e0" and (i+1) < len(args) and args[i+1] not in cmd_options:
        e0 = Integer(args[i+1])
        i += 1
    elif args[i] == "-a" and (i+1) < len(args) and args[i+1] not in cmd_options:
        a_auri = Integer(args[i+1])
        i += 1
    elif (args[i] == "-idx" or args[i] == "-i") and (i+1) < len(args) and args[i+1] not in cmd_options:
        idx = Integer(args[i+1])
        i += 1
    elif args[i] == "-samples" and (i+1) < len(args) and args[i+1] not in cmd_options:
        samples = Integer(args[i+1])
        i += 1
    elif args[i] == "-cost" and (i+1) < len(args) and args[i+1] not in cmd_options:
        cost = Integer(args[i+1])
        i += 1
    i += 1

if curve is None:
    raise ValueError("missing curve type: one of --kss or --bls or --bn or --freeman or --cyclo or --auri or --fm or --fst62 or --fst63 or --fst64 or --fst66 or --fst67")

if curve == FotiadisMartindale:
    if code is None:
        raise ValueError("missing family code, possible values with {}: {}".format(str_curve, allowed_code))
    elif code not in allowed_code:
        raise ValueError("family code ={} but possible values with {} are {}".format(code, str_curve, allowed_code))
elif k is None:
    raise ValueError("missing embedding degree k, possible values with {}: {}".format(str_curve, allowed_k))
elif allowed_k is not None and k not in allowed_k:
    raise ValueError("embedding degree k={} but possible values with {} are {}".format(k, str_curve, allowed_k))

if curve == FotiadisMartindale:
    print("curve={} code={} idx={} samples={}".format(curve,code,idx,samples))
else:
    print("curve={} k={} D={} idx={} samples={}".format(curve,k,D,idx,samples))

# match the test vectors in tnfs/param/testvector_sparseseed.py

if curve == BN:
    from tnfs.param.testvector_sparseseed import test_vector_bn as test_vector

elif curve == Freeman:
    from tnfs.curve.test_freeman import test_vector_freeman as test_vector

elif curve == BLS:
    if k==12:
        from tnfs.param.testvector_sparseseed import test_vector_bls12 as test_vector
    elif k==15:
        from tnfs.param.testvector_other_sparseseed import test_vector_sparse_bls15 as test_vector
    elif k==21:
        from tnfs.param.testvector_other_sparseseed import test_vector_sparse_bls21 as test_vector
    elif k==24:
        from tnfs.param.testvector_sparseseed import test_vector_bls24 as test_vector
    elif k==27:
        from tnfs.param.testvector_other_sparseseed import test_vector_sparse_bls27 as test_vector
    elif k==48:
        from tnfs.param.testvector_sparseseed import test_vector_bls48 as test_vector
    else:
        raise ValueError("k={} not implemented for BLS".format(k))

elif curve == KSS:
    if k==16:
        from tnfs.param.testvector_sparseseed import test_vector_kss16 as test_vector
    elif k==18:
        from tnfs.param.testvector_sparseseed import test_vector_kss18 as test_vector
    elif k==20 and (choice_kss is None or choice_kss == 0):
        from tnfs.param.testvector_other_sparseseed import test_vector_kss20a as test_vector
    elif k==20 and (choice_kss == 1):
        from tnfs.param.testvector_other_sparseseed import test_vector_kss20b as test_vector
    elif k==22:# and (D is None or D == 7):
        from tnfs.param.testvector_other_sparseseed import test_vector_kss22d7 as test_vector
        D = 7
        choice_kss = 1
    elif k==28:
        from tnfs.param.testvector_other_sparseseed import test_vector_sparse_kss28i0 as test_vector
        D = 1
        choice_kss = 0
    elif k==32:
        from tnfs.param.testvector_sparseseed import test_vector_kss32 as test_vector
    elif k==36:
        from tnfs.param.testvector_sparseseed import test_vector_kss36 as test_vector
    elif k==40:
        from tnfs.param.testvector_sparseseed import test_vector_kss40 as test_vector
    elif k==54:
        from tnfs.param.testvector_sparseseed import test_vector_kss54 as test_vector
    else:
        raise ValueError("k={} not implemented for KSS".format(k))

elif curve == FotiadisMartindale:
    if code == 17:
        from tnfs.param.testvector_other_sparseseed import test_vector_sparse_fm12_17 as test_vector
    if code == 18:
        from tnfs.param.testvector_other_sparseseed import test_vector_sparse_fm12_18 as test_vector
    elif code == 21:
        from tnfs.param.testvector_other_sparseseed import test_vector_sparse_fm15_21 as test_vector
    elif code == 22:
        from tnfs.param.testvector_other_sparseseed import test_vector_sparse_fm15_22 as test_vector
    elif code == 23:
        from tnfs.param.testvector_other_sparseseed import test_vector_sparse_fm16_23 as test_vector
    elif code == 25:
        from tnfs.param.testvector_other_sparseseed import test_vector_sparse_fm18_25 as test_vector
    elif code == 28:
        from tnfs.param.testvector_other_sparseseed import test_vector_sparse_fm16_28 as test_vector
    elif code == 27:
        from tnfs.param.testvector_other_sparseseed import test_vector_sparse_fm20_27 as test_vector
    else:
        raise ValueError("k={} FotiadisMartindale: seeds not available".format(k))

elif curve == Aurifeuillean:
    if k==18:
        from tnfs.param.testvector_other_sparseseed import test_vector_sparse_auri18_D3_a3_e01 as test_vector
        D = 3
        a_auri = 3
        e0 = 1
    elif k == 20:
        if (D is None) or (D == 1):
            D = 1
            a_auri = 2
            if e0 is None or e0 == 9:
                from tnfs.param.testvector_other_sparseseed import test_vector_sparse_auri20_D1_a2_e09 as test_vector
                e0 = 9
            else:
                from tnfs.param.testvector_other_sparseseed import test_vector_sparse_auri20_D1_a2_e019 as test_vector
                e0 = 19
    else:
        raise ValueError("k={} Aurifeuillean: seeds not available".format(k))
    
elif curve == FST63:
    if k==14:
        from tnfs.param.testvector_other_sparseseed import test_vector_sparse_fst63_k14 as test_vector
    elif k==22:
        from tnfs.param.testvector_other_sparseseed import test_vector_fst63_k22 as test_vector
    else:
        raise ValueError("k={} FST63: seeds not available".format(k))

elif curve == FST64:
    if k==28:
        from tnfs.param.testvector_other_sparseseed import test_vector_sparse_fst64_k28 as test_vector
    else:
        raise ValueError("k={} FST64: seeds not available".format(k))

elif curve == FST66:
    if k==24:        
        from tnfs.param.testvector_other_sparseseed import test_vector_sparse_fst66_k24 as test_vector
    elif k==22:
        from tnfs.param.testvector_other_sparseseed import test_vector_fst66_k22 as test_vector
    elif k==20:
        from tnfs.param.testvector_other_sparseseed import test_vector_sparse_fst66_k20 as test_vector
    else:
        raise ValueError("k={} FST66: seeds not available".format(k))
elif curve == FST67:
    if k==12:
        from tnfs.param.testvector_other_sparseseed import test_vector_sparse_fst67_k12 as test_vector
    else:
        raise ValueError("k={} FST67: seeds not available".format(k))
else:
    raise ValueError("error no precomputed test vector found with curve={} k={} code={}".format(curve, k, code))

QQx = QQ['x']; (x,) = QQx._first_ngens(1)
if curve == Aurifeuillean:
    px, rx, tx, cx, yx, betax, lambx, D, a_auri, exp_tr, automorphisms, m, u_m, cofactor_r = curve_path.polynomial_params(k, D, a_auri, e0)
elif curve == FotiadisMartindale:
    px, rx, tx, cx, yx, betax, lambx, D, k, m, u_m = curve_path.polynomial_params_from_code(code)
elif curve == Cyclotomic:
    px, rx, tx, cx, yx, betax, lambx, D, l, exp_tr, m, u_m = curve_path.polynomial_params(k, D, l, e0)
elif curve == KSS:
    px, rx, tx, cx, yx, betax, lambx, D = curve_path.polynomial_params(k, choice_kss, D)
else:
    px, rx, tx, cx, yx, betax, lambx, D = curve_path.polynomial_params(k)
# for Freeman curves, D is a quadratic polynomial

px_denom = lcm([ci.denom() for ci in px.list()])
rx_denom = lcm([ci.denom() for ci in rx.list()])
tx_denom = lcm([ci.denom() for ci in tx.list()])
if px_denom > 1:
    print("px = ({})/{}".format(px*px_denom, px_denom))
else:
    print("px = {}".format(px))
if rx_denom > 1:
    print("rx = ({})/{}".format(rx*rx_denom, rx_denom))
else:
    print("rx = {}".format(rx))
if tx_denom > 1:
    print("tx = ({})/{}".format(tx*tx_denom, tx_denom))
else:
    print("tx = {}".format(tx))


print(" i    p   p^k cost dh snfs dim  GJL df sd SSingh df dg sd (all p, pk, cost in bits)")
i = max(0,idx-2)
for vec in test_vector[max(0,idx-2):min(len(test_vector),idx+3)]:
    u = vec['u']
    pnbits = vec['pnbits']
    p = ZZ(px(ZZ(u)))
    lnpk = ceil((k)*RR(log(p,2)))
    if 'cost_S' in vec and 'deg_h_S' in vec:
        cost_S = vec['cost_S']
        deg_h_S = vec['deg_h_S']
    else:
        cost_S = "???"
        deg_h_S = "??"
    if 'cost_C' in vec and 'deg_h_C' in vec:
        cost_C = vec['cost_C']
        deg_h_C = vec['deg_h_C']
        print("{:2d} {:4d} {:5d} {:4s} {:2s} {:4s} {:2s}".format(i, pnbits, lnpk, str(cost_S), str(deg_h_S), str(cost_C), str(deg_h_C)))
    else:
        print("{:2d} {:4d} {:5d} {:4s} {:2s}".format(i, pnbits, lnpk, str(cost_S), str(deg_h_S)))
    i += 1

vec = test_vector[idx]
u, pnbits, rnbits = vec['u'], vec['pnbits'], vec['rnbits']
if 'cost_S' in vec and 'deg_h_S' in vec:
    cost_S, deg_h_S = vec['cost_S'], vec['deg_h_S']
else:
    cost_S = None
    deg_h_S = None
if 'cost_C' in vec and 'deg_h_C' in vec:
    cost_C = vec['cost_C']
    deg_h_C = vec['deg_h_C']
else:
    if cost_S is not None:
        cost_C = 1.2*cost_S
    else:
        cost_C = None
    deg_h_C = factor(k)[0][0] # the smallest divisor of k
if curve==Freeman:
    D = vec['D']
if D==1 or D==4:
    a = vec['a']
elif D==3:
    b = vec['b']
else:
    a,b = vec['a'], vec['b']

if 'cofact_r' in vec:
    cofact_r = vec['cofact_r']
else:
    cofact_r = 1

if "cost_JL" in vec:
    cost_JL = vec["cost_JL"]
else:
    cost_JL = cost_S
if "deg_h_JL" in vec:
    deg_h_JL = vec["deg_h_JL"]
else:
    deg_h_JL = deg_h_S
if "deg_f_JL" in vec:
    deg_f_JL = vec["deg_f_JL"]
else:
    deg_f_JL = 4
if "deg_f_Base_m" in vec:
    deg_f_Base_m = vec["deg_f_Base_m"]
else:
    deg_f_Base_m = 4


if float(log(abs(u),2)) >= 256.0 or pnbits >= 512:
    proof.arithmetic(False)

if Special:
    if cost is None:
        cost = cost_S
    if deg_h is None:
        deg_h = deg_h_S
elif Conj:
    if cost is None:
        cost = cost_C
    if deg_h is None:
        deg_h = deg_h_C
elif SSingh:
    deg_aux1 = 3
    max_coeff_aux1 = 2
    if 'deg_aux_SS' in vec and 'cost_SS' in vec and 'deg_h_SS' in vec:
        deg_h_SS, deg_aux_SS, cost_SS = vec['deg_h_SS'], vec['deg_aux_SS'], vec['cost_SS']
        if cost is None:
            cost = cost_SS
        if deg_h is None:
            deg_h = deg_h_SS
        deg_aux1 = deg_aux_SS
    else:
        raise ValueError("Please provide cost_SS, deg_h_SS and deg_aux_SS for SarkarSingh")
elif JL:
    if cost is None:
        cost = cost_JL
    if deg_h is None:
        deg_h = deg_h_JL
elif Base_m:
    if cost is None:
        cost = cost_JL
    if deg_h is None:
        deg_h = deg_h_JL

print("p {} bits, deg_h={}, cost = {}".format(pnbits, deg_h, cost))

print("{}-k{}-D{}-p{}".format(str_curve, k, D, pnbits))

if curve == FotiadisMartindale:
    if D == 1 or D==4:
        E = curve(code=code,u=u,a=a)
    else:
        E = curve(code=code,u=u,b=b)
elif curve == Aurifeuillean:
    if D==3:
        E = curve(k=k, u=u, D=D, e0=e0, aa=a_auri, b=b)
    elif D == 1:
        E = curve(k=k, u=u, D=D, e0=e0, aa=a_auri, a=a)
    else:
        E = curve(k=k, u=u, D=D, e0=e0, aa=a_auri, a=a, b=b)
elif curve == Cyclotomic:
    if D == 3:
        E = curve(k=k, u=u, D=D, l=l, e0=e0, b=b)
    elif D == 1 or D == 4:
        E = curve(k=k, u=u, D=D, l=l, e0=exp_tr, a=a)
    else:
        E = curve(k=k, u=u, D=D, l=l, e0=e0, a=a, b=b)
elif curve == KSS:
    if D == 3:
        E = curve(k=k, u=u, b=b, choice_kss=choice_kss)
    elif D == 1 or D == 4:
        E = curve(k=k, u=u, a=a, choice_kss=choice_kss)
    else:
        E = curve(k=k, u=u, a=a, b=b, choice_kss=choice_kss, D=D)
elif D==1 or D==4:
    E = curve(k=k, u=u, a=a, cofactor_r=cofact_r)
elif D==3:
    E = curve(k=k, u=u, b=b, cofactor_r=cofact_r)
else:
    E = curve(k=k, D=D, u=u, a=a,b=b, cofactor_r=cofact_r)
E.print_parameters()
print("")

ZZy.<y> = PolynomialRing(ZZ)
Rxy.<x> = PolynomialRing(ZZy)

poly_p = ZZy(px_denom*px)
poly_u = [-u, 1]

poly_p_sq = poly_p
u_sq = u
poly_u = [-u_sq, 1]

if curve == FotiadisMartindale and code == 17:
    poly_p_sq = ZZy(108*poly_p_sq((y-2)/6))
    u_sq = 6*u_sq + 2
    assert ZZ(poly_p_sq(u_sq)) == 108*E.p()
    poly_u = [-u_sq, 1]
elif curve == KSS and k==16:
    poly_p_sq = ZZy(poly_p_sq(y-1))
    u_sq = u_sq+1
    assert ZZ(poly_p_sq(u_sq)) == 980*E.p()
    poly_u = [-u_sq, 1]
elif curve == BN:
    # to get a monic poly_p_sq = x^4 - 2*x^3 + 12*x^2 - 20*x + 28
    # poly_p_sq = ZZy(36*poly_p_sq((y-1)/3))
    # u_sq = 6*u_sq + 2
    # assert ZZ(poly_p_sq(u_sq)) == 36*E.p()
    # poly_u = [-u_sq, 1]
    # to minimise the coefficients, poly_p_sq = 4*x^4 - 4*x^3 + 12*x^2 - 10*x + 7
    poly_p_sq = ZZy(9*poly_p_sq((y-1)/3))
    u_sq = 3*u_sq + 1
    assert ZZ(poly_p_sq(u_sq)) == 9*E.p()
    poly_u = [-u_sq, 1]

#if Special:
if lower_degree_px:
    print("Special TNFS available")
    Kp.<v> = NumberField(poly_p)
    #print("the subfields of p(x) are:")
    #print(Kp.subfields())
    if k != 31:
        print("the automorphisms of p(x) are:")
        print(Kp.automorphisms())

    # u is already known thanks to the test vector data
    # if poly_p is even, then take P(X) where P(x^2) = p(x)
    if is_even(poly_p.list()):
        print("px even")
        poly_p_sq = ZZy([poly_p.list()[i] for i in range(0, poly_p.degree()+1,2)])
        u_sq = u**2
        poly_u = [-u_sq, 1]
        print("poly_p = {} where y = x^2".format(poly_p_sq))
    # if poly_p is palindrome, takes minimal_polynomial(a+1/a) in K = NumberField(poly_p)
    elif is_palindrome(poly_p.list()):
        print("px palindrome, computes minimal_polynomial(a+1/a) in QQ[a]/(px(a))")
        mx = minimal_polynomial(Kp.0+1/Kp.0)
        mx_denom = lcm([mi.denom() for mi in mx.list()])
        poly_p_sq = ZZy(mx_denom*mx)
        #u_sq = u+1/u # x - (u+1/u) <=>  u*x - (u**2+1)
        # (u+1/u) is root of mx
        u_sq = u+1/u
        poly_u = [-(u**2+1), u]
        mc = mx.list()
        print("mx = {}".format(mx))
        print("mc = {}".format(mc))
    elif is_antipalindrome(poly_p.list()):
        print("px anti-palindrome, computes minimal_polynomial(a-1/a) in QQ[a]/(px(a))")
        mx = minimal_polynomial(Kp.0-1/Kp.0)
        mx_denom = lcm([mi.denom() for mi in mx.list()])
        poly_p_sq = ZZy(mx_denom*mx)
        #u_sq = u-1/u # x - (u-1/u) <=>  u*x - (u**2-1)
        # (u-1/u) is root of mx
        u_sq = u-1/u
        poly_u = [-(u**2-1), u]
        mc = mx.list()
        print("mx = {}".format(mx))
        print("mc = {}".format(mc))
    else:
        print("no easy automorphism, write P(u**{}) = p(u) and P has coefficients linear in |u|".format(deg_px_dec))
        # there is no automorphism
        mc = poly_p.list()
        #if len(mc) % deg_px_dec == 0:
        mx = [ sum([u^i * mc[i+j] for i in range(0, min(deg_px_dec, len(mc)-j))]) for j in range(0,len(mc),deg_px_dec)]
        #else:
        #    mx = [mc[i] + u*mc[i+1] for i in range(0,len(mc)-1,2)]
        #    mx.append(mc[-1])
        poly_p_sq = ZZy(mx)
        u_sq = u**deg_px_dec
        poly_u = [-u_sq, 1]

cont = poly_p_sq.content()
print("content of poly_p_sq is {}".format(cont))
poly_p_sq //= cont
print("poly_p_sq = {}".format(poly_p_sq))
print("u_sq = {}".format(u_sq))

k = E.k()
p = E.p()
ell = E.r()
cofactor = E.c()
tr = E.tr()
Fp = E.Fp()
Fpz,z = E.Fpz()

assert (ZZ(poly_p_sq.resultant(ZZy(poly_u))) % p  == 0), "error Resultant(poly_p_sq, poly_u) != 0 mod p"
ps = Polyselect(E)

if deg_h > 1:
    ps.compute_h(deg_h)
    E_list_h = ps.get_h()
    print("polynomials h")
    ps.print_h(deg_h=deg_h)

    deg_g=(k//deg_h)
    for tup_h in E_list_h[deg_h]:
        if len(tup_h) == 4:
            inv_zeta_Kh, w, aut_h, h = tup_h
        else:
            inv_zeta_Kh, w, h = tup_h
            aut_h = None
        inv_zeta_Kh = float(inv_zeta_Kh)
        w = int(w // 2) # divide by 2  because up to multiplication by {+-1}
    
        if type(h) != list:
            h_coeffs = h.list()
        else:
            h_coeffs = h
        if aut_h is None:
            aut_h = automorphism_factor(h_coeffs)
        h = ZZy(h)
        if (gcd(deg_g,deg_h) != 1) and aut_h != 1:
            # can we use the automorphism of h to speed-up the relation collection?
            # example: deg(h) = 6, h = cyclotomic_polynomial(7), sigma: y -> y^2 has order 3, to obtain f, g fixed by sigma,
            # the coefficient in y should be trace(sigma) = y+u^2+y^4
            if deg_h >= 4 and h.is_cyclotomic():
                if deg_h == 4 and h==cyclotomic_polynomial(5)(y): #y^4+y^3+y^2+y+1
                    sigma_y = -y^3 - y^2 - y - 1 # this is y^4 = y^5/y = 1/y
                    tr_sigma_y = -y^3 - y^2 - 1  # this is y + 1/y = (y^2+1)/y
                    tr_sigma_y_frac = (y^2+1, y)  # numerator, denominator
                    aut_h = 2
                elif deg_h == 4 and h==cyclotomic_polynomial(10)(y):#h==y^4-y^3+y^2-y+1
                    sigma_y = -y^3 + y^2 - y + 1 # this is -y^4 = -y^5/y = 1/y
                    tr_sigma_y = -y^3 + y^2 + 1  # this is y + 1/y = (y^2+1)/y
                    tr_sigma_y_frac = (y^2+1, y)
                    aut_h = 2
                elif deg_h == 6 and h==cyclotomic_polynomial(7)(y):#y^6+y^5+y^4+y^3+y^2+y+1
                    sigma_y = y^2 # it works with y^4 with the same trace
                    tr_sigma_y = y^4 + y^2 + y
                    tr_sigma_y_frac = (y^3 - y - 1, y^2 + y)
                    # the other fraction is (-2*y^2 - 2*y)/(y^3 + y^2 - 1)
                    aut_h = 3
                elif deg_h == 6 and h==cyclotomic_polynomial(14)(y):#y^6-y^5+y^4-y^3+y^2-y+1
                    sigma_y = -y^2 # it works with -y^4 with the same trace
                    tr_sigma_y = -y^4 - y^2 + y
                    tr_sigma_y_frac = (y^3 - y + 1, y^2 - y)
                    # the other fraction is (-2*y^2 + 2*y)/(y^3 - y^2 + 1)
                    aut_h = 3
                elif deg_h == 10 and h==cyclotomic_polynomial(11)(y):
                    sigma_y = y^3 # it works the same with y^4, y^5, y^9
                    tr_sigma_y = y^9 + y^5 + y^4 + y^3 + y
                    aut_h = 5
                elif deg_h == 10 and h==cyclotomic_polynomial(22)(y):
                    sigma_y = y^3 # it works the same with -y^4, y^5, y^9
                    tr_sigma_y = y^9 + y^5 - y^4 + y^3 + y
                    aut_h = 5
            elif is_palindrome(h_coeffs):
                # sigma: y -> 1/y, trace(sigma) = y + 1/y = (y^2+1)/y
                sigma_y = ((h-h.constant_coefficient())//y)/(-h.constant_coefficient())
                tr_sigma_y = y + sigma_y
                tr_sigma_y_frac = (y^2+1, y)
                aut_h = 2
            elif is_antipalindrome(h_coeffs):
                # sigma: y -> -1/y, trace(sigma) = y - 1/y = (y^2-1)/y
                sigma_y = ((h-h.constant_coefficient())//y)/(h.constant_coefficient())
                tr_sigma_y = y + sigma_y
                tr_sigma_y_frac = (y^2-1, y)
                aut_h = 2
            elif is_even(h_coeffs):
                # does not work
                aut_h = 1
                sigma_y = None # -y
                tr_sigma_y = None # 0 = y - y does not work...
                tr_sigma_y_frac = None # (0, 1) does not work
        else:
            aut_h = 1
            sigma_y = None
            tr_sigma_y = None
            tr_sigma_y_frac = None
        if aut_h > 1:
            print("h = {} has order-{} automorphism y -> {} of trace {} = ({})/({})".format(h, aut_h, sigma_y, tr_sigma_y, tr_sigma_y_frac[0], tr_sigma_y_frac[1]))
        if Special:
            res = ps.Resultant(deg_g, poly_p_sq, poly_u, h=h, with_y=(gcd(deg_g,deg_h) > 1), coeff_y=tr_sigma_y_frac)
        elif Conj:
            res = ps.TNFS_Conjugation(deg_g=deg_g,h=h,with_y=(gcd(deg_g,deg_h) > 1),max_coeff=2, compute_alpha=compute_alpha)
        elif JL:
            res = ps.TNFS_GJL(deg_phi=k//deg_h, deg_f=deg_f_JL, h=h, max_coeff=1)
        elif SSingh:
            res = ps.TNFS_SarkarSingh_JL(deg_aux1=deg_aux1, deg_g=deg_g, h=h, with_y=(gcd(deg_g,deg_h) > 1), max_coeff=max_coeff_aux1)
        elif Base_m:
            f0c, f1c = ps.Base_m(deg_f=deg_f_Base_m)
            f=ZZy(f0c)(x)
            g=ZZy(f1c)(x)
            max_fi = max([abs(fic) for fic in f0c])
            max_gi = max([abs(gic) for gic in f1c])
            aut_fg = 1
            res = (f,g,max_fi,max_gi,aut_fg)

        if res == None:
            print("h = {}, TNFS_special returned nothing".format(h))
            continue
        f, g, max_fi, max_gi, aut_fg = res[:5]
        Kh.<ah> = NumberField(h)
        #Oh = Kh.maximal_order()
        if compute_alpha and deg_h <= 24:
            clKh = Kh.class_number()
        else:
            clKh = None
        print("inv_zeta_Kh, w = {:.6f},{:2d}".format(inv_zeta_Kh, w))
        print("h = {} # {} class number Kh = {}".format(h, h.list(), clKh))
        if not compute_alpha:
            if barbulescu_duquesne:
                alpha_f = float(0.0)
                alpha_g = float(0.0)
            else:
                alpha_f = float(2.0)
                alpha_g = float(2.0)
        elif clKh == 1:
            alpha_f = float(alpha_TNFS_2d(f,h,1000,test_principal=True))
            alpha_g = float(alpha_TNFS_2d(g,h,1000,test_principal=True))
        else:
            alpha_f = float(alpha_TNFS_2d(f,h,1000,test_principal=False))
            alpha_g = float(alpha_TNFS_2d(g,h,1000,test_principal=False))
        sum_alpha = alpha_f+alpha_g
        # automorphisms sigma of h are compatible with f, g only if sigma(f), sigma(g) are invariant.
        # this is the case if f, g are univariate in x (no dependency in y where h = h(y))
        # or, if f, resp. g have coeffs with y but invariant by sigma, this is the case e.g. for trace(y) = y+sigma(y) + ... + sigma^i(y) where i = order(y)-1.
        aut = aut_h*aut_fg
        # TODO, are we sure it is aut_h*aut_fg?
        print("f = {}".format(f))
        print("g = {}".format(g))
        print("max_fi = {:6d}, log_2 max_gi = {:6.2f}".format(max_fi, float(log(max_gi,2))))
        print("aut = {}".format(aut))
        print("alpha_f = {:.4f} alpha_g = {:.4f}".format(alpha_f,alpha_g))
        print("    ({:.8f},{:2d}, {:40s}, {:.4f}, {:.4f}, {:.4f}),".format(float(inv_zeta_Kh),int(w),str(h),float(alpha_f),float(alpha_g),float(sum_alpha)))
        if barbulescu_duquesne:
            print("barbulescu_duquesne")
            count_sieving = False
            weight_per_row = 128
            cst_filtering=1.0
            label="model of cost BD19"
        else:
            count_sieving = True
            weight_per_row = 200
            cst_filtering=20
            label="model of cost GS21"
        simul = Simulation_TNFS(p,ell,Fp,Fpz,h,f,g,Rxy,cost,aut,inv_zeta_Kh,w,None,None,alpha_f,alpha_g,weight_per_row,cst_filtering,count_sieving,label,barbulescu_duquesne)
        simul.print_params()
        simul.simulation(samples=samples)
        simul.print_results()
        print(":::::::::::::::")
        simul.adjust_cost(samples=samples)
        print("###############")
else:
    print("deg_h = 1, NFS, no tower")
    if sieving_dim is None:
        print("sieving_dim not initialized, set to 2")
        sieving_dim = 2
    deg_g = k
    Rx.<x> = ZZ[]
    if Conj:
        deg_f = 2*k
        deg_g = k
        res = ps.NFS_Conjugation(deg_g=deg_g,sieving_dim=sieving_dim,max_coeff=2, compute_alpha=True,verbose=False)
        f, g, aux0, aux1, max_fi, max_gi, aut_g, alpha_f, alpha_g, sum_alpha, score = res[0]
    elif JLSV1:
        deg_f = k
        deg_g = k
        res = ps.NFS_JLSV1(deg_g=deg_g,sieving_dim=sieving_dim,compute_alpha=True,verbose=True)
    if res is None:
        print("Error polyselect returned nothing")
    else:
        if Conj:
            f, g, aux0, aux1, max_fi, max_gi, aut_g, alpha_f, alpha_g, sum_alpha, score = res[0]
            aut = aut_g
        elif JLSV1:
            f, g, max_fi, max_gi, aut_fg = res[:5]
            alpha_f = float(alpha2d(f,2000))
            alpha_g = float(alpha2d(g,2000))
            sum_alpha = alpha_f+alpha_g
            aut = aut_fg
        print("f = {}".format(f))
        print("g = {}".format(g))
        if max_fi >= 10^5:
            print("log_2 max_fi = {:6.2f}, log_2 max_gi = {:6.2f}".format(float(log(max_fi,2.0)), float(log(max_gi,2.0))))
        else:
            print("max_fi = {:6d}, log_2 max_gi = {:6.2f}".format(max_fi, float(log(max_gi,2.0))))
        print("aut = {}".format(aut))
        print("alpha_f = {:.4f} alpha_g = {:.4f}".format(alpha_f,alpha_g))

        simul = Simulation_NFS(p,ell,Fp,Fpz,sieving_dim,f,g,Rx,cost,aut,alpha_f=alpha_f, alpha_g=alpha_g,count_sieving=True)
        simul.print_params()
        simul.simulation(samples=samples)
        simul.print_results()
        print(":::::::::::::::")
        simul.adjust_cost(samples=samples)
        print("###############")
        
        
