# -*- coding: cp932 -*-
#�t�@�C��
readfile = 'datafile.txt'
myfile = open('myfile.txt', 'w')
myfile.write('Hello tex file\n')
myfile.close()


#�t�@�C���ւ̃I�u�W�F�N�g�̕ۑ��C�܂��͌��̃I�u�W�F�N�g�֕ϊ�
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
numbers = [int(P) for P in parts] #���X�g�̕��������x�ɕϊ�
print numbers

#���X�g�C�f�B�N�V���i���̕ϊ����@
line = F.readline()
print line
parts = line.split('$')             #���̃I�u�W�F�N�g�ɕϊ�
print eval(parts[0])
objects = [eval(P) for P in parts]  #���ׂĂ�ϊ�
print objects

#pickle���g���ăI�u�W�F�N�g�����̂܂܃t�@�C���ɕۑ�����
F = open(readfile,'w')
import pickle
pickle.dump(D,F)
F.close()
F = open(readfile)
E = pickle.load(F)
print E

#�t�@�C���ւ̃o�C�i���f�[�^�̕ۑ�
F = open('data.bin','wb')
import struct
bytes = struct.pack('>i4sh', 7, 'spam', 8)  #�o�C�i���f�[�^�̍쐬
print bytes
F.write(bytes)
F.close()

F = open('data.bin','rb')
data = F.read()
print data
values = struct.unpack('>i4sh', data)
print values
