# -*- coding: cp932 -*-
# 引数のバリエーションの応用例
def min1(*args):
    res = args[0]
    for arg in args[1:]:
        if arg < res:
            res = arg
    return res

def min2(first, *rest):
    for args in rest:
        if args < first:
            first = args
    return first

def min3(*args):
    tmp = list(args)
    tmp.sort()
    return tmp[0]

print min1(3,4,1,2)
print min2("bb","aa")
print min3([2,2],[1,1],[3,3])
