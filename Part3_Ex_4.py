L = [1,2,4,8,16,32,64]
X = 5

for x in L:
    if 2 ** X == x:
        print 'at index', L.index(x)
        break
else:
    print X, 'not found'

# c
L = [1,2,4,8,16,32,64]
X = 5

if 2 ** X in L:
    print 'at index', L.index(2 ** X)
else:
    print X, 'not found'

# d
L=[]
for x in range(10):
    L.append(2 ** x)
X = 5

if 2 ** X in L:
    print 'at index', L.index(2 ** X)
else:
    print X, 'not found'
