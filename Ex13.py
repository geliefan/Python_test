# -*- coding: cp932 -*-

x = 'spam'
while x:
    print x,
    x = x[1:]
print

a =0; b=10
while a<b:
    print a,
    a +=1
print

#continue
x = 10
while x:
    x = x-1
    if x % 2 != 0: continue
    print x,
print

#beak
'''
while 1:
    name = raw_input('Enter name:')
    if name == 'stop': break
    age = raw_input('Enter age:')
    print 'Hello', name, '=>', int(age) **2
'''
#else
y = 31
x = y /2
while x > 1:
    if y % x ==0:
        print y, 'has factor', x
        break
    x = x-1
else:
    print y, 'is prime'
print

'''
x = 12
found = False
while x and not found:
    if match(x[0]):     #リストの先頭に値があるか？
        print 'Ni'
        found = True
    else:
        x = x[1:]
if not found:
    print 'not found'
'''

# 13.3.1 for statement format
'''
    for <target> in <object>:
        <statement>
        if <test>: break
        if <test>: continue
    else:
        <statement>
'''
for x in ["spam", "eggs", "ham"]:
    print x,
print

sum = 0
for x in [1,2,3,4]:
    sum += x
print sum

#sequens except list
s = 'luberjack'
t = ('and', "I'm", "okey")
for x in s: print x,
print
for x in t: print x,
print

T = [(1,2), (3,4), (5,6)]
for (a,b) in T:
    print a,b
print

#nest of for loop
items = ['aaa', 111, (4,5), 2.01]
tests = [(4,5), 3.14]
for key in tests:
    for item in items:
        if item == key:
            print key, "was found"
            break
    else:
        print key, "not dound!"
for key in tests:
    if key in items:
        print key,'was found'
    else:
        print key,'not found'

seq1 = 'spam'
seq2 = 'scam'
res = []
for x in seq1:
    if x in seq2:
        res.append(x)
print res

''' read data from File 
file = open('abstract2.txt')
for line in file.readlines():
    print line
for line in file.xreadlines():
    print line
for line in file:
    print line
'''

#13.4 iterative processing
for x in [1,2,3,4]: print x ** 2,
print
for x in (1,2,3,4): print x ** 3,
print
for x in 'spam': print x * 2,
print '\n'

#13.4.1 iterative processing to File
f = open('Ex_7_1.py')
print f.next()
print f.next()
adds = '*****************************'
print adds

for line in open('Ex_7_1.py'):
    print line.upper(),
print adds

#13.4.2 iterative processing for other object
L = {1,2,3}
I = iter(L)
print I.next()
print I.next()
print adds

D = {'a':1, 'b':2, 'c':3}
for key in D:
    print key, D[key]
print adds

# 13.4.3 iterative processing except for loop
uppers = [line.upper() for line in open('Ex_7_1.py')]
print uppers
print adds
print map(str.upper, open('Ex_7_1.py'))
print adds

print sorted(open('Ex_7_1.py'))
print adds

# 13.5 special for loop
# 13.5.1 use range
X = 'spam'
for i in range(len(X)): print X[i],
print
print adds
# 13.5.4 use zip function
L1 = [1,2,3,4]
L2 = [5,6,7,8]
print zip(L1,L2)
print adds
for (x,y) in zip(L1,L2):
    print x, y, '--', x+y
print adds
S1 = 'spam'
S2 = 'xyz123'
print zip(S1,S2)
print map(None,S1,S2)
print adds

keys = ['spam', 'eggs', 'toast']
vals = [1,3,5]
D3 = dict(zip(keys,vals))
print D3
print adds

# 13.5.5 generating index and element : enumerate function
# until now
S = 'spam'
offset = 0
for item in S:
    print item, 'appears at offset', offset
    offset += 1
print adds
#now
for (offset, item) in enumerate(S):
    print item, 'appears at offset', offset
print adds

# 13.6 リスト内包表記
f = open('Ex9_6.py')
lines = [line.rstrip() for line in f]
print lines
print adds
#Extend syntax of list~
f = open('Ex9_6.py')
lines = [line.rstrip() for line in f if line[0] == 'p']
print lines
print adds
