test_vector_sparse_fm12_17 = [ # family 17 in eprint 2019/555
    {'u': 0x41fffff800800000, 'b':-2, 'pnbits':384, 'rnbits':254, 'deg_h_S':6,'cost_S':129, 'label':"+2^62+2^57-2^35+2^23 Hw2naf 4"},
    {'u': 0x420001fffffffff8, 'b':-2, 'pnbits':384, 'rnbits':254, 'deg_h_S':6,'cost_S':129, 'label':"+2^62+2^57+2^41-2^3 Hw2naf 4"},
    {'u':-0x41ffe10000000000, 'b':-2, 'pnbits':384, 'rnbits':254, 'deg_h_S':6,'cost_S':129, 'label':"-2^62-2^57+2^45-2^40 Hw2naf 4"},
    {'u':-0x4400000000003e00, 'b':-2, 'pnbits':384, 'rnbits':254, 'deg_h_S':6,'cost_S':129, 'label':"-2^62-2^58-2^14+2^9 Hw2naf 4"},
    {'u': 0x43fffffff7fe0000, 'b':-2, 'pnbits':384, 'rnbits':254, 'deg_h_S':6,'cost_S':129, 'label':"+2^62+2^58-2^27-2^17 Hw2naf 4"},
    {'u':-0x43ffbfffffffe000, 'b':-2, 'pnbits':384, 'rnbits':254, 'deg_h_S':6,'cost_S':129, 'label':"-2^62-2^58+2^46+2^13 Hw2naf 4"},
    {'u':-0x47ffffffe0000002, 'b': 2, 'pnbits':384, 'rnbits':254, 'deg_h_S':6,'cost_S':129, 'label':"-2^62-2^59+2^29-2 Hw2naf 4"},
]

# FM12 curves with sparse seed u = [1] mod 2 of 32--33 bits Hw2naf 5
test_vector_sparse_fm12_18 = [
    {'u': 0x87e00001, 'u_mod_6':3, 'a':-30, 'b':56, 'pnbits':433, 'rnbits':249, 'cost_S':133, 'deg_h_S':12, 'label':"2^31+2^27-2^21+1 Hw2naf 4"},
    {'u':0x100024001, 'u_mod_6':5, 'a':-30, 'b':56, 'pnbits':446, 'rnbits':257, 'cost_S':134, 'deg_h_S':12, 'label':"2^32+2^17+2^14+1 Hw2naf 4, u=4295114753 for Family 8 p.27 in ePrint 2018/969, Fotiadis-Martindale"},
    {'u':0x10087ffff, 'u_mod_6':1, 'a':-30, 'b':56, 'pnbits':446, 'rnbits':257, 'cost_S':134, 'deg_h_S':12, 'label':"2^32+2^23+2^19-1 Hw2naf 4"},
    {'u':0x104000011, 'u_mod_6':1, 'a':-30, 'b':56, 'pnbits':446, 'rnbits':257, 'cost_S':134, 'deg_h_S':12, 'label':"2^32+2^26+2^4+1 Hw2naf 4"},
    # Hamming weight 5, r of 256 bits.
    {'u': 0xfffff817, 'u_mod_6':1, 'a':-30, 'b':56, 'pnbits':445, 'rnbits':256, 'cost_S':134, 'deg_h_S':12, 'label':"+2^32-2^11+2^5-2^3-1 Hw2naf 5"},
    {'u': 0xc07ffeff, 'u_mod_6':3, 'a':-30, 'b':56, 'pnbits':440, 'rnbits':253, 'cost_S':134, 'deg_h_S':12, 'label':"+2^32-2^30+2^23-2^8-1 Hw2naf 5"},
    # Hamming weight 5, r of 256 bits.
    {'u': 0x80060041, 'u_mod_6':1, 'a':-30, 'b':56, 'pnbits':432, 'rnbits':249, 'cost_S':133, 'deg_h_S':12, 'label':"+2^31+2^18+2^17+2^6+1 Hw2naf 5"},
    {'u': 0x88400401, 'u_mod_6':1, 'a':-30, 'b':56, 'pnbits':433, 'rnbits':249, 'cost_S':133, 'deg_h_S':12, 'label':"+2^31+2^27+2^22+2^10+1 Hw2naf 5"},
]
test_vector_sparse_fst67_k12 = test_vector_sparse_fm12_18

# FM15 curves with sparse seed u = [0] mod 3 of 49--49 bits Hw2naf 5 and s.t. r has 384 to 384 bits
test_vector_sparse_fm15_21 = [
    {'u':-0xffffff020001, 'u_mod_5':2, 'b':-3, 'pnbits':768, 'rnbits':384, 'cost_S':194, 'deg_h_S':15, 'cost_C':201, 'deg_h_C':3, 'label':"-2^48+2^24-2^17-1 Hw2naf 4"},
]
# FM15 curves with sparse seed u = [0] mod 3 of 48--49 bits Hw2naf 5 and s.t. r has 380 to 384 bits
# x -> x/3 w.r.t. eprint 2019/555
test_vector_sparse_fm15_22 = [
    {'u': 0xa7fc00010000, 'u_mod_5':0, 'b': 1, 'pnbits':759, 'rnbits':380, 'cost_S':191, 'deg_h_S':15, 'cost_C':200, 'deg_h_C':3, 'label':"+2^47+2^45+2^43-2^34+2^16 Hw2naf 5"},
    {'u':-0xfffffe01fc00, 'u_mod_5':3, 'b': 1, 'pnbits':768, 'rnbits':384, 'cost_S':193, 'deg_h_S':15, 'cost_C':200, 'deg_h_C':3, 'label':"-2^48+2^25-2^17+2^10 Hw2naf 4"},
    {'u':-0xfffff3c00000, 'u_mod_5':0, 'b': 1, 'pnbits':768, 'rnbits':384, 'cost_S':193, 'deg_h_S':15, 'cost_C':200, 'deg_h_C':3, 'label':"-2^48+2^28-2^26+2^22 Hw2naf 4"},
    {'u': 0xff0100020000, 'u_mod_5':3, 'b': 1, 'pnbits':768, 'rnbits':384, 'cost_S':193, 'deg_h_S':15, 'cost_C':200, 'deg_h_C':3, 'label':"+2^48-2^40+2^32+2^17 Hw2naf 4"},
    {'u': 0xfe0000001f00, 'u_mod_5':0, 'b': 1, 'pnbits':768, 'rnbits':384, 'cost_S':193, 'deg_h_S':15, 'cost_C':200, 'deg_h_C':3, 'label':"+2^48-2^41+2^13-2^8 Hw2naf 4"},
    # there are other seeds of HW 5
    # seeds in non-signed representation to avoid non-free inversions/conjugations and p = 1 mod 5
    # u = 0, 3 mod 5 to ensure p = 1 mod 5
    {'u': 0xa80000a00200, 'u_mod_5':0, 'b': 1, 'pnbits':759, 'rnbits':380, 'cost_S':191, 'deg_h_S':15, 'cost_C':200, 'deg_h_C':3, 'label':"+2^47+2^45+2^43+2^23+2^21+2^9 Hw 6"},
    {'u': 0xc00400006800, 'u_mod_5':0, 'b': 1, 'pnbits':762, 'rnbits':381, 'cost_S':191, 'deg_h_S':15, 'cost_C':200, 'deg_h_C':3, 'label':"+2^47+2^46+2^34+2^14+2^13+2^11 Hw 6"},
]

test_vector_sparse_fm16_23 = [ # family 23 in eprint 2019/555
    {'u':0x1000014000000, 'a': 1, 'pnbits':767, 'rnbits':385, 'deg_h_S':16,'cost_S':196, 'deg_h_C':4,'cost_C':209, 'label':"+2^48+2^28+2^26 Hw2naf 3"},
    {'u':-0xfffffffd7ff8, 'a': 1, 'pnbits':766, 'rnbits':384, 'deg_h_S':16,'cost_S':196, 'deg_h_C':4,'cost_C':209, 'label':"-2^48+2^17+2^15+2^3 Hw2naf 4"},
    {'u':-0xffffffc00300, 'a': 1, 'pnbits':766, 'rnbits':384, 'deg_h_S':16,'cost_S':196, 'deg_h_C':4,'cost_C':209, 'label':"-2^48+2^22-2^10+2^8 Hw2naf 4"},
    {'u': 0xfffbdfff0000, 'a': 1, 'pnbits':766, 'rnbits':384, 'deg_h_S':16,'cost_S':196, 'deg_h_C':4,'cost_C':209, 'label':"+2^48-2^34-2^29-2^16 Hw2naf 4"},
    {'u': 0xfff000000140, 'a': 1, 'pnbits':766, 'rnbits':384, 'deg_h_S':16,'cost_S':196, 'deg_h_C':4,'cost_C':209, 'label':"+2^48-2^36+2^8+2^6 Hw2naf 4"},
    {'u':-0xffbffffc1000, 'a': 1, 'pnbits':766, 'rnbits':384, 'deg_h_S':16,'cost_S':196, 'deg_h_C':4,'cost_C':209, 'label':"-2^48+2^38+2^18-2^12 Hw2naf 4"},
    {'u':-0xff7fffff0800, 'a': 1, 'pnbits':766, 'rnbits':384, 'deg_h_S':16,'cost_S':196, 'deg_h_C':4,'cost_C':209, 'label':"-2^48+2^39+2^16-2^11 Hw2naf 4"},
    {'u':-0xfedc00000000, 'a': 1, 'pnbits':766, 'rnbits':384, 'deg_h_S':16,'cost_S':196, 'deg_h_C':4,'cost_C':209, 'label':"-2^48+2^40+2^37+2^34 Hw2naf 4"},
    {'u': 0xfc003fff0000, 'a': 1, 'pnbits':766, 'rnbits':384, 'deg_h_S':16,'cost_S':196, 'deg_h_C':4,'cost_C':209, 'label':"+2^48-2^42+2^30-2^16 Hw2naf 4"},
    {'u':-0xf80000400040, 'a': 1, 'pnbits':766, 'rnbits':384, 'deg_h_S':16,'cost_S':196, 'deg_h_C':4,'cost_C':209, 'label':"-2^48+2^43-2^22-2^6 Hw2naf 4"},
    {'u': 0xf60000010000, 'a': 1, 'pnbits':766, 'rnbits':384, 'deg_h_S':16,'cost_S':196, 'deg_h_C':4,'cost_C':209, 'label':"+2^48-2^43-2^41+2^16 Hw2naf 4"},
    {'u': 0xefc080000000, 'a': 1, 'pnbits':765, 'rnbits':384, 'deg_h_S':16,'cost_S':196, 'deg_h_C':4,'cost_C':209, 'cost_SS':227, 'deg_h_SS':4, 'deg_aux_SS':3, 'label':"+2^48-2^44-2^38+2^31 Hw2naf 4"},
    {'u':-0xc00000010200, 'a': 1, 'pnbits':760, 'rnbits':381, 'deg_h_S':16,'cost_S':196, 'deg_h_C':4,'cost_C':209, 'label':"-2^48+2^46-2^16-2^9 Hw2naf 4"},
    {'u':-0xa7ffffc04000, 'a': 1, 'pnbits':757, 'rnbits':380, 'cost_S':None, 'deg_h_S':None, 'cost_C':None, 'deg_h_C':None, 'label':"-2^47-2^45-2^43+2^22-2^14 Hw2naf 5"},
]
# FM16 curves with sparse seed u = [0] mod 1 of 49--49 bits Hw2naf 5 and s.t. r has 384 to 384 bits
test_vector_sparse_fm16_28 = [ # a new family, let's label it 28
    # seeds for the 128-bit security level:
    {'u': 0xffffc300, 'u_mod_4':0, 'a': 1, 'pnbits':510, 'rnbits':256, 'cost_S':None, 'deg_h_S':None, 'cost_C':None, 'deg_h_C':None, 'label':"+2^32-2^14+2^10-2^8 Hw2naf 4"},
    {'u': 0xfff80700, 'u_mod_4':0, 'a': 1, 'pnbits':510, 'rnbits':256, 'cost_S':None, 'deg_h_S':None, 'cost_C':None, 'deg_h_C':None, 'label':"+2^32-2^19+2^11-2^8 Hw2naf 4"},
    {'u':-0xfdfe0100, 'u_mod_4':0, 'a': 1, 'pnbits':510, 'rnbits':256, 'cost_S':None, 'deg_h_S':None, 'cost_C':None, 'deg_h_C':None, 'label':"-2^32+2^25+2^17-2^8 Hw2naf 4"},
    {'u': 0xfc000420, 'u_mod_4':0, 'a': 1, 'pnbits':510, 'rnbits':256, 'cost_S':None, 'deg_h_S':None, 'cost_C':None, 'deg_h_C':None, 'label':"+2^32-2^26+2^10+2^5 Hw2naf 4"},
    {'u':-0xee000400, 'u_mod_4':0, 'a': 1, 'pnbits':509, 'rnbits':256, 'cost_S':None, 'deg_h_S':None, 'cost_C':None, 'deg_h_C':None, 'label':"-2^32+2^28+2^25-2^10 Hw2naf 4"},
    # seeds for the 192-bit security level:
    {'u':-0xbefffff80000, 'a': 1, 'pnbits':760, 'rnbits':381, 'deg_h_S':16,'cost_S':196, 'deg_h_C':4,'cost_C':209, 'label':"-2^48+2^46+2^40+2^19 Hw2naf 4"},
    {'u':-0xe0000ffffe00, 'a': 1, 'pnbits':763, 'rnbits':383, 'deg_h_S':16,'cost_S':196, 'deg_h_C':4,'cost_C':209, 'label':"-2^48+2^45-2^28+2^9 Hw2naf 4"},
    {'u': 0xdffc80000000, 'a': 1, 'pnbits':763, 'rnbits':383, 'deg_h_S':16,'cost_S':196, 'deg_h_C':4,'cost_C':209, 'label':"+2^48-2^45-2^34+2^31 Hw2naf 4"},
    {'u':-0xf02000000000, 'a': 1, 'pnbits':765, 'rnbits':384, 'deg_h_S':16,'cost_S':196, 'deg_h_C':4,'cost_C':209, 'label':"-2^48+2^44-2^37 Hw2naf 3"},
    {'u': 0xfffffff08020, 'a': 1, 'pnbits':766, 'rnbits':384, 'deg_h_S':16,'cost_S':196, 'deg_h_C':4,'cost_C':209, 'label':"+2^48-2^20+2^15+2^5 Hw2naf 4"},
    {'u': 0xffffffb04000, 'a': 1, 'pnbits':766, 'rnbits':384, 'deg_h_S':16,'cost_S':196, 'deg_h_C':4,'cost_C':209, 'label':"+2^48-2^22-2^20+2^14 Hw2naf 4"},
    {'u':-0xfffff7000004, 'a': 1, 'pnbits':766, 'rnbits':384, 'deg_h_S':16,'cost_S':196, 'deg_h_C':4,'cost_C':209, 'label':"-2^48+2^27+2^24-2^2 Hw2naf 4"},
    {'u': 0xffffee000004, 'a': 1, 'pnbits':766, 'rnbits':384, 'deg_h_S':16,'cost_S':196, 'deg_h_C':4,'cost_C':209, 'label':"+2^48-2^28-2^25+2^2 Hw2naf 4"},
    {'u':-0xffffdfc00800, 'a': 1, 'pnbits':766, 'rnbits':384, 'deg_h_S':16,'cost_S':196, 'deg_h_C':4,'cost_C':209, 'label':"-2^48+2^29+2^22-2^11 Hw2naf 4"},
    {'u':-0xffdffc000010, 'a': 1, 'pnbits':766, 'rnbits':384, 'deg_h_S':16,'cost_S':196, 'deg_h_C':4,'cost_C':209, 'label':"-2^48+2^37+2^26-2^4 Hw2naf 4"},
    {'u':-0xfdfffefff000, 'a': 1, 'pnbits':766, 'rnbits':384, 'deg_h_S':16,'cost_S':196, 'deg_h_C':4,'cost_C':209, 'label':"-2^48+2^41+2^24+2^12 Hw2naf 4"},
    {'u':-0xfc0200020000, 'a': 1, 'pnbits':766, 'rnbits':384, 'deg_h_S':16,'cost_S':196, 'deg_h_C':4,'cost_C':209, 'label':"-2^48+2^42-2^33-2^17 Hw2naf 4"},
    {'u':-0xf803ffffc000, 'a': 1, 'pnbits':766, 'rnbits':384, 'deg_h_S':16,'cost_S':196, 'deg_h_C':4,'cost_C':209, 'label':"-2^48+2^43-2^34+2^14 Hw2naf 4"},
]
# Auri18 curves with sparse seed u = [0] mod 1 of 43--43 bits Hw2naf 6 and s.t. r has 256 to 256 bits
test_vector_sparse_auri18_D3_a3_e01 = [
    {'u': 0x3801ffffff0, 'b':11, 'pnbits':427, 'rnbits':256, 'cost_S':158, 'deg_h_S':18, 'cost_C':179, 'deg_h_C':3, 'label':"+2^42-2^39+2^29-2^4 Hw2naf 4"},
    {'u':-0x377c0000000, 'b':31, 'pnbits':426, 'rnbits':256, 'cost_S':158, 'deg_h_S':18, 'cost_C':179, 'deg_h_C':3, 'label':"-2^42+2^39+2^35+2^30 Hw2naf 4"},
    {'u':-0x3a000400000, 'b':17, 'pnbits':427, 'rnbits':256, 'cost_S':158, 'deg_h_S':18, 'cost_C':179, 'deg_h_C':3, 'label':"-2^42+2^39-2^37-2^22 Hw2naf 4"},
    # Auri18 curves with sparse seed u = [0] mod 1 of 64--64 bits Hw2naf 3 and s.t. r has 383 to 384 bits
    {'u': 0x80003ffffffffe00, 'b':19, 'pnbits':638, 'rnbits':383, 'cost_S':187, 'deg_h_S':18, 'cost_C':206, 'deg_h_C':3, 'label':"+2^63+2^46-2^9 Hw2naf 3"},
    {'u':-0x8040000000010000, 'b':15, 'pnbits':638, 'rnbits':383, 'cost_S':187, 'deg_h_S':18, 'cost_C':206, 'deg_h_C':3, 'label':"-2^63-2^54-2^16 Hw2naf 3"},
    {'u': 0x87fffff000000800, 'b':13, 'pnbits':639, 'rnbits':384, 'cost_S':187, 'deg_h_S':18, 'cost_C':206, 'deg_h_C':3, 'label':"+2^63+2^59-2^36+2^11 Hw2naf 4"},
    {'u': 0x87fff7f800000000, 'b':47, 'pnbits':639, 'rnbits':384, 'cost_S':187, 'deg_h_S':18, 'cost_C':206, 'deg_h_C':3, 'label':"+2^63+2^59-2^43-2^35 Hw2naf 4"},
    {'u': 0x9000000002008000, 'b':17, 'pnbits':640, 'rnbits':384, 'cost_S':187, 'deg_h_S':18, 'cost_C':206, 'deg_h_C':3, 'label':"+2^63+2^60+2^25+2^15 Hw2naf 4"},
    {'u':-0x8ff7ffffc0000000, 'b':19, 'pnbits':640, 'rnbits':384, 'cost_S':187, 'deg_h_S':18, 'cost_C':206, 'deg_h_C':3, 'label':"-2^63-2^60+2^51+2^30 Hw2naf 4"},
    #
    {'u': 0x3ffff800100000000, 'u_mod_3':0, 'b':13, 'pnbits':668, 'rnbits':401, 'cost_S':191, 'deg_h_S':18, 'cost_C':213, 'deg_h_C':3, 'label':"+2^66-2^47+2^32 Hw2naf 3"},
    {'u':-0x4000fffffffffffe0, 'u_mod_3':0, 'b':23, 'pnbits':668, 'rnbits':401, 'cost_S':191, 'deg_h_S':18, 'cost_C':213, 'deg_h_C':3, 'label':"-2^66-2^52+2^5 Hw2naf 3"},
    {'u':-0x408007fffffffe000, 'u_mod_3':0, 'b':17, 'pnbits':669, 'rnbits':401, 'cost_S':191, 'deg_h_S':18, 'cost_C':213, 'deg_h_C':3, 'label':"-2^66-2^59-2^47+2^13 Hw2naf 4"},
    {'u': 0x41000080000000008, 'u_mod_3':0, 'b':17, 'pnbits':669, 'rnbits':401, 'cost_S':191, 'deg_h_S':18, 'cost_C':213, 'deg_h_C':3, 'label':"+2^66+2^60+2^43+2^3 Hw2naf 4"},
    #
    {'u':-0x280000000000004400, 'u_mod_3':0, 'b':11, 'pnbits':702, 'rnbits':421, 'cost_S':194, 'deg_h_S':18, 'cost_C':215, 'deg_h_C':3, 'label':"-2^69-2^67-2^14-2^10 Hw2naf 4"},
    {'u': 0x27f800000040000000, 'u_mod_3':0, 'b':13, 'pnbits':702, 'rnbits':421, 'cost_S':194, 'deg_h_S':18, 'cost_C':215, 'deg_h_C':3, 'label':"+2^69+2^67-2^59+2^30 Hw2naf 4"},
    {'u': 0x2fffc0000010000000, 'u_mod_3':0, 'b':23, 'pnbits':704, 'rnbits':423, 'cost_S':194, 'deg_h_S':18, 'cost_C':216, 'deg_h_C':3, 'label':"+2^70-2^68-2^54+2^28 Hw2naf 4"},
]

test_vector_sparse_fm18_25 = [ # family 25 in eprint 2019/555 TODO
    {'u': 0xfffffffffffbc401, 'b': 7, 'pnbits':768, 'rnbits':384, 'deg_h_S':18,'cost_S':197, 'deg_h_C':3,'cost_C':221, 'label':"+2^64-2^18-2^14+2^10+1 Hw2naf 5"},
    {'u': 0xffffffffbfbfffe1, 'b':14, 'pnbits':768, 'rnbits':384, 'deg_h_S':18,'cost_S':197, 'deg_h_C':3,'cost_C':221, 'label':"+2^64-2^30-2^22-2^5+1 Hw2naf 5"},
    {'u': 0xffffffff82080001, 'b':13, 'pnbits':768, 'rnbits':384, 'deg_h_S':18,'cost_S':197, 'deg_h_C':3,'cost_C':221, 'label':"+2^64-2^31+2^25+2^19+1 Hw2naf 5"},
    {'u':-0xfffffffdfffdfff9, 'b': 5, 'pnbits':768, 'rnbits':384, 'deg_h_S':18,'cost_S':197, 'deg_h_C':3,'cost_C':221, 'label':"-2^64+2^33+2^17+2^3-1 Hw2naf 5"},
    {'u':-0xfffffffdbfefffff, 'b': 5, 'pnbits':768, 'rnbits':384, 'deg_h_S':18,'cost_S':197, 'deg_h_C':3,'cost_C':221, 'label':"-2^64+2^33+2^30+2^20+1 Hw2naf 5"},
    {'u':-0xfffffff800000051, 'b':14, 'pnbits':768, 'rnbits':384, 'deg_h_S':18,'cost_S':197, 'deg_h_C':3,'cost_C':221, 'label':"-2^64+2^35-2^6-2^4-1 Hw2naf 5"},
    {'u':-0xffffffeffffc0003, 'b':43, 'pnbits':768, 'rnbits':384, 'deg_h_S':18,'cost_S':197, 'deg_h_C':3,'cost_C':221, 'label':"-2^64+2^36+2^18-2^2+1 Hw2naf 5"},
    {'u':-0x100000007fffff801,'b':31, 'pnbits':769, 'rnbits':385, 'deg_h_S':18,'cost_S':197, 'deg_h_C':3,'cost_C':221, 'label':"-2^64-2^35+2^11-1 Hw2naf 4"},
]

# FM20 curves with sparse seed u = [1] mod 2 of 49--49 bits Hw2naf 5 and s.t. r has 384 to 384 bits
test_vector_sparse_fm20_27 = [
    {'u':-0xffffffc08001,   'a':29, 'pnbits':574, 'rnbits':384, 'deg_h_S':10,'cost_S':182, 'deg_h_C':4,'cost_C':201, 'label':"-2^48+2^22-2^15-1 Hw2naf 4"}, # with lower_degree_px trick for Special
    # larger p and r
    {'u':-0x21fffffffffbff, 'a': 1, 'pnbits':636, 'rnbits':425, 'deg_h_S':10,'cost_S':189, 'deg_h_C':4,'cost_C':209, 'label':"-2^53-2^49+2^10+1 Hw2naf 4"},
    # FM20 curves with sparse seed u = [1] mod 2 of 57--57 bits Hw2naf 5 and s.t. r has 448 to 448 bits
    {'u':-0xffefffffffffff, 'a': 1, 'pnbits':670, 'rnbits':448, 'deg_h_S':10,'cost_S':193, 'deg_h_C':4,'cost_C':214, 'label':"-2^56+2^44+1 Hw2naf 3"}, # with lower_degree_px trick for Special
    {'u': 0xfffffffe03fffd, 'a':-1, 'pnbits':670, 'rnbits':448, 'deg_h_S':10,'cost_S':193, 'deg_h_C':4,'cost_C':214, 'label':"+2^56-2^25+2^18-2^2+1 Hw2naf 5"}, # with lower_degree_px trick for Special
]
test_vector_sparse_fst64_k20 = test_vector_sparse_fm20_27

# Auri20 curves with sparse seed u = [0] mod 1 of 48--49 bits Hw2naf 4 and s.t. r has 380 to 385 bits
test_vector_sparse_auri20_D1_a2_e019 = [
    {'u': 0x7efffffffffc, 'a': 1, 'pnbits':665, 'rnbits':380, 'deg_h_S':20,'cost_S':203, 'deg_h_C':4,'cost_C':213, 'label':"+2^47-2^40-2^2 Hw2naf 3"},
    {'u':-0x7fffffdff804, 'a': 1, 'pnbits':665, 'rnbits':380, 'deg_h_S':20,'cost_S':203, 'deg_h_C':4,'cost_C':213, 'label':"-2^47+2^21+2^11-2^2 Hw2naf 4"},
    {'u':-0x8000003fffc2, 'a': 4, 'pnbits':666, 'rnbits':381, 'deg_h_S':20,'cost_S':203, 'deg_h_C':4,'cost_C':213, 'label':"-2^47-2^22+2^6-2 Hw2naf 4"},
    {'u':-0x800008002200, 'a': 1, 'pnbits':666, 'rnbits':381, 'deg_h_S':20,'cost_S':203, 'deg_h_C':4,'cost_C':213, 'label':"-2^47-2^27-2^13-2^9 Hw2naf 4"},
    {'u': 0x800040000210, 'a': 1, 'pnbits':666, 'rnbits':381, 'deg_h_S':20,'cost_S':203, 'deg_h_C':4,'cost_C':213, 'label':"+2^47+2^30+2^9+2^4 Hw2naf 4"},
    {'u':-0x7fff8001ffe0, 'a': 1, 'pnbits':665, 'rnbits':380, 'deg_h_S':20,'cost_S':203, 'deg_h_C':4,'cost_C':213, 'label':"-2^47+2^31-2^17+2^5 Hw2naf 4"},
    {'u':-0x8000fe800000, 'a': 1, 'pnbits':666, 'rnbits':381, 'deg_h_S':20,'cost_S':203, 'deg_h_C':4,'cost_C':213, 'label':"-2^47-2^32+2^25-2^23 Hw2naf 4"},
    {'u':-0x8003b8000000, 'a': 1, 'pnbits':666, 'rnbits':381, 'deg_h_S':20,'cost_S':203, 'deg_h_C':4,'cost_C':213, 'label':"-2^47-2^34+2^30+2^27 Hw2naf 4"},
    {'u':-0x7ff7ff100000, 'a': 1, 'pnbits':665, 'rnbits':380, 'deg_h_S':20,'cost_S':203, 'deg_h_C':4,'cost_C':213, 'label':"-2^47+2^35+2^24-2^20 Hw2naf 4"},
    {'u':-0x800803ff8000, 'a': 1, 'pnbits':666, 'rnbits':381, 'deg_h_S':20,'cost_S':203, 'deg_h_C':4,'cost_C':213, 'label':"-2^47-2^35-2^26+2^15 Hw2naf 4"},
    {'u': 0x8008ffffffe0, 'a': 1, 'pnbits':666, 'rnbits':381, 'deg_h_S':20,'cost_S':203, 'deg_h_C':4,'cost_C':213, 'label':"+2^47+2^35+2^32-2^5 Hw2naf 4"},
    {'u':-0x7ff400000400, 'a': 1, 'pnbits':665, 'rnbits':380, 'deg_h_S':20,'cost_S':203, 'deg_h_C':4,'cost_C':213, 'label':"-2^47+2^36-2^34-2^10 Hw2naf 4"},
    {'u': 0x7c0010008000, 'a': 1, 'pnbits':665, 'rnbits':380, 'deg_h_S':20,'cost_S':203, 'deg_h_C':4,'cost_C':213, 'label':"+2^47-2^42+2^28+2^15 Hw2naf 4"},
    {'u':-0x9fffffff6000, 'a': 1, 'pnbits':670, 'rnbits':383, 'deg_h_S':20,'cost_S':203, 'deg_h_C':4,'cost_C':213, 'label':"-2^47-2^45+2^15+2^13 Hw2naf 4"},
    {'u':-0x9bffffc00000, 'a': 1, 'pnbits':669, 'rnbits':383, 'deg_h_S':20,'cost_S':203, 'deg_h_C':4,'cost_C':213, 'label':"-2^47-2^45+2^42+2^22 Hw2naf 4"},
]
# Auri20 curves with sparse seed u = [0] mod 1 of 48--49 bits Hw2naf 4 and s.t. r has 380 to 385 bits
test_vector_sparse_auri20_D1_a2_e09 = [
    {'u':-0x7ffffffff002, 'a': 6, 'pnbits':665, 'rnbits':380, 'deg_h_S':20,'cost_S':203, 'deg_h_C':4,'cost_C':213, 'label':"-2^47+2^12-2 Hw2naf 3"},
    {'u': 0x7fffffc40002, 'a': 2, 'pnbits':665, 'rnbits':380, 'deg_h_S':20,'cost_S':203, 'deg_h_C':4,'cost_C':213, 'label':"+2^47-2^22+2^18+2 Hw2naf 4"},
    {'u': 0x7ffffe07ffff, 'a': 3, 'pnbits':665, 'rnbits':380, 'deg_h_S':20,'cost_S':203, 'deg_h_C':4,'cost_C':213, 'label':"+2^47-2^25+2^19-1 Hw2naf 4"},
    {'u': 0x80001c000000, 'a':11, 'pnbits':666, 'rnbits':381, 'deg_h_S':20,'cost_S':203, 'deg_h_C':4,'cost_C':213, 'label':"+2^47+2^29-2^26 Hw2naf 3"},
    {'u': 0x820000001000, 'a':17, 'pnbits':666, 'rnbits':381, 'deg_h_S':20,'cost_S':203, 'deg_h_C':4,'cost_C':213, 'label':"+2^47+2^41+2^12 Hw2naf 3"},
    {'u': 0x8007ffffc001, 'a': 3, 'pnbits':666, 'rnbits':381, 'deg_h_S':20,'cost_S':203, 'deg_h_C':4,'cost_C':213, 'label':"+2^47+2^35-2^14+1 Hw2naf 4"},
    {'u':-0x90000007f800, 'a':17, 'pnbits':668, 'rnbits':382, 'deg_h_S':20,'cost_S':203, 'deg_h_C':4,'cost_C':213, 'label':"-2^47-2^44-2^19+2^11 Hw2naf 4"},
    {'u':-0x902000004000, 'a':13, 'pnbits':668, 'rnbits':382, 'deg_h_S':20,'cost_S':203, 'deg_h_C':4,'cost_C':213, 'label':"-2^47-2^44-2^37-2^14 Hw2naf 4"},
    {'u':-0x8fbffff80000, 'a':35, 'pnbits':668, 'rnbits':382, 'deg_h_S':20,'cost_S':203, 'deg_h_C':4,'cost_C':213, 'label':"-2^47-2^44+2^38+2^19 Hw2naf 4"},
    {'u': 0x940000002000, 'a':13, 'pnbits':668, 'rnbits':382, 'deg_h_S':20,'cost_S':203, 'deg_h_C':4,'cost_C':213, 'label':"+2^47+2^44+2^42+2^13 Hw2naf 4"},
    {'u': 0x9fefffffff80, 'a':27, 'pnbits':670, 'rnbits':383, 'deg_h_S':20,'cost_S':203, 'deg_h_C':4,'cost_C':213, 'label':"+2^47+2^45-2^36-2^7 Hw2naf 4"},
]

# KSS20a curves with sparse seed u = [1715, 1815] mod 2050 of 50--51 bits Hw2naf 6 and s.t. r has 378 to 384 bits, p up to 576 bits, p=1 mod 5
test_vector_sparse_kss20a = [
    {'u':-0x20003efbfffff, 'u_mod_5':0, 'a': 2, 'pnbits':573, 'rnbits':378, 'label':"-2^49-2^34+2^28+2^22+1 Hw2naf 5"},
    {'u':-0x1ffff7fffdee1, 'u_mod_5':0, 'a': 1, 'pnbits':573, 'rnbits':378, 'label':"-2^49+2^31+2^13+2^8+2^5-1 Hw2naf 6"},
    {'u':-0x20004003ffef7, 'u_mod_5':0, 'a':-2, 'pnbits':573, 'rnbits':378, 'label':"-2^49-2^34-2^22+2^8+2^3+1 Hw2naf 6"},
    #
    {'u':-0x242000004000d, 'u_mod_5':0, 'a': 2, 'pnbits':576, 'rnbits':379, 'label':"+2^49+2^46+2^41+2^18+2^3+2^2+1 Hw 7"},
    {'u':-0x2200800848003, 'u_mod_5':0, 'a':29, 'pnbits':575, 'rnbits':379, 'label':"+2^49+2^45+2^35+2^23+2^18+2^15+2+1 Hw 8"},
    {'u': 0x2490000000069, 'u_mod_5':0, 'a':-2, 'pnbits':576, 'rnbits':379, 'label':"+2^49+2^46+2^43+2^40+2^6+2^5+2^3+1 Hw 8"},
    {'u': 0x2510408004001, 'u_mod_5':0, 'a': 2, 'pnbits':576, 'rnbits':380, 'label':"+2^49+2^46+2^44+2^40+2^34+2^27+2^14+1 Hw 8"},
    #
    {'u':-0x21feff8023fff, 'u_mod_5':0, 'a': 2, 'pnbits':575, 'rnbits':379, 'label':"-2^49-2^45+2^36+2^27-2^17-2^14+1 Hw2naf 7"},
    {'u':-0x2200f007ffeff, 'u_mod_5':0, 'a': 2, 'pnbits':575, 'rnbits':379, 'label':"-2^49-2^45-2^36+2^32-2^23+2^8+1 Hw2naf 7"},
    {'u': 0x21fe402100001, 'u_mod_5':0, 'a': 2, 'pnbits':575, 'rnbits':379, 'label':"+2^49+2^45-2^37+2^34+2^25+2^20+1 Hw2naf 7"},
    {'u': 0x223ffffffc47f, 'u_mod_5':0, 'a': 1, 'pnbits':575, 'rnbits':379, 'label':"+2^49+2^45+2^42-2^14+2^10+2^7-1 Hw2naf 7"},
    {'u': 0x23fffef0a0001, 'u_mod_5':0, 'a': 2, 'pnbits':576, 'rnbits':379, 'label':"+2^49+2^46-2^28-2^24+2^19+2^17+1 Hw2naf 7"},
    {'u':-0x24007f000403f, 'u_mod_5':0, 'a': 2, 'pnbits':576, 'rnbits':379, 'label':"-2^49-2^46-2^35+2^28-2^14-2^6+1 Hw2naf 7"},
    {'u':-0x242000004000d, 'u_mod_5':0, 'a': 2, 'pnbits':576, 'rnbits':379, 'label':"-2^49-2^46-2^41-2^18-2^4+2^2-1 Hw2naf 7"},
    {'u':-0x24400f000000f, 'u_mod_5':0, 'a': 2, 'pnbits':576, 'rnbits':379, 'label':"-2^49-2^46-2^42-2^32+2^28-2^4+1 Hw2naf 7"},
]

# KSS20b curves with sparse seed u = [1465, 1565] mod 2050 of 50--50 bits Hw2naf 7 such that p = 1 mod 5
test_vector_sparse_kss20b = [
    {'u': 0x2003ffdbb, 'a': 1, 'pnbits':381, 'rnbits':250, 'label':"+2^33+2^22-2^9-2^6-2^2-1 Hw2naf 6"},
    {'u':-0x20400002007e1, 'a': 2, 'pnbits':574, 'rnbits':378, 'label':"-2^49-2^42-2^21-2^11+2^5-1 Hw2naf 6"},
    {'u':-0x207ff00001041, 'a': 2, 'pnbits':574, 'rnbits':378, 'label':"-2^49-2^43+2^32-2^12-2^6-1 Hw2naf 6"},
    {'u':-0x20810ffff8001, 'a': 2, 'pnbits':574, 'rnbits':378, 'label':"-2^49-2^43-2^36-2^32+2^15-1 Hw2naf 6"},
    {'u': 0x209000000ffef, 'a': 2, 'pnbits':574, 'rnbits':378, 'label':"+2^49+2^43+2^40+2^16-2^4-1 Hw2naf 6"},
    {'u': 0x21f007fffffff, 'a': 2, 'pnbits':574, 'rnbits':379, 'label':"+2^49+2^45-2^40+2^31-1 Hw2naf 5"},
    {'u':-0x2240ffffff7ff, 'a': 3, 'pnbits':575, 'rnbits':379, 'label':"-2^49-2^45-2^42-2^36+2^11+1 Hw2naf 6"},
    {'u': 0x23e083fffffff, 'a': 2, 'pnbits':575, 'rnbits':379, 'label':"+2^49+2^46-2^41+2^35+2^30-1 Hw2naf 6"},
    {'u':-0x2600008440001, 'a': 2, 'pnbits':576, 'rnbits':380, 'label':"-2^49-2^47+2^45-2^27-2^22-2^18-1 Hw2naf 7"},
    {'u':-0x2601dffc00001, 'a': 2, 'pnbits':576, 'rnbits':380, 'label':"-2^49-2^47+2^45-2^37+2^33+2^22-1 Hw2naf 7"},
    {'u':-0x2801000200007, 'a': 3, 'pnbits':577, 'rnbits':380, 'label':"-2^49-2^47-2^36-2^21-2^3+1 Hw2naf 6"},
    {'u':-0x3880000050001, 'a': 2, 'pnbits':583, 'rnbits':384, 'label':"-2^50+2^47-2^43-2^18-2^16-1 Hw2naf 6"},
]

# FST66_k20 curves with sparse seed u = [1] mod 3 of 25--25 bits Hw2naf 5 and s.t. r has 384 to 384 bits and p=1 mod 5
# FST66_k20 curves with sparse seed u = [1] mod 3 of 27--27 bits Hw2naf 5 and s.t. p has 570 to 576 bits and p=1 mod 5
test_vector_sparse_fst66_k20 = [
    {'u':-0xff8141,  'u_mod_10':1, 'b':-9, 'pnbits':527, 'rnbits':384, 'cost_S':243, 'deg_h_S':20, 'cost_C':193, 'deg_h_C':4, 'cost_SS':200, 'deg_h_SS':4, 'deg_aux_SS':3, 'label':"-2^24+2^15-2^8-2^6-1 Hw2naf 5"},
    {'u':-0x3eeee00, 'u_mod_10':6, 'b':-4, 'pnbits':570, 'rnbits':416, 'cost_S':248, 'deg_h_S':20, 'cost_C':200, 'deg_h_C':4, 'cost_SS':200, 'deg_h_SS':4, 'deg_aux_SS':3, 'label':"-2^26+2^20+2^16+2^12+2^9 Hw2naf 5"},
    {'u': 0x3fb5fc0, 'u_mod_10':6, 'b':17, 'pnbits':571, 'rnbits':416, 'cost_S':248, 'deg_h_S':20, 'cost_C':200, 'deg_h_C':4, 'cost_SS':200, 'deg_h_SS':4, 'deg_aux_SS':3, 'label':"+2^26-2^18-2^15-2^13-2^6 Hw2naf 5"},
    {'u':-0x400a1fe, 'u_mod_10':6, 'b':-4, 'pnbits':571, 'rnbits':417, 'cost_S':248, 'deg_h_S':20, 'cost_C':200, 'deg_h_C':4, 'cost_SS':200, 'deg_h_SS':4, 'deg_aux_SS':3, 'label':"-2^26-2^15-2^13-2^9+2 Hw2naf 5"},
]

# KSS22 curves with seed u = [4, 18, 25, 39, 81, 95, 116, 123, 144] mod 161 s.t. r has 0 to 512 bits
test_vector_kss22d7 = [
    {'u': 0x21e0d, 'u_mod_11':0, 'a': -35, 'b':   98, 'pnbits':398,'rnbits':333, 'deg_h_S':22,'cost_S':None, 'deg_h_C':11, 'cost_C':None, 'label':"u=+2^17+2^13-2^9+2^4-2^2+1               Hw2NAF=6"},
    {'u':-0x2a1df, 'u_mod_11':2, 'a':-140, 'b': -784, 'pnbits':405,'rnbits':339, 'deg_h_S':22,'cost_S':None, 'deg_h_C':11, 'cost_C':None, 'label':"u=-2^17-2^15-2^13-2^9+2^5+1              Hw2NAF=6"},
    {'u': 0x459dd, 'u_mod_11':7, 'a': -35, 'b':   98, 'pnbits':423,'rnbits':354, 'deg_h_S':22,'cost_S':None, 'deg_h_C':11, 'cost_C':None, 'label':"u=+2^18+2^15-2^13-2^11+2^9-2^5-2^2+1     Hw2NAF=8"},
    {'u': 0x4c545, 'u_mod_11':3, 'a': -35, 'b':   98, 'pnbits':426,'rnbits':357, 'deg_h_S':22,'cost_S':None, 'deg_h_C':11, 'cost_C':None, 'label':"u=+2^18+2^16-2^14+2^10+2^8+2^6+2^2+1     Hw2NAF=8"},
    {'u':-0x6ea5b, 'u_mod_11':0, 'a': -35, 'b':   98, 'pnbits':439,'rnbits':367, 'deg_h_S':22,'cost_S':None, 'deg_h_C':11, 'cost_C':None, 'label':"u=-2^19+2^16+2^13-2^11-2^9-2^7+2^5+2^2+1 Hw2NAF=9"},
    {'u': 0x7657d, 'u_mod_11':7, 'a': -35, 'b':   98, 'pnbits':441,'rnbits':369, 'deg_h_S':22,'cost_S':None, 'deg_h_C':11, 'cost_C':None, 'label':"u=+2^19-2^15-2^13+2^11-2^9-2^7-2^2+1     Hw2NAF=8"},
    {'u':-0x81387, 'u_mod_11':0, 'a':-315, 'b':-2646, 'pnbits':444,'rnbits':372, 'deg_h_S':22,'cost_S':None, 'deg_h_C':11, 'cost_C':None, 'label':"u=-2^19-2^12-2^10+2^7-2^3+1              Hw2NAF=6"},
    {'u':-0x9921f, 'u_mod_11':0, 'a':-140, 'b': -784, 'pnbits':450,'rnbits':377, 'deg_h_S':22,'cost_S':None, 'deg_h_C':11, 'cost_C':None, 'label':"u=-2^19-2^17+2^15-2^12-2^9-2^5+1         Hw2NAF=7"},
    {'u':-0xaa07f, 'u_mod_11':7, 'a':-140, 'b': -784, 'pnbits':453,'rnbits':380, 'deg_h_S':22,'cost_S':None, 'deg_h_C':11, 'cost_C':None, 'label':"u=-2^19-2^17-2^15-2^13-2^7+1             Hw2NAF=6"},
    {'u':-0xbad1f, 'u_mod_11':0, 'a':-140, 'b': -784, 'pnbits':457,'rnbits':382, 'deg_h_S':22,'cost_S':None, 'deg_h_C':11, 'cost_C':None, 'label':"u=-2^20+2^18+2^14+2^12+2^10-2^8-2^5+1    Hw2NAF=8"},
    {'u':-0xbe503, 'u_mod_11':3, 'a': -35, 'b':   98, 'pnbits':457,'rnbits':383, 'deg_h_S':22,'cost_S':220,  'deg_h_C':11, 'cost_C':239,  'label':"u=-2^20+2^18+2^13-2^10-2^8-2^2+1         Hw2NAF=7"},# with --lower_degree_px -deg_px_dec 2
    {'u':-0xffb2f, 'u_mod_11':0, 'a':-140, 'b': -784, 'pnbits':468,'rnbits':391, 'deg_h_S':22,'cost_S':None, 'deg_h_C':11, 'cost_C':None, 'label':"u=-2^20+2^10+2^8-2^6+2^4+1               Hw2NAF=6"},
    {'u':0x137381, 'u_mod_11':7, 'a':-140, 'b': -784, 'pnbits':474,'rnbits':397, 'deg_h_S':22,'cost_S':None, 'deg_h_C':11, 'cost_C':None, 'label':"u=+2^20+2^18-2^15-2^12+2^10-2^7+1        Hw2NAF=7"},
]


# FST63_k22 curves with seed u = [1] mod 2 s.t. r has 380 to 400 bits and p=1 mod 22
test_vector_fst63_k22 = [
    {'u':0x7c1c1, 'u_mod_11':10, 'a': 1, 'pnbits':491,'rnbits':380, 'deg_h_S':22,'cost_S':184, 'deg_h_C':11, 'cost_C':250, 'label':"u=+2^19-2^14+2^9-2^6+1               Hw2NAF=5"},#0
    {'u':0x80119, 'u_mod_11': 1, 'a': 1, 'pnbits':493,'rnbits':381, 'deg_h_S':22,'cost_S':184, 'deg_h_C':11, 'cost_C':250, 'label':"u=+2^19+2^8+2^5-2^3+1                Hw2NAF=5"},
    {'u':0x846b5, 'u_mod_11': 1, 'a': 1, 'pnbits':494,'rnbits':381, 'deg_h_S':22,'cost_S':184, 'deg_h_C':11, 'cost_C':250, 'label':"u=+2^19+2^14+2^11-2^8-2^6-2^4+2^2+1  Hw2NAF=8"},
    {'u':0x85447, 'u_mod_11':10, 'a': 1, 'pnbits':494,'rnbits':382, 'deg_h_S':22,'cost_S':184, 'deg_h_C':11, 'cost_C':250, 'label':"u=+2^19+2^14+2^12+2^10+2^6+2^3-1     Hw2NAF=7"},
    {'u':0x86bff, 'u_mod_11':10, 'a': 1, 'pnbits':494,'rnbits':382, 'deg_h_S':22,'cost_S':184, 'deg_h_C':11, 'cost_C':250, 'label':"u=+2^19+2^15-2^12-2^10-1             Hw2NAF=5"},
    {'u':0x8b49d, 'u_mod_11':10, 'a': 1, 'pnbits':496,'rnbits':383, 'deg_h_S':22,'cost_S':184, 'deg_h_C':11, 'cost_C':250, 'label':"u=+2^19+2^16-2^14-2^12+2^10+2^7+2^5-2^2+1 Hw2NAF=9"},
    {'u':0x92507, 'u_mod_11': 1, 'a': 1, 'pnbits':498,'rnbits':384, 'deg_h_S':22,'cost_S':184, 'deg_h_C':11, 'cost_C':250, 'label':"u=+2^19+2^16+2^13+2^10+2^8+2^3-1     Hw2NAF=7"},#6
    {'u':0x957b9, 'u_mod_11':10, 'a': 1, 'pnbits':498,'rnbits':385, 'deg_h_S':22,'cost_S':184, 'deg_h_C':11, 'cost_C':250, 'label':"u=+2^19+2^17-2^15-2^13-2^11-2^6-2^3+1 Hw2NAF=8"},
    {'u':0x9e047, 'u_mod_11':10, 'a': 1, 'pnbits':500,'rnbits':387, 'deg_h_S':22,'cost_S':185, 'deg_h_C':11, 'cost_C':250, 'label':"u=+2^19+2^17-2^13+2^6+2^3-1          Hw2NAF=6"},
    {'u':0x9e17d, 'u_mod_11': 1, 'a': 1, 'pnbits':500,'rnbits':387, 'deg_h_S':22,'cost_S':185, 'deg_h_C':11, 'cost_C':250, 'label':"u=+2^19+2^17-2^13+2^9-2^7-2^2+1      Hw2NAF=7"},
    {'u':0xa0c5d, 'u_mod_11':10, 'a': 1, 'pnbits':501,'rnbits':387, 'deg_h_S':22,'cost_S':185, 'deg_h_C':11, 'cost_C':250, 'label':"u=+2^19+2^17+2^12-2^10+2^7-2^5-2^2+1 Hw2NAF=8"},
    {'u':0xb55ef, 'u_mod_11':10, 'a': 1, 'pnbits':506,'rnbits':391, 'deg_h_S':22,'cost_S':186, 'deg_h_C':11, 'cost_C':250, 'label':"u=+2^20-2^18-2^15-2^13-2^11-2^9-2^4-1 Hw2NAF=8"},
    {'u':0xb570d, 'u_mod_11':10, 'a': 1, 'pnbits':506,'rnbits':391, 'deg_h_S':22,'cost_S':186, 'deg_h_C':11, 'cost_C':250, 'label':"u=+2^20-2^18-2^15-2^13-2^11-2^8+2^4-2^2+1 Hw2NAF=9"},
    {'u':0xbd485, 'u_mod_11':10, 'a': 1, 'pnbits':507,'rnbits':392, 'deg_h_S':22,'cost_S':186, 'deg_h_C':11, 'cost_C':250, 'label':"u=+2^20-2^18-2^14+2^12+2^10+2^7+2^2+1 Hw2NAF=8"},
    {'u':0xc997f, 'u_mod_11': 1, 'a': 1, 'pnbits':510,'rnbits':394, 'deg_h_S':22,'cost_S':187, 'deg_h_C':11, 'cost_C':250, 'label':"u=+2^20-2^18+2^15+2^13-2^11+2^9-2^7-1 Hw2NAF=8"},
    {'u':0xd20c3, 'u_mod_11': 1, 'a': 1, 'pnbits':511,'rnbits':395, 'deg_h_S':22,'cost_S':187, 'deg_h_C':11, 'cost_C':250, 'label':"u=+2^20-2^18+2^16+2^13+2^8-2^6+2^2-1 Hw2NAF=8"},#15
    {'u':0xe547f, 'u_mod_11':10, 'a': 1, 'pnbits':514,'rnbits':397, 'deg_h_S':22,'cost_S':190, 'deg_h_C':11, 'cost_C':252, 'label':"u=+2^20-2^17+2^14+2^12+2^10+2^7-1    Hw2NAF=7"},
    {'u':0xe706d, 'u_mod_11':10, 'a': 1, 'pnbits':515,'rnbits':398, 'deg_h_S':22,'cost_S':190, 'deg_h_C':11, 'cost_C':252, 'label':"u=+2^20-2^17+2^15-2^12+2^7-2^4-2^2+1 Hw2NAF=8"},
    {'u':0xe9b39, 'u_mod_11':10, 'a': 1, 'pnbits':515,'rnbits':398, 'deg_h_S':22,'cost_S':190, 'deg_h_C':11, 'cost_C':252, 'label':"u=+2^20-2^17+2^15+2^13-2^10-2^8+2^6-2^3+1 Hw2NAF=9"},
    {'u':0xf705b, 'u_mod_11': 1, 'a': 1, 'pnbits':517,'rnbits':399, 'deg_h_S':22,'cost_S':190, 'deg_h_C':11, 'cost_C':252, 'label':"u=+2^20-2^15-2^12+2^7-2^5-2^2-1      Hw2NAF=7"},
    {'u':0x10aa5d, 'u_mod_11':10,'a': 1, 'pnbits':520,'rnbits':402, 'deg_h_S':22,'cost_S':190, 'deg_h_C':11, 'cost_C':252, 'label':"u=+2^20+2^15+2^13+2^11+2^9+2^7-2^5-2^2+1 Hw2NAF=9"},#20
    {'u':0x10bfd9, 'u_mod_11':10,'a': 1, 'pnbits':520,'rnbits':402, 'deg_h_S':22,'cost_S':190, 'deg_h_C':11, 'cost_C':252, 'label':"u=+2^20+2^16-2^14-2^5-2^3+1          Hw2NAF=6"},
    {'u':0x1166bf, 'u_mod_11':1, 'a': 1, 'pnbits':522,'rnbits':403, 'deg_h_S':22,'cost_S':190, 'deg_h_C':11, 'cost_C':252, 'label':"u=+2^20+2^17-2^15-2^13+2^11-2^8-2^6-1 Hw2NAF=8"},
    {'u':0x119e6f, 'u_mod_11':1, 'a': 1, 'pnbits':522,'rnbits':403, 'deg_h_S':22,'cost_S':190, 'deg_h_C':11, 'cost_C':252, 'label':"u=+2^20+2^17-2^15+2^13-2^9+2^7-2^4-1 Hw2NAF=8"},
    {'u':0x11a171, 'u_mod_11':1, 'a': 1, 'pnbits':522,'rnbits':403, 'deg_h_S':22,'cost_S':190, 'deg_h_C':11, 'cost_C':252, 'label':"u=+2^20+2^17-2^15+2^13+2^9-2^7-2^4+1 Hw2NAF=8"},
    {'u':0x11be7d, 'u_mod_11':1, 'a': 1, 'pnbits':522,'rnbits':403, 'deg_h_S':22,'cost_S':190, 'deg_h_C':11, 'cost_C':252, 'label':"u=+2^20+2^17-2^14-2^9+2^7-2^2+1      Hw2NAF=7"},
    {'u':0x11fa37, 'u_mod_11':1, 'a': 1, 'pnbits':523,'rnbits':404, 'deg_h_S':22,'cost_S':190, 'deg_h_C':11, 'cost_C':252, 'label':"u=+2^20+2^17-2^11+2^9+2^6-2^3-1      Hw2NAF=7"},
    {'u':0x12193d, 'u_mod_11':1, 'a': 1, 'pnbits':523,'rnbits':404, 'deg_h_S':22,'cost_S':190, 'deg_h_C':11, 'cost_C':252, 'label':"u=+2^20+2^17+2^13-2^11+2^8+2^6-2^2+1 Hw2NAF=8"},
    {'u':0x122b1b, 'u_mod_11':10,'a': 1, 'pnbits':523,'rnbits':404, 'deg_h_S':22,'cost_S':190, 'deg_h_C':11, 'cost_C':252, 'label':"u=+2^20+2^17+2^14-2^12-2^10-2^8+2^5-2^2-1 Hw2NAF=9"},#28
    {'u':0x1fe049, 'u_mod_11':1, 'a': 1, 'pnbits':544,'rnbits':420, 'deg_h_S':22,'cost_S':192, 'deg_h_C':11, 'cost_C':254, 'label':"u=+2^21-2^13+2^6+2^3+1               Hw2NAF=5"},#29
    {'u':0x2fedb9, 'u_mod_11':10,'a': 1, 'pnbits':560,'rnbits':432, 'deg_h_S':22,'cost_S':194, 'deg_h_C':11, 'cost_C':254, 'label':"u=+2^22-2^20-2^12-2^9-2^6-2^3+1      Hw2NAF=7"},#30
    {'u':0x492005, 'u_mod_11':10,'a': 1, 'pnbits':575,'rnbits':444, 'deg_h_S':22,'cost_S':194, 'deg_h_C':11, 'cost_C':254, 'label':"u=+2^22+2^19+2^16+2^13+2^2+1         Hw2NAF=6"},#31
]

test_vector_fst66_k22 = [
    # x = 1, 5 mod 11 to ensure p = 1 mod 11
    # p up to 512 bits
    # negative u
    {'u':-0x4b5d5, 'u_mod_11':0, 'b': 1, 'pnbits':510,'rnbits':365, 'deg_h_S':None,'cost_S':None, 'label':"u=-2^18-2^16+2^14+2^11+2^9+2^6-2^4-2^2-1 Hw2NAF=9"},#0
    {'u':-0x4bfd7, 'u_mod_11':1, 'b': 1, 'pnbits':510,'rnbits':365, 'deg_h_S':None,'cost_S':None, 'label':"u=-2^18-2^16+2^14+2^5+2^3+1          Hw2NAF=6"},#1
    {'u':-0x4c0ac, 'u_mod_11':8, 'b':-2, 'pnbits':510,'rnbits':365, 'deg_h_S':None,'cost_S':None, 'label':"u=-2^18-2^16+2^14-2^8+2^6+2^4+2^2    Hw2NAF=7"},#2
    {'u':-0x4db9d, 'u_mod_11':8, 'b': 1, 'pnbits':511,'rnbits':366, 'deg_h_S':None,'cost_S':None, 'label':"u=-2^18-2^16+2^13+2^10+2^7-2^5+2^2-1 Hw2NAF=8"},#3
    {'u':-0x4dcb7, 'u_mod_11':1, 'b': 1, 'pnbits':511,'rnbits':366, 'deg_h_S':None,'cost_S':None, 'label':"u=-2^18-2^16+2^13+2^10-2^8+2^6+2^3+1 Hw2NAF=8"},#4
    {'u':-0x4e4e2, 'u_mod_11':0, 'b':-2, 'pnbits':511,'rnbits':366, 'deg_h_S':None,'cost_S':None, 'label':"u=-2^18-2^16+2^13-2^10-2^8+2^5-2     Hw2NAF=7"},#5
    # positive u
    {'u': 0x4b865, 'u_mod_11':7, 'b': 1, 'pnbits':510,'rnbits':365, 'deg_h_S':None,'cost_S':None, 'label':"u=+2^18+2^16-2^14-2^11+2^7-2^5+2^2+1 Hw2NAF=8"},#6
    {'u': 0x4e268, 'u_mod_11':4, 'b':-2, 'pnbits':511,'rnbits':366, 'deg_h_S':None,'cost_S':None, 'label':"u=+2^18+2^16-2^13+2^9+2^7-2^5+2^3    Hw2NAF=7"},#7
    {'u': 0x4e712, 'u_mod_11':10,'b':-2, 'pnbits':511,'rnbits':366, 'deg_h_S':None,'cost_S':None, 'label':"u=+2^18+2^16-2^13+2^11-2^8+2^4+2     Hw2NAF=7"},#8
    # r close to 384 bits
    {'u': 0x7d722, 'u_mod_11':5, 'b':-2, 'pnbits':530,'rnbits':380, 'deg_h_S':None,'cost_S':None, 'label':"u=+2^19-2^13-2^11-2^8+2^5+2          Hw2NAF=6"},#9
    {'u': 0x80572, 'u_mod_11':3, 'b':-2, 'pnbits':531,'rnbits':381, 'deg_h_S':None,'cost_S':None, 'label':"u=+2^19+2^11-2^9-2^7-2^4+2           Hw2NAF=6"},#10
    {'u': 0x80b51, 'u_mod_11':10,'b': 1, 'pnbits':531,'rnbits':381, 'deg_h_S':None,'cost_S':None, 'label':"u=+2^19+2^12-2^10-2^8+2^6+2^4+1      Hw2NAF=7"},#11
    {'u': 0x811e4, 'u_mod_11':10,'b':-2, 'pnbits':531,'rnbits':381, 'deg_h_S':None,'cost_S':None, 'label':"u=+2^19+2^12+2^9-2^5+2^2             Hw2NAF=5"},#12
    {'u': 0x818f8, 'u_mod_11':7, 'b':-2, 'pnbits':531,'rnbits':381, 'deg_h_S':None,'cost_S':None, 'label':"u=+2^19+2^13-2^11+2^8-2^3            Hw2NAF=5"},#13
    {'u': 0x82a1a, 'u_mod_11':4, 'b':-2, 'pnbits':532,'rnbits':381, 'deg_h_S':None,'cost_S':None, 'label':"u=+2^19+2^13+2^11+2^9+2^5-2^3+2      Hw2NAF=7"},#14
    {'u': 0x853ab, 'u_mod_11':8, 'b': 1, 'pnbits':533,'rnbits':382, 'deg_h_S':None,'cost_S':None, 'label':"u=+2^19+2^14+2^12+2^10-2^6-2^4-2^2-1 Hw2NAF=8"},#15
    {'u': 0x879b5, 'u_mod_11':0, 'b': 1, 'pnbits':533,'rnbits':382, 'deg_h_S':None,'cost_S':None, 'label':"u=+2^19+2^15-2^11+2^9-2^6-2^4+2^2+1  Hw2NAF=8"},#16
    {'u': 0x880b4, 'u_mod_11':9, 'b':-2, 'pnbits':533,'rnbits':382, 'deg_h_S':None,'cost_S':None, 'label':"u=+2^19+2^15+2^8-2^6-2^4+2^2         Hw2NAF=6"},#17
    {'u': 0x8894b, 'u_mod_11':8, 'b': 1, 'pnbits':534,'rnbits':382, 'deg_h_S':None,'cost_S':None, 'label':"u=+2^19+2^15+2^11+2^8+2^6+2^4-2^2-1  Hw2NAF=8"},#18
    {'u': 0x8919a, 'u_mod_11':1, 'b':-2, 'pnbits':534,'rnbits':382, 'deg_h_S':None,'cost_S':None, 'label':"u=+2^19+2^15+2^12+2^9-2^7+2^5-2^3+2  Hw2NAF=8"},#19
    {'u': 0x89c1a, 'u_mod_11':5, 'b':-2, 'pnbits':534,'rnbits':383, 'deg_h_S':None,'cost_S':None, 'label':"u=+2^19+2^15+2^13-2^10+2^5-2^3+2     Hw2NAF=7"},#20
    {'u': 0x89e3c, 'u_mod_11':1, 'b':-2, 'pnbits':534,'rnbits':383, 'deg_h_S':None,'cost_S':None, 'label':"u=+2^19+2^15+2^13-2^9+2^6-2^2        Hw2NAF=6"},#21
    {'u': 0x8a808, 'u_mod_11':1, 'b':-2, 'pnbits':534,'rnbits':383, 'deg_h_S':None,'cost_S':None, 'label':"u=+2^19+2^15+2^13+2^11+2^3           Hw2NAF=5"},#22
    {'u': 0x8e1e3, 'u_mod_11':6, 'b': 1, 'pnbits':535,'rnbits':384, 'deg_h_S':None,'cost_S':None, 'label':"u=+2^19+2^16-2^13+2^9-2^5+2^2-1      Hw2NAF=7"},#23
    {'u': 0x8e483, 'u_mod_11':7, 'b': 1, 'pnbits':535,'rnbits':384, 'deg_h_S':None,'cost_S':None, 'label':"u=+2^19+2^16-2^13+2^10+2^7+2^2-1     Hw2NAF=7"},#24
    {'u': 0x90265, 'u_mod_11':1, 'b': 1, 'pnbits':536,'rnbits':384, 'deg_h_S':None,'cost_S':None, 'label':"u=+2^19+2^16+2^9+2^7-2^5+2^2+1       Hw2NAF=7"},#25
    {'u': 0x916e4, 'u_mod_11':1, 'b':-2, 'pnbits':536,'rnbits':384, 'deg_h_S':None,'cost_S':None, 'label':"u=+2^19+2^16+2^13-2^11-2^8-2^5+2^2   Hw2NAF=7"},#26
    {'u': 0x91f51, 'u_mod_11':2, 'b': 1, 'pnbits':536,'rnbits':384, 'deg_h_S':None,'cost_S':None, 'label':"u=+2^19+2^16+2^13-2^8+2^6+2^4+1      Hw2NAF=7"},#27
    #
    {'u':-0x81bc3, 'u_mod_11':4, 'b': 1, 'pnbits':531,'rnbits':381, 'deg_h_S':None,'cost_S':None, 'label':"u=-2^19-2^13+2^10+2^6-2^2+1          Hw2NAF=6"},#28
    {'u':-0x824c9, 'u_mod_11':4, 'b': 1, 'pnbits':532,'rnbits':381, 'deg_h_S':None,'cost_S':None, 'label':"u=-2^19-2^13-2^10-2^8+2^6-2^3-1      Hw2NAF=7"},#29
    {'u':-0x82bad, 'u_mod_11':0, 'b': 1, 'pnbits':532,'rnbits':381, 'deg_h_S':None,'cost_S':None, 'label':"u=-2^19-2^14+2^12+2^10+2^6+2^4+2^2-1 Hw2NAF=8"},#30
    {'u':-0x83f12, 'u_mod_11':7, 'b':-2, 'pnbits':532,'rnbits':381, 'deg_h_S':None,'cost_S':None, 'label':"u=-2^19-2^14+2^8-2^4-2               Hw2NAF=5"},#31
    {'u':-0x866ed, 'u_mod_11':1, 'b': 1, 'pnbits':533,'rnbits':382, 'deg_h_S':None,'cost_S':None, 'label':"u=-2^19-2^15+2^13-2^11+2^8+2^4+2^2-1 Hw2NAF=8"},#32
    {'u':-0x86984, 'u_mod_11':9, 'b':-2, 'pnbits':533,'rnbits':382, 'deg_h_S':None,'cost_S':None, 'label':"u=-2^19-2^15+2^13-2^11-2^9+2^7-2^2   Hw2NAF=7"},#33
    {'u':-0x86987, 'u_mod_11':6, 'b': 1, 'pnbits':533,'rnbits':382, 'deg_h_S':None,'cost_S':None, 'label':"u=-2^19-2^15+2^13-2^11-2^9+2^7-2^3+1 Hw2NAF=8"},#34
    {'u':-0x8e04c, 'u_mod_11':5, 'b':-2, 'pnbits':535,'rnbits':383, 'deg_h_S':None,'cost_S':None, 'label':"u=-2^19-2^16+2^13-2^6-2^4+2^2        Hw2NAF=6"},#35
    {'u':-0x925d3, 'u_mod_11':4, 'b': 1, 'pnbits':536,'rnbits':384, 'deg_h_S':None,'cost_S':None, 'label':"u=-2^19-2^16-2^13-2^11+2^9+2^6-2^4-2^2+1 Hw2NAF=9"},#36
]

# BLS15, choose u = 1, 7 mod 15 to ensure p = 1 mod 15 for easier towering, that is, u = 1, 2 mod 5 (u = 1 mod 3 by design)
# BLS15 curves with sparse seed u = [1, 7] mod 15 of 48--49 bits Hw2naf 4 and s.t. r has 380 to 384 bits
test_vector_sparse_bls15 = [
    {'u':-0x8f000000, 'u_mod_5':2, 'b':-2, 'pnbits':373, 'rnbits':250, 'cost_S':None, 'deg_h_S':None, 'cost_C':None, 'deg_h_C':None, 'label':"-2^31-2^28+2^24 Hw2naf 3"},
    {'u': 0xb0080048, 'u_mod_5':1, 'b':-2, 'pnbits':376, 'rnbits':252, 'cost_S':None, 'deg_h_S':None, 'cost_C':None, 'deg_h_C':None, 'label':"+2^31+2^29+2^28+2^19+2^6+2^3 Hw 6"},
    {'u':-0xc100001f, 'u_mod_5':1, 'b': 1, 'pnbits':378, 'rnbits':253, 'cost_S':None, 'deg_h_S':None, 'cost_C':None, 'deg_h_C':None, 'label':"-2^32+2^30-2^24-2^5+1 Hw2naf 5"},
    {'u':-0xfbffeffd, 'u_mod_5':2, 'b': 1, 'pnbits':383, 'rnbits':256, 'cost_S':None, 'deg_h_S':None, 'cost_C':None, 'deg_h_C':None, 'label':"-2^32+2^26+2^12+2^2-1 Hw2naf 5"},
    {'u': 0xfe0001f1, 'u_mod_5':1, 'b': 1, 'pnbits':383, 'rnbits':256, 'cost_S':None, 'deg_h_S':None, 'cost_C':None, 'deg_h_C':None, 'label':"+2^32-2^25+2^9-2^4+1 Hw2naf 5"},
    {'u':-0xfffc0a01, 'u_mod_5':2, 'b': 1, 'pnbits':383, 'rnbits':256, 'cost_S':None, 'deg_h_S':None, 'cost_C':None, 'deg_h_C':None, 'label':"-2^32+2^18-2^11-2^9-1 Hw2naf 5"},
    {'u': 0xffffdbf7, 'u_mod_5':1, 'b': 1, 'pnbits':383, 'rnbits':256, 'cost_S':None, 'deg_h_S':None, 'cost_C':None, 'deg_h_C':None, 'label':"+2^32-2^13-2^10-2^3-1 Hw2naf 5"},
    {'u':-0xffffc3fffffe, 'u_mod_5':1, 'b':16, 'pnbits':575, 'rnbits':384, 'cost_S':160, 'deg_h_S':15, 'cost_C':177, 'deg_h_C':3, 'label':"-2^48+2^30-2^26+2 Hw2naf 4"},
    # BLS15 curves with sparse seed u = [1, 7] mod 15 of 64--65 bits Hw2naf 4 and s.t. p has 760 to 768 bits, r > 512 bits removed
    {'u':  0xfffffffe00fff800, 'u_mod_5':2, 'b':-2, 'pnbits':767, 'rnbits':512, 'cost_S':178, 'deg_h_S':15, 'cost_C':200, 'deg_h_C':3, 'label':"+2^64-2^33+2^24-2^11 Hw2naf 4"},
    {'u': -0xfff7f80000000800, 'u_mod_5':2, 'b':-2, 'pnbits':767, 'rnbits':512, 'cost_S':178, 'deg_h_S':15, 'cost_C':200, 'deg_h_C':3, 'label':"-2^64+2^51+2^43-2^11 Hw2naf 4"},
    {'u': -0xfbffffffffffffde, 'u_mod_5':2, 'b':14, 'pnbits':767, 'rnbits':512, 'cost_S':178, 'deg_h_S':15, 'cost_C':200, 'deg_h_C':3, 'label':"-2^64+2^58+2^5+2 Hw2naf 4"},
    # BLS15 curves with sparse seed u = [1, 7] mod 15 of 75--76 bits Hw2naf 4 and s.t. p has 890 to 896 bits
    {'u':-0x4ffbffff80000000000, 'u_mod_5':2, 'b':-2, 'pnbits':891, 'rnbits':595, 'cost_S':190, 'deg_h_S':15, 'cost_C':213, 'deg_h_C':3, 'label':"-2^74-2^72+2^62+2^43 Hw2naf 4"},
    # BLS15 curves with sparse seed u = [1, 7] mod 15 of 75--75 bits Hw 5 and s.t. p has 888 to 896 bits
    # avoid negative 'bits' in the seed as with odd embedding degree, inversion and conjugation are not free but cost some multiplications: f^(p^10+p^5+1) = 1 => f^(p^10+p^5) = 1/f
    {'u': 0x4800002000400000004, 'u_mod_5':2, 'b': 2, 'pnbits':889, 'rnbits':594, 'cost_S':190, 'deg_h_S':15, 'cost_C':213, 'deg_h_C':3, 'label':"+2^74+2^71+2^49+2^34+2^2 Hw 5"},
    {'u': 0x5800000008010000000, 'u_mod_5':2, 'b':-2, 'pnbits':892, 'rnbits':596, 'cost_S':190, 'deg_h_S':15, 'cost_C':213, 'deg_h_C':3, 'label':"+2^74+2^72+2^71+2^39+2^28 Hw 5"},
    {'u': 0x6004800000000000040, 'u_mod_5':2, 'b':-2, 'pnbits':894, 'rnbits':597, 'cost_S':190, 'deg_h_S':15, 'cost_C':213, 'deg_h_C':3, 'label':"+2^74+2^73+2^62+2^59+2^6 Hw 5"},
]

# BLS21 curves with sparse seed u = [1, 4] mod 6 of 33--33 bits Hw2naf 5 and s.t. r has 384 to 384 bits
# u % 7 == 1 allows to have p = 1 mod 7 as (px-1).roots(GF(7)) gives root (1).
test_vector_sparse_bls21 = [
    {'u':-0x1b1ee0, 'u_mod_7':1, 'b':-2, 'pnbits':331,'rnbits':250, 'deg_h_S':21,'cost_S':178, 'deg_h_C':7, 'cost_C':171, 'label':"u=-2^21+2^18+2^16-2^13+2^8+2^5       Hw2NAF=6"},
    {'u': 0x1b61fc, 'u_mod_7':1, 'b': 2, 'pnbits':331,'rnbits':250, 'deg_h_S':21,'cost_S':178, 'deg_h_C':7, 'cost_C':171, 'label':"u=+2^21-2^18-2^15-2^13+2^9-2^2       Hw2NAF=6"},
    {'u': 0x1c7812, 'u_mod_7':1, 'b':16, 'pnbits':332,'rnbits':250, 'deg_h_S':21,'cost_S':178, 'deg_h_C':7, 'cost_C':171, 'label':"u=+2^21-2^18+2^15-2^11+2^4+2         Hw2NAF=6"},
    {'u': 0x1d75e0, 'u_mod_7':1, 'b':-2, 'pnbits':333,'rnbits':251, 'deg_h_S':21,'cost_S':178, 'deg_h_C':7, 'cost_C':171, 'label':"u=+2^21-2^17-2^15-2^11-2^9-2^5       Hw2NAF=6"},
    {'u': 0x1dc0b0, 'u_mod_7':1, 'b':-2, 'pnbits':333,'rnbits':251, 'deg_h_S':21,'cost_S':178, 'deg_h_C':7, 'cost_C':171, 'label':"u=+2^21-2^17-2^14+2^8-2^6-2^4        Hw2NAF=6"},
    {'u':-0x1f9eec, 'u_mod_7':1, 'b': 2, 'pnbits':335,'rnbits':252, 'deg_h_S':21,'cost_S':178, 'deg_h_C':7, 'cost_C':171, 'label':"u=-2^21+2^15-2^13+2^8+2^4+2^2        Hw2NAF=6"},
    {'u': 0x206c41, 'u_mod_7':1, 'b': 1, 'pnbits':335,'rnbits':253, 'deg_h_S':21,'cost_S':178, 'deg_h_C':7, 'cost_C':171, 'label':"u=+2^21+2^15-2^12-2^10+2^6+1         Hw2NAF=6"},
    {'u':-0x221f81, 'u_mod_7':1, 'b': 1, 'pnbits':336,'rnbits':254, 'deg_h_S':21,'cost_S':178, 'deg_h_C':7, 'cost_C':171, 'label':"u=-2^21-2^17-2^13+2^7-1              Hw2NAF=5"},
    {'u': 0x23adf0, 'u_mod_7':1, 'b':-2, 'pnbits':337,'rnbits':254, 'deg_h_S':21,'cost_S':178, 'deg_h_C':7, 'cost_C':171, 'label':"u=+2^21+2^18-2^14-2^12-2^9-2^4       Hw2NAF=6"},
    {'u': 0x23af40, 'u_mod_7':1, 'b':-2, 'pnbits':337,'rnbits':254, 'deg_h_S':21,'cost_S':178, 'deg_h_C':7, 'cost_C':171, 'label':"u=+2^21+2^18-2^14-2^12-2^8+2^6       Hw2NAF=6"},
    {'u': 0x27f6f1, 'u_mod_7':1, 'b': 1, 'pnbits':340,'rnbits':256, 'deg_h_S':21,'cost_S':178, 'deg_h_C':7, 'cost_C':171, 'label':"u=+2^21+2^19-2^11-2^8-2^4+1          Hw2NAF=6"},
    {'u':-0x288710, 'u_mod_7':1, 'b':-2, 'pnbits':340,'rnbits':257, 'deg_h_S':21,'cost_S':178, 'deg_h_C':7, 'cost_C':171, 'label':"u=-2^21-2^19-2^15-2^11+2^8-2^4       Hw2NAF=6"},
    {'u': 0x28c7e0, 'u_mod_7':1, 'b':-2, 'pnbits':341,'rnbits':257, 'deg_h_S':21,'cost_S':178, 'deg_h_C':7, 'cost_C':171, 'label':"u=+2^21+2^19+2^16-2^14+2^11-2^5      Hw2NAF=6"},
    #
    {'u':-0xfdffffbe, 'u_mod_7':1, 'b':16, 'pnbits':511, 'rnbits':384, 'deg_h_S':21,'cost_S':199, 'deg_h_C':7, 'cost_C':210, 'label':"-2^32+2^25+2^6+2 Hw2naf 4"},# in paper
    {'u':-0xfbffefc1, 'u_mod_7':1, 'b': 1, 'pnbits':511, 'rnbits':384, 'deg_h_S':21,'cost_S':199, 'deg_h_C':7, 'cost_C':210, 'label':"-2^32+2^26+2^12+2^6-1 Hw2naf 5"},
    {'u': 0xfbdf7f00, 'u_mod_7':1, 'b':-2, 'pnbits':511, 'rnbits':384, 'deg_h_S':21,'cost_S':199, 'deg_h_C':7, 'cost_C':210, 'label':"+2^32-2^26-2^21-2^15-2^8 Hw2naf 5"},
    #
    {'u': 0xfffb1802, 'u_mod_7':1, 'b':11, 'pnbits':511, 'rnbits':384, 'deg_h_S':21,'cost_S':199, 'deg_h_C':7, 'cost_C':210, 'label':"+2^32-2^18-2^16+2^13-2^11+2 Hw2naf 6"},
    {'u': 0xff7fef22, 'u_mod_7':1, 'b':16, 'pnbits':511, 'rnbits':384, 'deg_h_S':21,'cost_S':199, 'deg_h_C':7, 'cost_C':210, 'label':"+2^32-2^23-2^12-2^8+2^5+2 Hw2naf 6"},
    {'u':-0xff7f9fe2, 'u_mod_7':1, 'b': 2, 'pnbits':511, 'rnbits':384, 'deg_h_S':21,'cost_S':199, 'deg_h_C':7, 'cost_C':210, 'label':"-2^32+2^23+2^15-2^13+2^5-2 Hw2naf 6"},
    {'u':-0xff6e3ffc, 'u_mod_7':1, 'b': 2, 'pnbits':511, 'rnbits':384, 'deg_h_S':21,'cost_S':199, 'deg_h_C':7, 'cost_C':210, 'label':"-2^32+2^23+2^20+2^17-2^14+2^2 Hw2naf 6"},
    {'u':-0xffa04804, 'u_mod_7':1, 'b': 2, 'pnbits':511, 'rnbits':384, 'deg_h_S':21,'cost_S':199, 'deg_h_C':7, 'cost_C':210, 'label':"-2^32+2^23-2^21-2^14-2^11-2^2 Hw2naf 6"},
    {'u':-0xff608c00, 'u_mod_7':1, 'b':-2, 'pnbits':511, 'rnbits':384, 'deg_h_S':21,'cost_S':199, 'deg_h_C':7, 'cost_C':210, 'label':"-2^32+2^23+2^21-2^15-2^12+2^10 Hw2naf 6"},
    {'u':-0xffa0ff70, 'u_mod_7':1, 'b':-2, 'pnbits':511, 'rnbits':384, 'deg_h_S':21,'cost_S':199, 'deg_h_C':7, 'cost_C':210, 'label':"-2^32+2^23-2^21-2^16+2^7+2^4 Hw2naf 6"},
    {'u': 0xfefe2007, 'u_mod_7':1, 'b': 1, 'pnbits':511, 'rnbits':384, 'deg_h_S':21,'cost_S':199, 'deg_h_C':7, 'cost_C':210, 'label':"+2^32-2^24-2^17+2^13+2^3-1 Hw2naf 6"},
    {'u':-0xfefc1440, 'u_mod_7':1, 'b':-2, 'pnbits':511, 'rnbits':384, 'deg_h_S':21,'cost_S':199, 'deg_h_C':7, 'cost_C':210, 'label':"-2^32+2^24+2^18-2^12-2^10-2^6 Hw2naf 6"},
    {'u':-0xff3e4008, 'u_mod_7':1, 'b':-2, 'pnbits':511, 'rnbits':384, 'deg_h_S':21,'cost_S':199, 'deg_h_C':7, 'cost_C':210, 'label':"-2^32+2^24-2^22+2^17-2^14-2^3 Hw2naf 6"},
    {'u': 0xfec7c400, 'u_mod_7':1, 'b':-2, 'pnbits':511, 'rnbits':384, 'deg_h_S':21,'cost_S':199, 'deg_h_C':7, 'cost_C':210, 'label':"+2^32-2^24-2^22+2^19-2^14+2^10 Hw2naf 6"},
    {'u': 0xfdf8fff1, 'u_mod_7':1, 'b': 1, 'pnbits':511, 'rnbits':384, 'deg_h_S':21,'cost_S':199, 'deg_h_C':7, 'cost_C':210, 'label':"+2^32-2^25-2^19+2^16-2^4+1 Hw2naf 6"},
    {'u': 0xfc00d780, 'u_mod_7':1, 'b':-2, 'pnbits':511, 'rnbits':384, 'deg_h_S':21,'cost_S':199, 'deg_h_C':7, 'cost_C':210, 'label':"+2^32-2^26+2^16-2^13-2^11-2^7 Hw2naf 6"},
    {'u': 0xfbfd07fc, 'u_mod_7':1, 'b': 2, 'pnbits':511, 'rnbits':384, 'deg_h_S':21,'cost_S':199, 'deg_h_C':7, 'cost_C':210, 'label':"+2^32-2^26-2^18+2^16+2^11-2^2 Hw2naf 6"},
    {'u':-0xfbe40102, 'u_mod_7':1, 'b': 2, 'pnbits':511, 'rnbits':384, 'deg_h_S':21,'cost_S':199, 'deg_h_C':7, 'cost_C':210, 'label':"-2^32+2^26+2^21-2^18-2^8-2 Hw2naf 6"},
    {'u':-0xf7bdbff8, 'u_mod_7':1, 'b':-2, 'pnbits':510, 'rnbits':384, 'deg_h_S':21,'cost_S':199, 'deg_h_C':7, 'cost_C':210, 'label':"-2^32+2^27+2^22+2^17+2^14+2^3 Hw2naf 6"},
    {'u':-0xf8fbf004, 'u_mod_7':1, 'b': 2, 'pnbits':510, 'rnbits':384, 'deg_h_S':21,'cost_S':199, 'deg_h_C':7, 'cost_C':210, 'label':"-2^32+2^27-2^24+2^18+2^12-2^2 Hw2naf 6"},
    {'u':-0xf8fafffe, 'u_mod_7':1, 'b':16, 'pnbits':510, 'rnbits':384, 'deg_h_S':21,'cost_S':199, 'deg_h_C':7, 'cost_C':210, 'label':"-2^32+2^27-2^24+2^18+2^16+2 Hw2naf 6"},
    {'u':-0xf9f81080, 'u_mod_7':1, 'b':-2, 'pnbits':510, 'rnbits':384, 'deg_h_S':21,'cost_S':199, 'deg_h_C':7, 'cost_C':210, 'label':"-2^32+2^27-2^25+2^19-2^12-2^7 Hw2naf 6"},
    {'u': 0xf4ffff60, 'u_mod_7':1, 'b':-2, 'pnbits':510, 'rnbits':384, 'deg_h_S':21,'cost_S':199, 'deg_h_C':7, 'cost_C':210, 'label':"+2^32-2^28+2^26+2^24-2^7-2^5 Hw2naf 6"},
]

# BLS27 curves with sparse seed u = [1, 4] mod 6
# u % 9 == 1 allows to have p = 1 mod 9 as (px(3*x+1)/3-1).roots(GF(3)) gives root (0).
test_vector_sparse_bls27 = [
    {'u':  0x99a, 'u_mod_9':1, 'b':16, 'pnbits':224, 'rnbits':202, 'deg_h_S':27,'cost_S':200, 'deg_h_C':9, 'cost_C':210, 'label':"u=+2^11+2^9-2^7+2^5-2^3+2            Hw2NAF=6"},
    {'u':-0x20f0, 'u_mod_9':1, 'b':-2, 'pnbits':260, 'rnbits':234, 'deg_h_S':27,'cost_S':200, 'deg_h_C':9, 'cost_C':210, 'label':"u=-2^13-2^8+2^4                      Hw2NAF=3"},
    {'u':-0x297b, 'u_mod_9':1, 'b': 1, 'pnbits':266, 'rnbits':240, 'deg_h_S':27,'cost_S':200, 'deg_h_C':9, 'cost_C':210, 'label':"u=-2^13-2^11-2^9+2^7+2^2+1           Hw2NAF=6"},
    {'u':-0x39d4, 'u_mod_9':1, 'b': 2, 'pnbits':276, 'rnbits':248, 'deg_h_S':27,'cost_S':200, 'deg_h_C':9, 'cost_C':210, 'label':"u=-2^14+2^11-2^9+2^6-2^4-2^2         Hw2NAF=6"},
    {'u': 0x5e81, 'u_mod_9':1, 'b': 1, 'pnbits':290, 'rnbits':261, 'deg_h_S':27,'cost_S':200, 'deg_h_C':9, 'cost_C':210, 'label':"u=+2^15-2^13-2^9+2^7+1               Hw2NAF=5"},
    {'u': 0x6a24, 'u_mod_9':1, 'b': 2, 'pnbits':294, 'rnbits':264, 'deg_h_S':27,'cost_S':200, 'deg_h_C':9, 'cost_C':210, 'label':"u=+2^15-2^13+2^11+2^9+2^5+2^2        Hw2NAF=6"},
    {'u':-0x6c98, 'u_mod_9':1, 'b':-2, 'pnbits':294, 'rnbits':265, 'deg_h_S':27,'cost_S':200, 'deg_h_C':9, 'cost_C':210, 'label':"u=-2^15+2^12+2^10-2^7-2^5+2^3        Hw2NAF=6"},
    {'u': 0x74e6, 'u_mod_9':1, 'b': 2, 'pnbits':296, 'rnbits':267, 'deg_h_S':27,'cost_S':200, 'deg_h_C':9, 'cost_C':210, 'label':"u=+2^15-2^12+2^10+2^8-2^5+2^3-2      Hw2NAF=7"},
    {'u': 0x7c09, 'u_mod_9':1, 'b': 1, 'pnbits':298, 'rnbits':268, 'deg_h_S':27,'cost_S':200, 'deg_h_C':9, 'cost_C':210, 'label':"u=+2^15-2^10+2^3+1                   Hw2NAF=4"},
    {'u':-0x7e62, 'u_mod_9':1, 'b': 2, 'pnbits':299, 'rnbits':269, 'deg_h_S':27,'cost_S':200, 'deg_h_C':9, 'cost_C':210, 'label':"u=-2^15+2^9-2^7+2^5-2                Hw2NAF=5"},
    {'u': 0x89f5, 'u_mod_9':1, 'b': 1, 'pnbits':301, 'rnbits':271, 'deg_h_S':27,'cost_S':200, 'deg_h_C':9, 'cost_C':210, 'label':"u=+2^15+2^11+2^9-2^4+2^2+1           Hw2NAF=6"},
    {'u': 0x9202, 'u_mod_9':1, 'b':11, 'pnbits':303, 'rnbits':272, 'deg_h_S':27,'cost_S':200, 'deg_h_C':9, 'cost_C':210, 'label':"u=+2^15+2^12+2^9+2                   Hw2NAF=4"},
    {'u': 0xae4f, 'u_mod_9':1, 'b': 1, 'pnbits':308, 'rnbits':277, 'deg_h_S':27,'cost_S':200, 'deg_h_C':9, 'cost_C':210, 'label':"u=+2^16-2^14-2^12-2^9+2^6+2^4-1      Hw2NAF=7"},
    #
    {'u':-0x23a87e, 'u_mod_9':1, 'b':16, 'pnbits':422, 'rnbits':380, 'deg_h_S':27,'cost_S':200, 'deg_h_C':9, 'cost_C':210, 'label':"u=-2^21-2^18+2^15-2^13-2^11-2^7+2    Hw2NAF=7"},
    {'u':-0x23ff5d, 'u_mod_9':1, 'b': 1, 'pnbits':422, 'rnbits':380, 'deg_h_S':27,'cost_S':200, 'deg_h_C':9, 'cost_C':210, 'label':"u=-2^21-2^18+2^7+2^5+2^2-1           Hw2NAF=6"},
    {'u':-0x24062f, 'u_mod_9':1, 'b': 1, 'pnbits':422, 'rnbits':380, 'deg_h_S':27,'cost_S':200, 'deg_h_C':9, 'cost_C':210, 'label':"u=-2^21-2^18-2^11+2^9-2^6+2^4+1      Hw2NAF=7"},
    {'u':-0x253f7f, 'u_mod_9':1, 'b': 1, 'pnbits':423, 'rnbits':381, 'deg_h_S':27,'cost_S':200, 'deg_h_C':9, 'cost_C':210, 'label':"u=-2^21-2^18-2^16-2^14+2^7+1         Hw2NAF=6"},#16
    {'u':-0x26ee05, 'u_mod_9':1, 'b': 1, 'pnbits':425, 'rnbits':382, 'deg_h_S':27,'cost_S':200, 'deg_h_C':9, 'cost_C':210, 'label':"u=-2^21-2^19+2^16+2^12+2^9-2^2-1     Hw2NAF=7"},
    {'u': 0x27706c, 'u_mod_9':1, 'b': 2, 'pnbits':425, 'rnbits':382, 'deg_h_S':27,'cost_S':200, 'deg_h_C':9, 'cost_C':210, 'label':"u=+2^21+2^19-2^15-2^12+2^7-2^4-2^2   Hw2NAF=7"},
    {'u': 0x27a3e4, 'u_mod_9':1, 'b': 2, 'pnbits':425, 'rnbits':382, 'deg_h_S':27,'cost_S':200, 'deg_h_C':9, 'cost_C':210, 'label':"u=+2^21+2^19-2^15+2^13+2^10-2^5+2^2  Hw2NAF=7"},
    {'u': 0x27d390, 'u_mod_9':1, 'b':-2, 'pnbits':425, 'rnbits':383, 'deg_h_S':27,'cost_S':200, 'deg_h_C':9, 'cost_C':210, 'label':"u=+2^21+2^19-2^14+2^12+2^10-2^7+2^4  Hw2NAF=7"},
    {'u':-0x27de1a, 'u_mod_9':1, 'b': 2, 'pnbits':425, 'rnbits':383, 'deg_h_S':27,'cost_S':200, 'deg_h_C':9, 'cost_C':210, 'label':"u=-2^21-2^19+2^13+2^9-2^5+2^3-2      Hw2NAF=7"},
    {'u':-0x27f290, 'u_mod_9':1, 'b':-2, 'pnbits':425, 'rnbits':383, 'deg_h_S':27,'cost_S':200, 'deg_h_C':9, 'cost_C':210, 'label':"u=-2^21-2^19+2^12-2^9-2^7-2^4        Hw2NAF=6"},
    {'u': 0x280c7b, 'u_mod_9':1, 'b': 1, 'pnbits':425, 'rnbits':383, 'deg_h_S':27,'cost_S':200, 'deg_h_C':9, 'cost_C':210, 'label':"u=+2^21+2^19+2^12-2^10+2^7-2^2-1     Hw2NAF=7"},
    {'u':-0x287beb, 'u_mod_9':1, 'b': 1, 'pnbits':426, 'rnbits':383, 'deg_h_S':27,'cost_S':200, 'deg_h_C':9, 'cost_C':210, 'label':"u=-2^21-2^19-2^15+2^10+2^4+2^2+1     Hw2NAF=7"},# in paper
    {'u': 0x29bee8, 'u_mod_9':1, 'b':-2, 'pnbits':427, 'rnbits':384, 'deg_h_S':27,'cost_S':200, 'deg_h_C':9, 'cost_C':210, 'label':"u=+2^21+2^19+2^17-2^14-2^8-2^5+2^3   Hw2NAF=7"},
]

# FST64_k28 curves with sparse seed u = [1] mod 2 of 33--33 bits Hw2naf 5 and s.t. r has 384 to 384 bits
test_vector_sparse_fst64_k28 = [
    {'u': 0xfe00000f, 'u_mod_7':3, 'a':11, 'pnbits':510, 'rnbits':384, 'deg_h_S':14,'cost_S':208, 'deg_h_C': 7,'cost_C':226, 'label':"+2^32-2^25+2^4-1 Hw2naf 4"},
    {'u':-0xfffdef81, 'u_mod_7':2, 'a': 7, 'pnbits':510, 'rnbits':384, 'deg_h_S':14,'cost_S':208, 'deg_h_C': 7,'cost_C':226, 'label':"-2^32+2^17+2^12+2^7-1 Hw2naf 5"},
    {'u': 0xfffe4fff, 'u_mod_7':4, 'a': 5, 'pnbits':510, 'rnbits':384, 'deg_h_S':14,'cost_S':208, 'deg_h_C': 7,'cost_C':226, 'label':"+2^32-2^17+2^14+2^12-1 Hw2naf 5"},
    {'u': 0xfffc001b, 'u_mod_7':2, 'a':-2, 'pnbits':510, 'rnbits':384, 'deg_h_S':14,'cost_S':208, 'deg_h_C': 7,'cost_C':226, 'label':"+2^32-2^18+2^5-2^2-1 Hw2naf 5"},
    {'u': 0xffeffbf9, 'u_mod_7':5, 'a': 1, 'pnbits':510, 'rnbits':384, 'deg_h_S':14,'cost_S':208, 'deg_h_C': 7,'cost_C':226, 'label':"+2^32-2^20-2^10-2^3+1 Hw2naf 5"},
    {'u':-0xffdfdc01, 'u_mod_7':0, 'a':11, 'pnbits':510, 'rnbits':384, 'deg_h_S':14,'cost_S':208, 'deg_h_C': 7,'cost_C':226, 'label':"-2^32+2^21+2^13+2^10-1 Hw2naf 5"},
    {'u': 0xffe47fff, 'u_mod_7':4, 'a':23, 'pnbits':510, 'rnbits':384, 'deg_h_S':14,'cost_S':208, 'deg_h_C': 7,'cost_C':226, 'label':"+2^32-2^21+2^18+2^15-1 Hw2naf 5"},
    {'u': 0xff7f7f7f, 'u_mod_7':3, 'a':17, 'pnbits':510, 'rnbits':384, 'deg_h_S':14,'cost_S':208, 'deg_h_C': 7,'cost_C':226, 'label':"+2^32-2^23-2^15-2^7-1 Hw2naf 5"},
    {'u': 0xfe408001, 'u_mod_7':6, 'a': 1, 'pnbits':510, 'rnbits':384, 'deg_h_S':14,'cost_S':208, 'deg_h_C': 7,'cost_C':226, 'label':"+2^32-2^25+2^22+2^15+1 Hw2naf 5"},# in paper
    {'u': 0xfbffdffd, 'u_mod_7':2, 'a':-1, 'pnbits':510, 'rnbits':384, 'deg_h_S':14,'cost_S':208, 'deg_h_C': 7,'cost_C':226, 'label':"+2^32-2^26-2^13-2^2+1 Hw2naf 5"},
]
# KSS28 curves with seed u = [309, 449, 1759, 1899] mod 2030 s.t. r has 0 to 256 bits
test_vector_kss28i0 = [
    {'u':-0x250f9,  'u_mod_7':1, 'a': 7, 'pnbits':262,'rnbits':202, 'deg_h_S':None,'cost_S':None, 'label':"u=-2^17-2^14-2^12-2^8+2^3-1          Hw2NAF=6"},#0
    {'u': 0x52b33,  'u_mod_7':2, 'a': 1, 'pnbits':280,'rnbits':216, 'deg_h_S':None,'cost_S':None, 'label':"u=+2^18+2^16+2^14-2^12-2^10-2^8+2^6-2^4+2^2-1 Hw2NAF=10"},#0
    {'u':-0x133a95, 'u_mod_7':1, 'a': 1, 'pnbits':311,'rnbits':239, 'deg_h_S':None,'cost_S':None, 'label':"u=-2^20-2^18+2^16-2^14+2^11-2^9-2^7-2^4-2^2-1 Hw2NAF=10"},#1
    {'u':-0x14d1cf, 'u_mod_7':2, 'a':13, 'pnbits':313,'rnbits':240, 'deg_h_S':None,'cost_S':None, 'label':"u=-2^20-2^18-2^16+2^14-2^12-2^9+2^6-2^4+1 Hw2NAF=9"},#2
    {'u': 0x1c29d7, 'u_mod_7':1, 'a': 5, 'pnbits':320,'rnbits':245, 'deg_h_S':None,'cost_S':None, 'label':"u=+2^21-2^18+2^13+2^11+2^9-2^5-2^3-1 Hw2NAF=8"},#1
    {'u': 0x1c4903, 'u_mod_7':1, 'a': 1, 'pnbits':320,'rnbits':246, 'deg_h_S':None,'cost_S':None, 'label':"u=+2^21-2^18+2^14+2^11+2^8+2^2-1     Hw2NAF=7"},#2
    {'u': 0x1f701f, 'u_mod_7':2, 'a': 2, 'pnbits':322,'rnbits':247, 'deg_h_S':None,'cost_S':None, 'label':"u=+2^21-2^15-2^12+2^5-1              Hw2NAF=5"},#3
    {'u': 0x273679, 'u_mod_7':2, 'a': 5, 'pnbits':327,'rnbits':251, 'deg_h_S':None,'cost_S':None, 'label':"u=+2^21+2^19-2^16+2^14-2^11-2^9+2^7-2^3+1 Hw2NAF=9"},#4
    {'u': 0x336ac5, 'u_mod_7':2, 'a': 2, 'pnbits':333,'rnbits':256, 'deg_h_S':None,'cost_S':None, 'label':"u=+2^22-2^20+2^18-2^15-2^12-2^10-2^8-2^6+2^2+1 Hw2NAF=10"},#5
]
# KSS28 curves with sparse seed u = [309, 449, 1759, 1899] mod 2030 of 33--33 bits Hw2naf 7 and s.t. r has 380 to 384 bits
test_vector_sparse_kss28i0 = [
    {'u': 0xfdf80215,  'u_mod_7':1, 'a': 2, 'pnbits':498, 'rnbits':380, 'deg_h_S':28,'cost_S':247, 'deg_h_C': 7,'cost_C':223, 'label':"+2^32-2^25-2^19+2^9+2^4+2^2+1 Hw2naf 7"},
    {'u': 0x10408443f, 'u_mod_7':2, 'a': 2, 'pnbits':499, 'rnbits':380, 'deg_h_S':28,'cost_S':247, 'deg_h_C': 7,'cost_C':223, 'label':"+2^32+2^26+2^19+2^14+2^10+2^6-1 Hw2naf 7"},
    {'u':-0x10ff7fe09, 'u_mod_7':2, 'a': 9, 'pnbits':500, 'rnbits':381, 'deg_h_S':28,'cost_S':247, 'deg_h_C': 7,'cost_C':223, 'label':"-2^32-2^28+2^19+2^9-2^3-1 Hw2naf 6"},
    {'u':-0x11f00fd01, 'u_mod_7':2, 'a': 2, 'pnbits':501, 'rnbits':382, 'deg_h_S':28,'cost_S':247, 'deg_h_C': 7,'cost_C':223, 'label':"-2^32-2^29+2^24-2^16+2^10-2^8-1 Hw2naf 7"},
    {'u':-0x11feffe79, 'u_mod_7':2, 'a': 9, 'pnbits':501, 'rnbits':382, 'deg_h_S':28,'cost_S':247, 'deg_h_C': 7,'cost_C':223, 'label':"-2^32-2^29+2^20+2^9-2^7+2^3-1 Hw2naf 7"},
    {'u':-0x120fbfe21, 'u_mod_7':2, 'a': 2, 'pnbits':501, 'rnbits':382, 'deg_h_S':28,'cost_S':247, 'deg_h_C': 7,'cost_C':223, 'label':"-2^32-2^29-2^24+2^18+2^9-2^5-1 Hw2naf 7"},
    {'u':-0x133fdfffb, 'u_mod_7':2, 'a': 2, 'pnbits':503, 'rnbits':383, 'deg_h_S':28,'cost_S':247, 'deg_h_C': 7,'cost_C':223, 'label':"-2^32-2^30+2^28-2^26+2^17+2^2+1 Hw2naf 7"},
    {'u': 0x1407eff21, 'u_mod_7':1, 'a':13, 'pnbits':504, 'rnbits':384, 'deg_h_S':28,'cost_S':247, 'deg_h_C': 7,'cost_C':223, 'label':"+2^32+2^30+2^23-2^16-2^8+2^5+1 Hw2naf 7"},
    {'u':-0x148420007, 'u_mod_7':2, 'a':13, 'pnbits':504, 'rnbits':384, 'deg_h_S':28,'cost_S':247, 'deg_h_C': 7,'cost_C':223, 'label':"-2^32-2^30-2^27-2^22-2^17-2^3+1 Hw2naf 7"},
]
