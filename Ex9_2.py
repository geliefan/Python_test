# -*- coding: cp932 -*-
#ファイル
readfile = 'datafile.txt'
myfile = open('myfile.txt', 'w')
myfile.write('Hello tex file\n')
myfile.close()


#ファイルへのオブジェクトの保存，または元のオブジェクトへ変換
X,Y,Z = 43, 44, 45
S = 'spam'
D = {'a':1, 'b':2}
L = [1, 2, 3]

F = open('datafile.txt','w')
F.write(S + '\n')
F.write('%s,%s,%s\n' %(X,Y,Z))
F.write(str(L) + '$' + str(D) + '\n')
F.close()

byte = open('datafile.txt').read()
print byte

F = open('datafile.txt')
line = F.readline()
print line
print line.rstrip()
line = F.readline()
print line
parts = line.split(',')
print parts
numbers = [int(P) for P in parts] #リストの文字列を一度に変換
print numbers

#リスト，ディクショナリの変換方法
line = F.readline()
print line
parts = line.split('$')             #元のオブジェクトに変換
print eval(parts[0])
objects = [eval(P) for P in parts]  #すべてを変換
print objects

#pickleを使ってオブジェクトをそのままファイルに保存する
F = open(readfile,'w')
import pickle
pickle.dump(D,F)
F.close()
F = open(readfile)
E = pickle.load(F)
print E

#ファイルへのバイナリデータの保存
F = open('data.bin','wb')
import struct
bytes = struct.pack('>i4sh', 7, 'spam', 8)  #バイナリデータの作成
print bytes
F.write(bytes)
F.close()

F = open('data.bin','rb')
data = F.read()
print data
values = struct.unpack('>i4sh', data)
print values
