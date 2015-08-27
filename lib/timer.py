# coding: utf-8

import threading,time

class Timer(threading.Thread):
    def __init__(self,sleep,fn,args=(),lastDo=True):
        threading.Thread.__init__(self)
        self.fn = fn
        self.args = args
        self.sleep = sleep
        self.lastDo = lastDo
        self.setDaemon(True)

        self.isPlay = True
        self.fnPlay = False

    def __do(self):
        self.fnPlay = True
        apply(self.fn,self.args)
        self.fnPlay = False
        if self.lastDo == False:
            self.stop()

    def run(self):
        while self.isPlay :
            time.sleep(self.sleep)
            self.__do()

    def stop(self):
        #stop the loop
        self.isPlay = False
        while True:
            if not self.fnPlay : break
            time.sleep(0.01)
        #if lastDo,do it again
        if self.lastDo : self.__do()
