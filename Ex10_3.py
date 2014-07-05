# -*- coding: cp932 -*-
#10.3 簡単なステートメントの例

#ループ
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
