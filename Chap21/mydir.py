# -*- coding: cp932 -*-
verbose = 1

def listing(module):
    if verbose:
        print "-"*30
        print "name:", module.__name__, "file:", module.__file__
        print "-"*30

    count = 0
    for attr in module.__dict__.keys():     # ���O��Ԃ̓��e�𒲂ׂ�
        print "%02d) %s" % (count, attr),
        if attr[0:2] == "__":
            print "<built-in name>"         # �r���g�C�������̏o��
        else:
            print getattr(module, attr)     # .__dict__[attr]�Ɠ���
        count = count+1

    if verbose:
        print "-"*30
        print module.__name__, "has %d names" % count
        print "-"*30

if __name__ == "__main__":
    import mydir
    listing(mydir)                          # ����������ɂ���listing�֐����Ăяo��
