#8章　リストとディクショナリ
print("------%s-------" %"8.2.1")
print(len([1,2,3]))
print([1,2,3]+[4,5,6])
print(['Ni!'] * 4)
print(3 in [1,2,3])
for x in [1,2,3]: print(x)

print("------%s-------" %"8.2.2")
L = ['spam', 'Spam', 'SPAM']
print(L[2])
print(L[-2])
print(L[1:])
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix[1])
print(matrix[1][1])

print("------%s-------" %"8.2.3")
print(L)
L[1] = 'eggs'
print(L)
L[0:2] = ["eat","more"]
print(L)
L.append("please")
print(L)
L.sort()
print(L)

print("------%s-------" %"8.2.3")
L = [1,2]
print(L.extend([3,4,5]))
print(L)
print(L.pop())
print(L)
print(L.reverse())
print(L)
L = []
L.append(1)
L.append(2)
print(L)
L.pop()
print(L)

print("------%s-------" %"8.4.1")
d2 = {"spam":2, "ham":1, "eggs":3}
print(d2["spam"])
print(d2)
print(len(d2))
#d2.has_key("ham") #python3系では存在しない。
print("ham" in d2)
D = d2.keys()
print(D)

print("------%s-------" %"8.4.2")
d2["ham"] = ["girl!","bake","fry"]
print(d2)
del d2["eggs"]
print(d2)
d2["brunch"] = "Bacon"
print(d2)
d3 = {"toast":4, "muffin":5}
d2.update(d3)
print(d2)

print("------%s-------" %"8.4.4")
table = {'Python':  'Guido van Rossum',
         'Perl':    'Larry Wall',
         'Tcl':     'John Ousterhout'}
language = 'Python'
creator = table[language]
print(creator)
for lang in table.keys():
    print(lang, '\t', table[lang])
    
print("------%s-------" %"8.4.5")
Matrix = {}
Matrix[(2,3,4)] = 88
Matrix[(7,8,9)] = 99
X = 2; Y = 3; Z =4
print(Matrix[(X,Y,Z)])
print(Matrix)
try:
    print(Matrix[(2,3,6)])
except KeyError:
    print(0)
print(Matrix.get((2,3,4),0))
print(Matrix.get((2,3,6),0))

rec = {}
rec['name'] = 'mel'
rec['age'] = '41'
rec['job'] = 'trainer/writer'
print(rec['name'])

mel = {'name':  'Merk',
       'jobs':  ['trainer','writer'],
       'web':   'www.rmi.net/~lutz',
       'home':  {'state': 'CO', 'zip':80513}}
print(mel['name'])
print(mel['jobs'])
print(mel['jobs'][1])
print(mel['home']['zip'])

