# -*- coding: cp932 -*-
'''
ジェネレータの例
'''
def gensquares(N):
    for i in range(N):
        yield i ** 2

for i in gensquares(5):
    print i, ':',
print

'''
関数で同様の処理を作成
'''
def buildsquares(n):
    res = []
    for i in range(n): res.append(i**2)
    return res
for x in buildsquares(5):
    print x,':',
print

'''
その他の方法
'''
for x in [n**2 for n in range(5)]:
    print x, ':',
print

for x in map((lambda x:x**2),range(5)):
    print x, ':',
print

# 17.6.3 いてれーたとビルトイン型
D ={'a':1,'b':2, 'c':3}
x = iter(D)
print x.next()
print x.next()

for key in D:
    print key,D[key],
print

# ジェネレータ式：イレテータとリスト内包表記の融合
print [x**2 for x in range(4)] #　リスト内包表記：リストを作る
print (x**2 for x in range(4)) #　ジェネレータ式：反復処理可能なオブジェクトを作る
G = (x**2 for x in range(4))
print G.next()
print G.next()  #acctualy not use next() method cause it used in for statement

for num in (x**2 for x in range(4)):
    print '%s, %s' % (num, num / 2.0)

print sorted(x ** 2 for x in range(4))
print sorted((x**2 for x in range(4)), reverse = True)
import math
print map(math.sqrt, (x**2 for x in range(4)))

# 17.8.1
def echo(message):
    print message

x = echo
x("Hello world")

def indirect(func, arg):
    func(arg)
indirect(echo, 'Hello jello!')

schedule = [(echo, 'Spam'), (echo, 'Ham!')]
for (func, arg) in schedule:
    func(arg)

X = 99
def selector(): # Xには関数内では値が代入されない
    print X     # Xはグローバルスコープの変数とみなされる
selector()

# 17.9.2
def saver(x=[]):
    x.append(1)
    print x
saver([2])
saver()
saver()
saver()
saver([3])
saver()
