# -*- coding: cp932 -*-
#10.3 �ȒP�ȃX�e�[�g�����g�̗�

#���[�v
while True:
    reply = raw_input('Enter text:')
    if reply == 'stop':
        break
    try:
        num = int(reply)
    except:
        print 'Bad!' *8
    else:
        print num **2
print 'Bye'
