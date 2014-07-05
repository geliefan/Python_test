def minimax(test, *args):
    res = args[0]
    for arg in args[1:]:
        if test(arg, res):
            res = arg
    return res

def lessthan(x,y): return x < y
def grtrthan(x,y): return x > y

"""
print minimax(lessthan, 4,2,1,5,6,3)
print minimax(grtrthan, 4,2,1,5,6,3)
"""
