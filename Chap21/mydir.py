# -*- coding: cp932 -*-
verbose = 1

def listing(module):
    if verbose:
        print "-"*30
        print "name:", module.__name__, "file:", module.__file__
        print "-"*30

    count = 0
    for attr in module.__dict__.keys():     # 名前空間の内容を調べる
        print "%02d) %s" % (count, attr),
        if attr[0:2] == "__":
            print "<built-in name>"         # ビルトイン属性の出力
        else:
            print getattr(module, attr)     # .__dict__[attr]と同等
        count = count+1

    if verbose:
        print "-"*30
        print module.__name__, "has %d names" % count
        print "-"*30

if __name__ == "__main__":
    import mydir
    listing(mydir)                          # 自らを引数にしてlisting関数を呼び出す
