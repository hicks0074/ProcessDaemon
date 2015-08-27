# !/usr/bin/env python
# coding: utf-8

from config import Config
from lib import ActionsManager
from lib.daemonize import Daemonize
from lib import CMD
from lib import Logger
import os

PID_FILE = os.path.join(os.getcwd(),'process.pid')

def main():
    Logger().log('enter main function')
    actions = Config.actions
    for actionName  in actions:
        ActionsManager().regiest(actionName,actions[actionName])
    ActionsManager().run()

if __name__ == '__main__':
    daemon = Daemonize(app='ProcessDaemon',pid=PID_FILE,action=main)
    if CMD == 'start':
        Logger().log('start daemon')
        daemon.start()
    elif CMD == 'stop':
        Logger().log('stop daemon')
        daemon.exit()
    else:
        print """ProcessDaemon:
        useage: python entry.py -c start -r production
            -c --command start stop : start or stop process daemon
            -r --runmode develop testing production : set run mode
        """
