
from PyQt5.QtCore import QThread,QWaitCondition,QMutex
from PyQt5.QtWidgets import QLabel
from log import *

class CanPauseThread(QThread):

    def __init__(self,log:Log):
        super(CanPauseThread,self).__init__()
        
        self.console_log:Log=log

        self._isPause = False
        self._isRun= False
        self._value = 0
        self.cond = QWaitCondition()
        self.mutex = QMutex()

    def action(self):
        self.console_log.log_update('test test running '+str(self._isPause))
        time.sleep(0.6)

    def isQuit(self):
        return False

    def run(self):
        self._isRun= True
        while True:
            if not self._isRun or self.isQuit():
                break
            self.mutex.lock()       # 上锁
            if self._isPause:
                self.cond.wait(self.mutex)
            self.action()
            self.mutex.unlock()  # 解锁

    def pause(self):
        self._isPause = True
 
    def resume(self):
        self._isPause = False
        self.cond.wakeAll()

