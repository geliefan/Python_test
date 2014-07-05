#10 Nest
Men = { 'Name':'',
        'Fast':'',
        'age':40,
        'job':'',
        'adress':'',
        'mail':'',
        'Tel':0120}
print Men

#11 File
S = open('myfile.txt','w')
S.write('Hello file world!')
S.close()

S = open('myfile.txt')
print S.read()
S.close()
