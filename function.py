# -*- coding: cp932 -*-
#�l�X�Ȋ֐��̕ۊǏꏊ

def intersect(seq1,seq2):
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res

# global scope
X = 99          # �g�b�v���x���ő�����s���Ă���X��func�̓O���[�o��

def func(Y):    # �֐����ő�����s���Ă���Y,Z�̓��[�J��
    # local scope
    Z = X + Y   # X�̓O���[�o��
    return Z

print func(1)   #func�̓O���[�o���Ȃ̂ŁA���s���ʂƂ��ĂP�O�O��������

# �O���[�o���ϐ��ƃ��[�J���ϐ��̈���
X = 88          #�O���[�o���ϐ�

def func1():
    X = 99
    print X     # ���[�J���ϐ��F�O���[�o���ϐ��Ƃ͕ʕ�

func1()
print X         # �l�͕ς���ĂȂ��̂�88�Əo�͂����

# 16.2 global statement
X = 88

def func():
    global X
    X = 99
    print X
func()
print X
print

y , z = 1, 2
def all_global():
    global x
    x = y + z
    print x
all_global()
print x
print

# �l�X�g�X�R�[�v�����R�[�h�̗�
def f1():
    x = 88
    def f2():
        print x
    return f2

action = f1()
action()

def maker(N):
    def action(X):
        return X ** N
    return action

def funcl():
    x = 4
    action = (lambda n : x ** n)
    return action
x = funcl()
print x(2)
