#coding: utf-8
import sys,getopt

def Singleton(cls, *args, **kw):
    instances = {}
    def _Singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _Singleton

def commandLineParams(name):
    params = {}
    opts,args = getopt.getopt(sys.argv[1:],"r:c:",['runmode=','command='])
    for k,v in opts:
        k=k.replace('--','').replace('-','')
        params[k] = v
    if params.has_key(name):
        return params[name]
    return None


ENV = commandLineParams('runmode')

if ENV == None:
    Env = commandLineParams('r')

if ENV == None:
    ENV = 'develop'

CMD = None

if commandLineParams('c'):
    CMD = commandLineParams('c')

if commandLineParams('command'):
    CMD = commandLineParams('command')

from lib.timer import Timer
from lib.actions import ActionsManager
from lib.logger import Logger
