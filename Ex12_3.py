# -*- coding: cp932 -*-
#12.3 Python�̃u�[�����Z

#ture: not 0, not null object
#false: 0, null object,None

print 2 < 3, 3<2
print 2 or 3, 3 or 2, 2 and 3
print [] or 3, 0 or 1
print [] or {}

#if/else��
A = 't' if 'spam' else 'f'
print A
A = 't' if '' else 'f'
print A

print ['f','t'][bool('')]
print ['f','t'][bool('spam')]
