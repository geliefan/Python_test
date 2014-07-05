# -*- coding: cp932 -*-
#様々な関数の保管場所

def intersect(seq1,seq2):
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res

# global scope
X = 99          # トップレベルで代入が行われているXとfuncはグローバル

def func(Y):    # 関数内で代入が行われているY,Zはローカル
    # local scope
    Z = X + Y   # Xはグローバル
    return Z

print func(1)   #funcはグローバルなので、実行結果として１００が得られる

# グローバル変数とローカル変数の扱い
X = 88          #グローバル変数

def func1():
    X = 99
    print X     # ローカル変数：グローバル変数とは別物

func1()
print X         # 値は変わってないので88と出力される

# 16.2 global statement
X = 88

def func():
    global X
    X = 99
    print X
func()
print X
print

y , z = 1, 2
def all_global():
    global x
    x = y + z
    print x
all_global()
print x
print

# ネストスコープをもつコードの例
def f1():
    x = 88
    def f2():
        print x
    return f2

action = f1()
action()

def maker(N):
    def action(X):
        return X ** N
    return action

def funcl():
    x = 4
    action = (lambda n : x ** n)
    return action
x = funcl()
print x(2)
