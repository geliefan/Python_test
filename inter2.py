# -*- coding: cp932 -*-

#�C�ӂ̃V�[�P���X���w�肵�āA���ʂ���v�f�����o��
def intersect(*args):
    res =[]
    for x in args[0]:                   # �P�ڂ̃V�[�P���X�ɃA�N�Z�X
        for other in args[1:]:          # ���̂��ׂẴV�[�P���X�ɃA�N�Z�X
            if x not in other: break    # ���ʗv�f���Ȃ���ΏI��
        else:
            res.append(x)               # ����Ύ��s���ʂɒǉ�
    return res

# �w�肳�ꂽ�V�[�P���X�̂����ꂩ�Ɋ܂܂��v�f�����ׂĎ��o��
def union(*args):
    res = []
    for seq in args:            # ���ׂẴV�[�P���X�ɃA�N�Z�X
        for x in seq:           # ���ׂĂ̗v�f�ɃA�N�Z�X
            if not x in res:    # �V���ȗv�f��������Ύ��s���ʂɒǉ�
                res.append(x)
    return res
