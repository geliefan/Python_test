# -*- coding: cp932 -*-

#任意のシーケンスを指定して、共通する要素を取り出す
def intersect(*args):
    res =[]
    for x in args[0]:                   # １つ目のシーケンスにアクセス
        for other in args[1:]:          # 他のすべてのシーケンスにアクセス
            if x not in other: break    # 共通要素がなければ終了
        else:
            res.append(x)               # あれば実行結果に追加
    return res

# 指定されたシーケンスのいずれかに含まれる要素をすべて取り出す
def union(*args):
    res = []
    for seq in args:            # すべてのシーケンスにアクセス
        for x in seq:           # すべての要素にアクセス
            if not x in res:    # 新たな要素が見つかれば実行結果に追加
                res.append(x)
    return res
