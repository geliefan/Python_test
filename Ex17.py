# -*- coding: cp932 -*-
#１７章　関数に関連する高度なテクニック

#lambda式
# def式との比較
def func(x, y, z): return x+y+z
print func(2,3,4)

# lambda式
x = (lambda a="fee",b="fie",c="foe": a+b+c)
print x("wee")

# スコープ
def knights():
    title = 'Sir'
    action = (lambda x: title + ' ' + x)
    return action
act = knights()
print act('robin')

# lambda式の特徴
L = [(lambda x : x **2),(lambda x: x**3), (lambda x: x**4)]
for f in L:
    print f(2),
print
print L[0](3)

#ステートメントを式に書き直す
''' 以下のステートメントを検討
if a:
    b
else:
    c
は次の式と同等
b if a else c
→
((a and b) or c)
'''
lower = (lambda x,y: x if x<y else y)
print lower('bb','aa')
print lower('aa','bb')

# ループが必要な場合は、map関数の呼び出しやリスト内包表記を埋め込む
import sys
showall = (lambda x: map(sys.stdout.write, x))
t = showall(['spam\n', 'toast\n', 'eggs\n'])
showall = lambda x: [sys.stdout.write(line) for line in x]
t = showall(('spam\n', 'side\n', 'of\n', 'life\n'))

# lambda式とネストスコープ
def action(x):
    return (lambda y: y+x)
act = action(99)
print act
print act(2)

action = (lambda x: (lambda y: y+x))
act = action(99)
print act(3)
print ((lambda x: (lambda y: x+y))(99))(4)

# 17.3 map関数
#　個々の要素について同じ操作をするには
#　これまで
counters = [1,2,3,4]
update = []
for x in counters:
    update.append(x)
print update
#　map関数は、第１引数に指定された関数を、その後に指定されたシーケンスの個々に要素に適用する
def inc(x): return x+10
print map(inc,counters)

print map((lambda x: x+3), counters)      #lambda式を使用

print pow(3,4)
print map(pow, [1,2,3], [2,3,4])

#17.4 map関数と類似した関数：filterとreduce

print filter((lambda x: x>0), range(-5,5))
res = []
for x in range(-5,5):
    if x > 0:
        res.append(x)
print res

# reduce関数
print reduce((lambda x,y: x+y), [1,2,3,4])
print reduce((lambda x,y: x*y), [1,2,3,4])

L = [1,2,3,4]
res = L[0]
for x in L[1:]:
    res = res + x
print res

#17.5 リスト内包表記
# example
res = []
for x in 'spam':
    res.append(ord(x))
print res
res = map(ord,'spam')
print res
# リスト内包表記
res = [ord(x) for x in 'spam']
print res
print [x ** 2 for x in range(10)]
# リスト内表記で使用するループとif
print [x for x in range(5) if x % 2 ==0]

