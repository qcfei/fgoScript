
from PyQt5.QtWidgets import QLabel
import time

#日志设计
class Log():
    def __init__(self,la_log:QLabel):
        self.console_log:str='none'
        self.la_log:QLabel=la_log
        self.lineNum=1

    def log_update(self,text:str,):
        self.console_log=time.strftime('%H:%M:%S',time.localtime(time.time()))+'\t'+text+'\n'+self.console_log
        self.lineNum+=1
        # self.la_log.setFixedHeight((2*13-1)*self.lineNum)
        self.la_log.setText(self.console_log)

    def log_reset(self):
        self.console_log='none'
        # self.la_log.setFixedHeight(2*13-1)
        self.la_log.setText(self.console_log)
        self.lineNum=1

