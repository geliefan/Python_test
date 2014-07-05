# -*- coding: cp932 -*-
#比較とブール値
L1 = [1, ('a',3)]
L2 = [1, ('a',3)]
print L1==L2, L1 is L2

S1 = 'spam'
S2 = 'spam'
print S1 == S2, S1 is S2

S1 = 'This is a longer string. tomorrow never die is the most interesting movies'
S2 = 'This is a longer string. tomorrow never die is the most interesting movies'
print S1 == S2, S1 is S2

L2 = [1, ('a',2)]
print L1 < L2, L1 == L2, L1 > L2
