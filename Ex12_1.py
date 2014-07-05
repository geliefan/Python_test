# -*- coding: cp932 -*-
#12.1 if statement

x = 'killer rabit'
if x == 'rogger':
    print "how's jessica?"
elif x == 'bugs':
    print "what's up doc?"
else:
    print 'Run away! Run away!'

choice = 'ham'
print {'spam':  1.25,
       'ham':   1.99,
       'eggs':  0.99,
       'bacon': 1.10}[choice]

branch = {'spam':   1.25,
          'ham':    1.99,
          'eggs':   0.99}
print branch.get('spam', 'Bad coice')
print branch.get('bacon','Bad choice')

#ブロックの区切り
x = 1
if x:
    y = 2
    if y:
        print 'block2'
    print 'block1'
print 'block0'
