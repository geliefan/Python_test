# -*- coding: cp932 -*-
import types

def status(module):
    print 'reloading', module.__name__

def transitive_reload(module, visited):
    if not visited.has_key(module):                 # リロード済みでないか確認
        status(module)                              # 指定のモジュールをリロードし，
        reload(module)                              # さらにリロード対象を探す
        visited[module] = None
        for attrobj in module.__dict__.values():    # すべての属性のアクセス
            if type(attrobj) == types.ModuleType:   # 属性がモジュールなら
                transitive_reload(attrobj, visited) # 自分自身を呼び出す

def reload_all(*args):
    visited = {}
    for arg in args:
        if type(arg) == types.ModuleType:
            transitive_reload(arg, visited)

if __name__ == '__main__':
    import reloadall
    reload_all(reloadall)   
