#Part 3 summarizes exercises

#1 make easy code of loop
S = raw_input("Change ASCII:")
N = []
y =0
for x in S:
    y += ord(x)
    N.append(ord(x))
    print ord(x),
print
print y
print map(ord,S)
print N

#2 backslash
for i in range(50):
    print 'hello %d\n\t' % i
