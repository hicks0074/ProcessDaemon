# coding: utf-8

from lib import Singleton
from lib import Timer

@Singleton
class ActionsManager(object):
    def __init__(self):
        self.actions = {}
    def regiest(self,actionName,module,args={}):
        self.actions[actionName] = (module,args)
    def unregist(self,actionName):
        self.actions.pop(actionName)
    def getEvents(self):
        return self.actions
    def run(self):
        for act in self.actions:
            try:
                module = None
                act = self.actions[act]
                act = act[0]
                actionName = act['actionName']
                module = __import__('actions')
                action = getattr(module,actionName)()
                Timer(act['time'],action.run,act['args'],act['loop']).run()
            except e:
                print e
