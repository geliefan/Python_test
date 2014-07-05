# -*- coding: cp932 -*-
#�P�V�́@�֐��Ɋ֘A���鍂�x�ȃe�N�j�b�N

#lambda��
# def���Ƃ̔�r
def func(x, y, z): return x+y+z
print func(2,3,4)

# lambda��
x = (lambda a="fee",b="fie",c="foe": a+b+c)
print x("wee")

# �X�R�[�v
def knights():
    title = 'Sir'
    action = (lambda x: title + ' ' + x)
    return action
act = knights()
print act('robin')

# lambda���̓���
L = [(lambda x : x **2),(lambda x: x**3), (lambda x: x**4)]
for f in L:
    print f(2),
print
print L[0](3)

#�X�e�[�g�����g�����ɏ�������
''' �ȉ��̃X�e�[�g�����g������
if a:
    b
else:
    c
�͎��̎��Ɠ���
b if a else c
��
((a and b) or c)
'''
lower = (lambda x,y: x if x<y else y)
print lower('bb','aa')
print lower('aa','bb')

# ���[�v���K�v�ȏꍇ�́Amap�֐��̌Ăяo���⃊�X�g����\�L�𖄂ߍ���
import sys
showall = (lambda x: map(sys.stdout.write, x))
t = showall(['spam\n', 'toast\n', 'eggs\n'])
showall = lambda x: [sys.stdout.write(line) for line in x]
t = showall(('spam\n', 'side\n', 'of\n', 'life\n'))

# lambda���ƃl�X�g�X�R�[�v
def action(x):
    return (lambda y: y+x)
act = action(99)
print act
print act(2)

action = (lambda x: (lambda y: y+x))
act = action(99)
print act(3)
print ((lambda x: (lambda y: x+y))(99))(4)

# 17.3 map�֐�
#�@�X�̗v�f�ɂ��ē������������ɂ�
#�@����܂�
counters = [1,2,3,4]
update = []
for x in counters:
    update.append(x)
print update
#�@map�֐��́A��P�����Ɏw�肳�ꂽ�֐����A���̌�Ɏw�肳�ꂽ�V�[�P���X�̌X�ɗv�f�ɓK�p����
def inc(x): return x+10
print map(inc,counters)

print map((lambda x: x+3), counters)      #lambda�����g�p

print pow(3,4)
print map(pow, [1,2,3], [2,3,4])

#17.4 map�֐��Ɨގ������֐��Ffilter��reduce

print filter((lambda x: x>0), range(-5,5))
res = []
for x in range(-5,5):
    if x > 0:
        res.append(x)
print res

# reduce�֐�
print reduce((lambda x,y: x+y), [1,2,3,4])
print reduce((lambda x,y: x*y), [1,2,3,4])

L = [1,2,3,4]
res = L[0]
for x in L[1:]:
    res = res + x
print res

#17.5 ���X�g����\�L
# example
res = []
for x in 'spam':
    res.append(ord(x))
print res
res = map(ord,'spam')
print res
# ���X�g����\�L
res = [ord(x) for x in 'spam']
print res
print [x ** 2 for x in range(10)]
# ���X�g���\�L�Ŏg�p���郋�[�v��if
print [x for x in range(5) if x % 2 ==0]

