# coding: utf-8

from lib import ENV

module = __import__('config.' + ENV , globals=None, locals=None, fromlist=('Config'), level=0)

conf = getattr(module,'Config')

if isinstance(conf,dict):
    conf['logging'] = {}
    conf['logging']['tag'] = 'ProcessDaemon'

def dictToObject(d):
    class _O: pass
    [setattr(_O, _k, d[_k]) for _k in d]
    return _O

Config = dictToObject(conf)
