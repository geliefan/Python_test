#Part 3 summarizes exercises

#Sort Dictionary
D = {"spamn":"nya", "is":"frends", "tasetless":"week", "no":"ared"}
D1 = D.copy()
print D
keys = D.keys()
keys.sort()
print keys
for key in keys:
    print key, '=>' ,D[key]
print
#now Python do this
for key in sorted(D):
    print key, '=>', D[key]
print

#sort by value
for key,value in sorted(D.items(), key = lambda x:x[1]):
    print key ,'=>', value
print
