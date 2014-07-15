# -*- coding: cp932 -*-
import types

def status(module):
    print 'reloading', module.__name__

def transitive_reload(module, visited):
    if not visited.has_key(module):                 # �����[�h�ς݂łȂ����m�F
        status(module)                              # �w��̃��W���[���������[�h���C
        reload(module)                              # ����Ƀ����[�h�Ώۂ�T��
        visited[module] = None
        for attrobj in module.__dict__.values():    # ���ׂĂ̑����̃A�N�Z�X
            if type(attrobj) == types.ModuleType:   # ���������W���[���Ȃ�
                transitive_reload(attrobj, visited) # �������g���Ăяo��

def reload_all(*args):
    visited = {}
    for arg in args:
        if type(arg) == types.ModuleType:
            transitive_reload(arg, visited)

if __name__ == '__main__':
    import reloadall
    reload_all(reloadall)   
