#7.3 文字列フォーマット
exclamation = "Ni"
print("The kings who say %s!" % exclamation)
print("%d %s %d you " %(1,'spam', 4))
print("%s -- %s -- %s" %(42,3.14159, [1,2,3]))

#文字列フォーマットに使用するコード
x = 1234
res = "integers:...%d...%-6d...%06d" %(x,x,x)
print(res)
x = 1.23456789
print(x)
print('%e | %f | %g' % (x,x,x))

#ディクショナリを使用した文字列フォーマット
replay = """
Greetings...
Hello %(name)s!
Your age squared is %(age)s
"""
values = {'name':'Bob', 'age':40}
print(replay % values)

food = 'spam'
age = 40
print(vars())
print("%(age)d %(food)s" %vars())

#文字列のメソッド
S = 'xxxxSPAMxxxxSPAMxxxx'
where = S.find('SPAM')
print(where)
#S = S[:where] + 'BGGS' + S[(where+4):]
#print(S)
Sre = S.replace('SPAM','BGGS')
print(Sre)
Sre2 = S.replace('SPAM','EGGS',1)
print(Sre2)
S = 'spammy'
L = list(S)
print(L)
L[3] = 'x'
L[4] = 'x'
print(L)
S = ''.join(L)
print(S)

#文字列の分解
line = "aaa bbb ccc"
col1 = line[:3]
col2 = line[8:]
print(col1,col2)
col = line.split()
print(col)
