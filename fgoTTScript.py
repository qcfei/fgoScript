'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-02-28 17:59:27
LastEditors: jk 1875809993@qq.com
LastEditTime: 2023-03-13 07:17:54
FilePath: \projectp\set_win.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# ⠀⠰⢷⢿⠄ 
# ⠀⠀⠀⠀⠀⣼⣷⣄ 
# ⠀⠀⣤⣿⣇⣿⣿⣧⣿⡄ 
# ⢴⠾⠋⠀⠀⠻⣿⣷⣿⣿⡀ 
# ○ ⠀⢀⣿⣿⡿⢿⠈⣿ 
# ⠀⠀⠀⢠⣿⡿⠁⠀⡊⠀⠙ 
# ⠀⠀⠀⢿⣿⠀⠀⠹⣿ 
# ⠀⠀⠀⠀⠹⣷⡀⠀⣿⡄ 
# ⠀⠀⠀⠀⣀⣼⣿⠀⢈⣧.

# contect:
# TabWidget_set            <------------------------------------------------------thread_update <-----------┐
# │                                                                                                         │
# ├─ Widget_run(vbox)      <------------------------------------------------------thread_reset              │
# │        ├─   <-----------------------------------------------------------------thread_skill_test         │
# │        ├─   <-----------------------------------------------------------------thread_order_test         │
# │        ├─   <-----------------------------------------------------------------thread_test <-------------┼---┐
# │        ├─ -- hBox_description                                                                           │   │
# │        │            └─ -- la_mnq                                                                        │   │
# │        │            ├─ -- la_state                                                                      │   │
# │        │            └─ -- la_neighborState                                                              │   │
# │        ├─ -- hBox_screen                                                                                │   │
# │        │            ├─ -- la_screen                                                                     │   │
# │        │            └─ -- splitter_log(vertical)                                                        │   │
# │        │                        ├─ -- la_time                                                           │   │
# │        │                        └─ -- scroll_log -- --la_log                                            │   │
# │        ├─ -- hbox_testBtn                                                                               │   │
# │        │            ├─ -- btn_reset                                                                     │   │
# │        │            ├─ -- btn_skill_test                                                                │   │
# │        │            ├─ -- btn_order_test                                                                │   │
# │        │            ├─ -- btn_test                                                                      │   │
# │        │            └─ -- btn_reset_state                                                               │   │
# │        └─ -- hbox_switch                                                                                │   │
# │                     ├─ -- btn_connect_start------------------------------------------------------------>┤   │
# │                     ├─ -- btn_connect_stop------------------------------------------------------------->┘   │
# │                     ├─ -- btn_script_start----------------------------------------------------------------->┤
# │                     └─ -- btn_script_stop------------------------------------------------------------------>┘
# ├─ Widget_set(hbox)
# │        ├─ -- setTitle_list(vbox)
# │        │            ├─ -- la_3T策略
# │        │            ├─ -- la_助战
# │        │            ├─ -- la_模拟器选择
# │        └─ -- scrollArea_setting(splitter vertival)
# │                     ├─ -- groupBox_strategy(vbox)
# │                     │           ├─ -- vbox_turn_lst[0-2]
# │                     │           │       ├─ -- label_turnIdx
# │                     │           │       ├─ -- le_skill_check
# │                     │           │       └─ -- le_order_check
# │                     │           └─ -- btn_update
# │                     ├─ -- groupBox_assist
# │                     │           └─ -- hbox_assist_lst[0-2]
# │                     │                   ├─ -- la_img_servant
# │                     │                   ├─ -- la_img_cloth
# │                     │                   └─ -- btn_update
# │                     └─ -- groupBox_mnq
# │                                 ├─ -- cbb_mnq
# │                                 ├─ -- btn_mnq_connect_test
# │                                 └─ -- la_test_result

import os
import cv2
import subprocess
from PyQt5.QtCore import Qt,QThread,QWaitCondition,QMutex
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from math import *
import numpy as np
import time
import socket
import struct
from collections import OrderedDict
import json
import re
import miniInstall
from pyminitouch import safe_connection, safe_device, MNTDevice, CommandBuilder

#minicap相关类
class Banner:
    def __init__(self):
        self.__banner = OrderedDict(
            [('version', 0),
             ('length', 0),
             ('pid', 0),
             ('realWidth', 0),
             ('realHeight', 0),
             ('virtualWidth', 0),
             ('virtualHeight', 0),
             ('orientation', 0),
             ('quirks', 0)
             ])
 
    def __setitem__(self, key, value):
        self.__banner[key] = value
 
    def __getitem__(self, key):
        return self.__banner[key]
 
    def keys(self):
        return self.__banner.keys()
 
    def __str__(self):
        return str(self.__banner)
 
 
class Minicap:
    def __init__(self, host, port, banner):
        self.buffer_size = 2048
        self.host = host
        self.port = port
        self.banner = banner
        self.isConnected=False
 
    def connect(self):
        self.isConnected=True
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except (socket.error) as e:
            # print(e)
            sys.exit(1)
        self.socket.connect((self.host, self.port))

    def on_image_transfered(self, data):
        file_name = scr_road  # 图片名
        with open(file_name, 'wb') as f:
            for b in data:
                f.write((b).to_bytes(1,'big'))
 
    def consume(self):
        global scr
        readBannerBytes = 0
        bannerLength = 24
        readFrameBytes = 0
        frameBodyLength = 0  
        data = []
        while True:
            flag=0
            chunk = self.socket.recv(self.buffer_size)
            cursor = 0
            buf_len = len(chunk)    
            while cursor < buf_len:
                if readBannerBytes < bannerLength:
                    map(lambda i, val: self.banner.__setitem__(self.banner.keys()[i], val),
                        [i for i in range(len(self.banner.keys()))], struct.unpack("<2b5ibB", chunk))
                    cursor = buf_len
                    readBannerBytes = bannerLength
                elif readFrameBytes < 4:
                    frameBodyLength += (chunk[cursor] << (readFrameBytes * 8)) >> 0
                    cursor += 1
                    readFrameBytes += 1
                else:
                    if buf_len - cursor >= frameBodyLength:
                        data.extend(chunk[cursor:cursor + frameBodyLength])
                        self.on_image_transfered(data)
                        cursor += frameBodyLength
                        frameBodyLength = readFrameBytes = 0
                        data = []
                        flag=1
                    else:
                        data.extend(chunk[cursor:buf_len])
                        frameBodyLength -= buf_len - cursor
                        readFrameBytes += buf_len - cursor
                        cursor = buf_len
            if flag==1:
                scr=cv2.imread(scr_road)
                
 
#界面设计
#   主窗口
class TabWidget_set(QTabWidget):#主窗口             ->None
    def __init__(self):
        global mnq_idx
        super(TabWidget_set, self).__init__()
        self.setGeometry(300, 500, 1100, 700)
        self.setWindowTitle('fgoTTScript')
        self.setWindowIcon(QIcon('litShk.ico'))
        # self.setMaximumSize(1000, 700)
        

        # self.ocr=ocr_laoding()
        self.settings=json_read()
        mnq_idx=self.settings['changable']['mnqChoose']['mnqChoose']

        self.tab1 :Widget_run= Widget_run(self)
        self.addTab(self.tab1, '运行')

        self.console_log=Log(self)
        

        self.flow_fight=Flow_Fight(self)
        self.flow_general=Flow_General(self)

        self.tab2 :Widget_set= Widget_set(self)
        self.addTab(self.tab2, '设置')

        
        self.mc = Minicap('localhost', 1717, Banner())



        
        self.thread_update:Thread_Update=Thread_Update(self)
        self.thread_run=Thread_Run(self)
        self.thread_mc=Thread_Minicap(self)
        self.thread_init=Thread_Init(self)

        

        


    def update(self) -> None:
        global time_count
        time_count += 0.5
            
        
        img = QPixmap(scr_road)
        self.tab1.hbox_screen.la_screen.setPixmap(img)  
        self.tab1.hbox_screen.la_time.setText(str(int(time_count)))

        for idx in self.flow_general.state_lst[self.flow_general.state_idx].neighbor_state:
            if check(self.flow_general.state_lst[idx])==True:
                self.flow_general.state_idx=idx
                # break
        self.tab1.la_state.setText('state:'+self.flow_general.state_lst[self.flow_general.state_idx].name)
        neighbor_state_text=''
        for neighbor_idx in self.flow_general.state_lst[self.flow_general.state_idx].neighbor_state:
            neighbor_state_text+=self.flow_general.name_lst[neighbor_idx]+','
        self.tab1.la_neighborState.setText('neighborState:'+neighbor_state_text)
        self.tab1.la_fightCount.setText('战斗次数:'+str(self.flow_general.fight_current_count))
        
        

        
    def keyPressEvent(self, event) -> None:
        if event.key() == Qt.Key_Escape:
            if self.mc.isConnected :
                self.thread_update.terminate()
                self.thread_mc.terminate()
                self.mc.socket.close()
                adb_cmd('adb kill-server')
            self.close()
        elif event.key() == Qt.Key_1:
            self.setCurrentWidget(self.tab1)
        elif event.key() == Qt.Key_2:
            self.setCurrentWidget(self.tab2)


#       子窗口
class Widget_run(QWidget):#运行窗口                 ->主窗口
    def __init__(self,total_tab:TabWidget_set):
        super(Widget_run, self).__init__()



        self.init(total_tab)


    def init(self,total_tab:TabWidget_set) -> None:
        self.vbox1 = QVBoxLayout(self)


        self.hbox_description = QHBoxLayout()
        self.vbox1.addLayout(self.hbox_description)
        mnq_idx=total_tab.settings['changable']['mnqChoose']['mnqChoose']
        self.la_mnq=QLabel('模拟器:'+mnq[mnq_idx])
        self.hbox_description.addWidget(self.la_mnq)
        self.la_fightCount=QLabel('战斗次数:'+'0')
        # self.la_fightCount.setText("<p style='color:red;'>这是一段html的红色文字</p>")
        self.hbox_description.addWidget(self.la_fightCount)
        self.la_state=QLabel('state:'+'init')
        self.hbox_description.addWidget(self.la_state)
        self.la_neighborState=QLabel('neighborState:'+'init')
        self.hbox_description.addWidget(self.la_neighborState)

        self.hbox_testBtn=QHBoxLayout()
        self.vbox1.addLayout(self.hbox_testBtn)
        self.hbox_testBtn.addStretch(1)
        self.btn_reset=QPushButton('reset')
        self.btn_reset.clicked.connect(lambda cnct: self.reset_cnct(total_tab))
        self.hbox_testBtn.addWidget(self.btn_reset)
        self.btn_test=QPushButton('test')
        self.btn_test.clicked.connect(lambda cnct: self.test_cnct(total_tab))
        self.hbox_testBtn.addWidget(self.btn_test)
        self.hbox_testBtn.addStretch(1)
        

        self.hbox_screen = HBox_screen()
        self.vbox1.addLayout(self.hbox_screen)


        self.hbox_switch=QHBoxLayout()
        self.vbox1.addLayout(self.hbox_switch)
        self.hbox_switch.addStretch(1)
        self.btn_connect_start = QPushButton(text='连接开始')
        self.btn_connect_start.clicked.connect(lambda cnct:self.connect_start_cnct(total_tab))
        self.hbox_switch.addWidget(self.btn_connect_start)
        self.btn_connect_stop = QPushButton(text='连接结束')
        self.btn_connect_stop.clicked.connect(lambda cnct:self.connect_stop_cnct(total_tab))
        self.btn_connect_stop.setEnabled(False)
        self.hbox_switch.addWidget(self.btn_connect_stop)
        self.btn_script_start = QPushButton(text='运行开始')
        self.btn_script_start.clicked.connect(lambda cnct:self.script_start_cnct(total_tab))
        self.btn_script_start.setEnabled(False)
        self.hbox_switch.addWidget(self.btn_script_start)
        self.btn_script_stop = QPushButton(text='清空日志')
        self.btn_script_stop.clicked.connect(lambda cnct:self.script_stop_cnct(total_tab))
        self.btn_script_stop.setEnabled(False)
        self.hbox_switch.addWidget(self.btn_script_stop)
        self.hbox_switch.addStretch(1)


    def test_cnct(self,total_tab:TabWidget_set):
        total_tab.console_log.log_update('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        

    def reset_cnct(self,total_tab:TabWidget_set):
        total_tab.console_log.log_update('reset init running')
        print('reset init running')
        total_tab.flow_general.state_idx=0
        self.la_state.setText('state:'+total_tab.flow_general.name_lst[total_tab.flow_general.state_idx])
        neighbor_state_text=''
        for neighbor_idx in total_tab.flow_general.state_lst[total_tab.flow_general.state_idx].neighbor_state:
            neighbor_state_text+=total_tab.flow_general.name_lst[neighbor_idx]+','
        self.la_neighborState.setText('neighborState:'+neighbor_state_text)

        total_tab.console_log.log_update('reset finished')
        print('reset finished')


    def connect_start_cnct(self,total_tab:TabWidget_set):
        text_lst=['连接开始','连接暂停','连接恢复']
        if self.btn_connect_start.text()==text_lst[0]:
            self.btn_connect_start.setText(text_lst[1])
            total_tab.thread_init.start()
        elif self.btn_connect_start.text()==text_lst[1]:
            self.btn_connect_start.setText(text_lst[2])
            total_tab.thread_update.pause()
        else:
            self.btn_connect_start.setText(text_lst[1])
            total_tab.thread_update.resume()
        
        self.btn_connect_stop.setEnabled(True)


    def connect_stop_cnct(self,total_tab:TabWidget_set):
        self.btn_connect_stop.setEnabled(False)
        self.btn_connect_start.setText('连接开始')
        total_tab.thread_update.terminate()
        total_tab.thread_mc.terminate()
        total_tab.mc.socket.close()
        adb_cmd('adb kill-server')


    def script_start_cnct(self,total_tab:TabWidget_set):
        text_lst=['运行开始','运行暂停','运行恢复']
        if self.btn_script_start.text()==text_lst[0]:
            total_tab.thread_run.start()
            self.btn_script_start.setText(text_lst[1])
        elif self.btn_script_start.text()==text_lst[1]:
            self.btn_script_start.setText(text_lst[2])
            total_tab.thread_run.pause()
        else:
            self.btn_script_start.setText(text_lst[1])
            total_tab.thread_run.resume()

        self.btn_script_stop.setEnabled(True)


    def script_stop_cnct(self,total_tab:TabWidget_set):
        total_tab.console_log.log_reset()


class Widget_set(QWidget):#设置窗口                 ->主窗口
    def __init__(self,total_tab:TabWidget_set):
        super(Widget_set, self).__init__()
        self.init(total_tab)

    def init(self,total_tab:TabWidget_set) -> None:
        self.hbox = QHBoxLayout(self)

        self.setTitle_list=QVBoxLayout()
        self.hbox.addLayout(self.setTitle_list)
        
        self.la_lst:list[QLabel]=[]
        self.nm_la_lst:list[str]=['策略',
                              '助战',
                              '多次战斗设置',
                              '模拟器选择',
                              'value:'+'0',]
        self.num_la:int=len(self.nm_la_lst)-1
        for i in range(self.num_la):
            self.la_lst.append(QLabel(self.nm_la_lst[i]))
            self.setTitle_list.addWidget(self.la_lst[i])
        self.la_lst[0].setStyleSheet("background-color:#cccccc;")
        self.setTitle_list.addStretch(1)

        self.scrollArea_setting=ScrollArea_setting(total_tab)
        self.scrollArea_setting.setFixedWidth(700)
        self.scrollArea_setting.verticalScrollBar().valueChanged.connect(lambda cnct: self.scrollBar_cnct())
        self.hbox.addWidget(self.scrollArea_setting)

    def scrollBar_cnct(self):
        value=self.scrollArea_setting.verticalScrollBar().value()
        if value<500:
            idx=0
        elif value<840:
            idx=1
        elif value<890:
            idx=2
        else:
            idx=3
        for i in range(self.num_la):
            self.la_lst[i].setStyleSheet("background-color:#ffffff;")
        self.la_lst[idx].setStyleSheet("background-color:#cccccc;")
                

#           子布局
class HBox_screen(QHBoxLayout):#显示模拟器画面       ->运行窗口
    def __init__(self):
        super(HBox_screen, self).__init__()

        self.init()

    def init(self) -> None:
        
        self.vbox_screen = QVBoxLayout()
        self.addLayout(self.vbox_screen)
        self.vbox_screen.addStretch(1)
        self.la_screen = QLabel()
        self.la_screen.setPixmap(QPixmap(scr_road))
        self.vbox_screen.addWidget(self.la_screen)

        self.splitter_log=QSplitter()
        self.splitter_log.setOrientation(Qt.Vertical)
        self.addWidget(self.splitter_log)
        self.la_time = QLabel('0')
        self.splitter_log.addWidget(self.la_time)
        self.scroll_log=QScrollArea()
        self.scroll_log.setFixedHeight(450)
        self.splitter_log.addWidget(self.scroll_log)
        self.la_log=QLabel('none')
        self.la_log.setFixedWidth(530)
        self.scroll_log.setWidget(self.la_log)

    def log_change(self,text:str):
        self.la_log.setText(text)
        

class ScrollArea_setting(QScrollArea):#设置滚动区域   ->设置窗口
    def __init__(self,total_tab:TabWidget_set):
        super(ScrollArea_setting, self).__init__()

        self.strategy_idx=total_tab.settings['changable']['sao']['strategyChoose']-1
        self.flow_fight=total_tab.flow_fight
        self.init(total_tab)

    def init(self,total_tab:TabWidget_set) -> None:
        self.win_scrollArea=QSplitter()
        self.win_scrollArea.setOrientation(Qt.Vertical)


        self.qb_strategy=QGroupBox('策略')
        self.win_scrollArea.addWidget(self.qb_strategy)
        self.qb_strategy_vbox=QVBoxLayout()
        self.qb_strategy.setLayout(self.qb_strategy_vbox)
        self.qb_strategy_lst:list[GroupBox_Strategy]=[]
        self.qb_strategy_num=2
        for i in range(self.qb_strategy_num):
            self.qb_strategy_lst.append(GroupBox_Strategy(total_tab,i+1))
            self.qb_strategy_vbox.addWidget(self.qb_strategy_lst[i])
        self.la_strategyChoose=QLabel('策略选择')
        self.qb_strategy_vbox.addWidget(self.la_strategyChoose)
        self.cb_strategyChoose=QComboBox()
        self.cb_strategyChoose.addItems(['1',
                                '2',])
        self.cb_strategyChoose.setCurrentIndex(self.strategy_idx)
        self.cb_strategyChoose.currentIndexChanged.connect(lambda cnct:self.cb_strategyChoose_cnct(total_tab))
        self.qb_strategy_vbox.addWidget(self.cb_strategyChoose)

        self.qb_assist=GroupBox_Assist(total_tab)
        self.win_scrollArea.addWidget(self.qb_assist)

        self.qb_continue=GroupBox_Continue(total_tab)
        self.win_scrollArea.addWidget(self.qb_continue)

        self.qb_mnq=GroupBox_Mnq(total_tab)
        self.win_scrollArea.addWidget(self.qb_mnq)


        self.setWidget(self.win_scrollArea)

    def cb_strategyChoose_cnct(self,total_tab:TabWidget_set):
        self.strategy_idx=self.cb_strategyChoose.currentIndex()
        for qb_strategy in self.qb_strategy_lst:
            qb_strategy.strategy_idx=self.strategy_idx
        for state_idx in range(3):
            self.flow_fight.state_lst[2*state_idx+1].strategy_str=total_tab.settings['changable']['sao']['strategy{}'.format(str(self.strategy_idx+1))]['skill{}_act'.format(state_idx+1)]
            self.flow_fight.state_lst[2*state_idx+2].strategy_str=total_tab.settings['changable']['sao']['strategy{}'.format(str(self.strategy_idx+1))]['order{}_act'.format(state_idx+1)]
        total_tab.settings['changable']['sao']['strategyChoose']=self.strategy_idx+1
        json_save(total_tab.settings)


class GroupBox_Strategy(QGroupBox):#策略设置            ->滚动区域
    def __init__(self,total_tab:TabWidget_set,index:int):
        super(GroupBox_Strategy, self).__init__('3T策略{}'.format(index))

        self.flow_fight=total_tab.flow_fight

        self.index=index
        self.strategy_idx=total_tab.settings['changable']['sao']['strategyChoose']-1

        self.strategy=total_tab.settings['changable']['sao']['strategy{}'.format(index)]
        self.init(total_tab)

    def init(self,total_tab:TabWidget_set) -> None:
        self.setFixedWidth(500)
        self.vbox=QVBoxLayout()
        self.setLayout(self.vbox)
        
        self.vbox_turn_lst:list[Vbox_Turn]=[]
        for i in range(3):
            self.vbox_turn_lst.append(Vbox_Turn(self,total_tab,i+1))
            self.vbox.addLayout(self.vbox_turn_lst[i])


class GroupBox_Assist(QGroupBox):#助战设置              ->滚动区域
    def __init__(self,total_tab:TabWidget_set):
        super(GroupBox_Assist, self).__init__('助战')

        self.state_assistChoose=total_tab.flow_general.state_assistChoose

        self.isCloth=total_tab.settings['changable']['isCloth']['isCloth']
        self.init(total_tab)
    
    def init(self,total_tab:TabWidget_set) -> None:
        self.vbox=QVBoxLayout()
        self.setLayout(self.vbox)


        self.cb_cloth=QCheckBox('是否关心礼装')
        self.cb_cloth.setChecked(int(self.isCloth))
        self.cb_cloth.stateChanged.connect(lambda cnct: self.cb_cnct(total_tab))
        self.vbox.addWidget(self.cb_cloth)


        self.la_title1=QLabel('助战礼装选择1')
        self.vbox.addWidget(self.la_title1)
        self.hbox_assist_1=Hbox_assist(1)
        self.vbox.addLayout(self.hbox_assist_1)


        self.la_title2=QLabel('助战礼装选择2')
        self.vbox.addWidget(self.la_title2)
        self.hbox_assist_2=Hbox_assist(2)
        self.vbox.addLayout(self.hbox_assist_2)

        self.la_title3=QLabel('助战礼装选择3')
        self.vbox.addWidget(self.la_title3)
        self.hbox_assist_3=Hbox_assist(3)
        self.vbox.addLayout(self.hbox_assist_3)

    def cb_cnct(self,total_tab:TabWidget_set):
        self.isCloth=self.cb_cloth.isChecked()
        self.state_assistChoose.isCloth=self.isCloth
        total_tab.settings['changable']['isCloth']['isCloth']=self.isCloth
        json_save(total_tab.settings)


class GroupBox_Continue(QGroupBox):#
    def __init__(self,total_tab:TabWidget_set):
        super(GroupBox_Continue, self).__init__('多次战斗设置')

        self.flow_general=total_tab.flow_general
        self.settings=total_tab.settings

        self.init()

    def init(self) -> None:
        self.vbox=QVBoxLayout()
        self.setLayout(self.vbox)

        self.cb_isAgain=QCheckBox('是否多次战斗')
        self.cb_isAgain.setChecked(self.flow_general.state_fightAgain.isAgain)
        self.cb_isAgain.stateChanged.connect(lambda:self.cb_isAgain_cnct())
        self.vbox.addWidget(self.cb_isAgain)
        self.la_fightCount=QLabel('战斗次数')
        self.vbox.addWidget(self.la_fightCount)
        self.le_fightCount=QLineEdit()
        self.le_fightCount.setText(str(self.flow_general.fight_count))
        self.le_fightCount.textChanged.connect(lambda cnct:self.le_fightCount_cnct())
        self.vbox.addWidget(self.le_fightCount)
        self.la_apple=QLabel('吃苹果类型')
        self.vbox.addWidget(self.la_apple)
        self.cbb_apple=QComboBox()
        self.cbb_apple.addItems(['金苹果',
                                '银苹果',
                                '蓝苹果',
                                '铜苹果',
                                '不吃苹果'])
        self.cbb_apple.setCurrentIndex(self.flow_general.state_drug.apple_index)
        self.cbb_apple.currentIndexChanged.connect(lambda cnct:self.cbb_apple_cnct())
        self.vbox.addWidget(self.cbb_apple)
        

    def cb_isAgain_cnct(self):
        self.flow_general.state_fightAgain.isAgain=self.cb_isAgain.isChecked()
        self.settings['changable']['again']['isAgain']=self.cb_isAgain.isChecked()
        json_save(self.settings)

    def le_fightCount_cnct(self):
        if self.le_fightCount.text()=='a':
            self.flow_general.fight_count=-1
        elif self.le_fightCount.text()<='9' and self.le_fightCount.text()>='0':
            self.flow_general.fight_count=int(self.le_fightCount.text())

        self.settings['changable']['again']['fight_count']=int(self.le_fightCount.text())
        json_save(self.settings)

    def cbb_apple_cnct(self):
        self.flow_general.state_drug.apple_index=self.cbb_apple.currentIndex()
        self.settings['changable']['again']['appleIndex']=self.cbb_apple.currentIndex()
        json_save(self.settings)

        
class GroupBox_Mnq(QGroupBox):#模拟器设置                 ->滚动区域
    def __init__(self,total_tab:TabWidget_set):
        super(GroupBox_Mnq, self).__init__('模拟器选择')
        self.la_mnq=total_tab.tab1.la_mnq

        self.init(total_tab)

    def init(self,total_tab:TabWidget_set) -> None:
        self.vbox=QVBoxLayout(self)

        self.cbb_mnq=QComboBox()
        self.vbox.addWidget(self.cbb_mnq)
        self.la_expain=QLabel()
        self.vbox.addWidget(self.la_expain)
        self.la_expain.setText('MuMu模拟器:127.0.0.1:7555\n夜神模拟器(nox):127.0.0.1:62001')
        self.cbb_mnq.addItems(mnq)
        self.cbb_mnq.setCurrentIndex(mnq_idx)
        self.cbb_mnq.currentIndexChanged.connect(lambda cnct:self.cbb_mnq_cnct(total_tab))
        self.btn_mnq_connect_test=QPushButton('模拟器连接测试')
        self.vbox.addWidget(self.btn_mnq_connect_test)
        self.btn_mnq_connect_test.clicked.connect(lambda cnct:self.mnq_test_cnct())
        self.la_test_result=QLabel('none')
        self.vbox.addWidget(self.la_test_result)


        self.btn_mini_install=QPushButton('minicap及minitouch安装')
        self.btn_mini_install.clicked.connect(lambda cnct:self.mini_install_cnct())
        self.vbox.addWidget(self.btn_mini_install)
        self.la_install_result=QLabel('none')
        self.vbox.addWidget(self.la_install_result)
        

        self.le_add=QLineEdit()
        self.le_add.setText('name ip')
        self.vbox.addWidget(self.le_add)
        self.btn_add=QPushButton('模拟器添加')
        self.btn_add.clicked.connect(lambda cnct:self.mnq_add())
        self.vbox.addWidget(self.btn_add)
        

        self.le_del=QLineEdit()
        self.le_del.setText('name')
        self.vbox.addWidget(self.le_del)
        self.btn_del=QPushButton('模拟器删除')
        self.btn_del.clicked.connect(lambda cnct:self.mnq_del())
        self.vbox.addWidget(self.btn_del)
        

    def cbb_mnq_cnct(self,total_tab:TabWidget_set):
        global mnq_idx
        mnq_idx=self.cbb_mnq.currentIndex()
        self.la_mnq.setText('模拟器:'+mnq[mnq_idx])
        total_tab.settings['changable']['mnqChoose']['mnqChoose']=mnq_idx
        json_save(total_tab.settings)

    def mnq_test_cnct(self):
        adb_cmd('adb disconnect')
        adb_cmd('adb connect '+ipConnect[mnq_idx])
        devices_lst=subprocess.getoutput('adb devices').split('\n')
        adb_cmd('adb disconnect')
        devices_lst.remove('List of devices attached')
        if len(devices_lst)==0:
            self.la_test_result.setText('failed to connect')
        elif devices_lst[0]==ipConnect[mnq_idx]+'\tdevice':
            self.la_test_result.setText('success to connect\n'+ipConnect[mnq_idx]+'\tdevice')
        else:
            self.la_test_result.setText('wrong to connect')

            
    def mini_install_cnct(self):
        flag,struc,sdk=miniInstall.install(ipConnect[mnq_idx])
        text="structure: "+struc+'\nsdk: '+sdk+'\nsuccess to install'
        if flag:
            self.la_install_result.setText(text)


    def mnq_add(self):
        text=self.le_add.text().split(' ')
        insertion={"name":text[0],"ip":text[1]}
        obj=json_read()
        obj['mnq'][text[0]]=insertion
        json_save(obj)

    def mnq_del(self):
        text=self.le_del.text()
        obj=json_read()
        if text in obj['mnq'].keys():
            del obj['mnq'][text]
        json_save(obj)


class Vbox_Turn(QVBoxLayout):#回合设置              ->策略
    def __init__(self,parent:GroupBox_Strategy,total_tab:TabWidget_set,turnIdx:int):
        super(Vbox_Turn, self).__init__()
        self.turnIdx=turnIdx
        self.skill=parent.strategy['skill{}_act'.format(turnIdx)]
        self.order=parent.strategy['order{}_act'.format(turnIdx)]
        self.init(parent,total_tab)
    
    def init(self,parent:GroupBox_Strategy,total_tab:TabWidget_set) -> None:
        turnIdx=self.turnIdx
        self.label_turnIdx=QLabel(text='Turn '+str(turnIdx))
        self.addWidget(self.label_turnIdx)

        self.le_skill_check=QLineEdit()
        self.le_skill_check.setText(self.skill)
        self.le_skill_check.textChanged.connect(lambda cnct:self.le_skill_cnct(parent,total_tab,turnIdx))
        self.addWidget(self.le_skill_check)
        

        self.le_order_check=QLineEdit()
        self.le_order_check.setText(self.order)
        self.le_order_check.textChanged.connect(lambda cnct:self.le_order_cnct(parent,total_tab,turnIdx))
        self.addWidget(self.le_order_check)

    def le_skill_cnct(self,parent:GroupBox_Strategy,total_tab:TabWidget_set,turnIdx:int):
        self.skill=self.le_skill_check.text()
        parent.strategy['skill{}_act'.format(turnIdx)]=self.le_skill_check.text()
        json_save(total_tab.settings)
        if parent.strategy_idx+1==parent.index:
            parent.flow_fight.state_lst[2*self.turnIdx-1].strategy_str=self.skill

        
    def le_order_cnct(self,parent:GroupBox_Strategy,total_tab:TabWidget_set,turnIdx:int):
        self.order=self.le_order_check.text()
        parent.strategy['order{}_act'.format(turnIdx)]=self.le_order_check.text()
        json_save(total_tab.settings)
        if parent.strategy_idx+1==parent.index:
            parent.flow_fight.state_lst[2*self.turnIdx].strategy_str=self.order


class Hbox_assist(QHBoxLayout):#助战设置            ->滚动区域
    def __init__(self,idx:int):
        super(Hbox_assist, self).__init__()

        self.bs=0.7
        self.assist_servant_road='material\\fgo\\assist_servant_{}.png'.format(str(idx))
        self.assist_cloth_road='material\\fgo\\assist_cloth_{}.png'.format(str(idx))
        self.init()
    
    def init(self) -> None:
        #flsta img
        self.le_assist_name=QLineEdit()
        # img_shw_w(self.le_assist_name, self.assist_servant_road,self.bs)
        # self.addWidget(self.le_assist_name)
        
        self.la_img_servant=QLabel()
        img_shw_w(self.la_img_servant, self.assist_servant_road,self.bs)
        self.addWidget(self.la_img_servant)

        self.la_img_cloth=QLabel()
        img_shw_w(self.la_img_cloth, self.assist_cloth_road,self.bs)
        self.addWidget(self.la_img_cloth)
        #flsto img

        #flsta btn
        self.btn_update=QPushButton(text='更新')
        self.btn_update.clicked.connect(lambda cnct:self.btn_cnct())
        self.addWidget(self.btn_update)
        #flsto btn


    def btn_cnct(self):
        #parameter_get
        para_fn='settings\\fixed\\paspn\\assist_pas.txt'
        para_f=open(para_fn,'r')
        para=para_f.read().split('\n')
        para_f.close()

        assist_servant_pas,assist_cloth_pas=list(map(int,para[0].split(' '))),list(map(int,para[1].split(' ')))

        scr_cap(assist_servant_pas,scr_road,self.assist_servant_road)
        img_shw_w(self.la_img_servant, self.assist_servant_road,self.bs)
        
        scr_cap(assist_cloth_pas,scr_road,self.assist_cloth_road)
        img_shw_w(self.la_img_cloth, self.assist_cloth_road,self.bs)
   

#流程设计
#流式
class Flow():                                                                                                                               #××××
    def __init__(total_tab:TabWidget_set,self,name_lst:list[str],neighbor_state:list[list[int]]):
        self.total_tab=total_tab


        self.name_lst:list[str]=name_lst
        self.neighbor_state:list[list[int]]=neighbor_state
        self.state_lst:list[State_General]=[]
        for idx in range(len(self.name_lst)):
            self.state_lst.append(State_General(self.name_lst[idx],idx,self.neighbor_state[idx]))
        # 状态
        self.state_idx:int=0
        # 是否运行
        self.isable:bool=False


class Flow_General():
    def __init__(self,total_tab:TabWidget_set):
        # 流程分类：初始 关卡前 磕药 助战选择 准备 战斗(有子流程) 结算 再来一次 加载   其中初始、加载无页面特征点 备用：'loading'

        # 状态
        self.state_idx:int=0
        
        self.fight_count=total_tab.settings['changable']['again']['fight_count']
        
        self.fight_current_count=0
        # 是否运行
        self.isable:bool=False

        self.name_lst:list[str] =['init','before','drug','assistChoose','prepare','fight','result','fightAgain']
        self.neighbor_state:list[list[int]] =[[1,2,3,4,5,6,7],
                                            [2,3],
                                            [3,4],
                                            [4,5],
                                            [5],
                                            [6],
                                            [7],
                                            [1,2,3]]
                                           

        self.state_init:State_Init=State_Init(total_tab)
        self.state_before:State_Before=State_Before(total_tab)
        self.state_drug:State_Drug=State_Drug(total_tab)
        self.state_assistChoose:State_AssistChoose=State_AssistChoose(total_tab,self)
        self.state_prepare:State_Prepare=State_Prepare(total_tab)
        self.state_fight:State_Fight=State_Fight(total_tab)
        self.state_result:State_Result=State_Result(total_tab,self)
        self.state_fightAgain:State_FightAgain=State_FightAgain(total_tab)

        self.state_lst=[self.state_init,self.state_before,self.state_drug,self.state_assistChoose,self.state_prepare,
            self.state_fight,self.state_result,self.state_fightAgain]
    
    def state_change(self,goalState:int):
        self.state_idx=goalState


class Flow_Fight():
    def __init__(self,total_tab:TabWidget_set):

        self.name_lst:list[str]=['off','skill1','order1','skill2','order2','skill3','order3']
        self.neighbor_state:list[list[int]]=[[1],[2],[3],[4],[5],[6],[0]]
        self.state_lst:list[State]=[State_InFight(self.name_lst[0],0,self.neighbor_state[0])]
        for idx in range(3):
            self.state_lst.append(State_Skill(total_tab,idx))
            self.state_lst.append(State_Order(total_tab,idx))
        # 状态
        self.state_idx:int=0
        # 是否运行
        self.isable:bool=False


class State():
    def __init__(self,name:str,index:int,neighbor_state:list[int]):
        self.name:str=name
        self.index:int=index
        self.neighbor_state:list[int]=neighbor_state

        #特征标
        #   包括路径、图像、SIFT参数
        #行动标
        #   包括行动类型、行动参数


class State_General(State):
    def __init__(self,total_tab:TabWidget_set,name:str,index:int,neighbor_state:list[int]):
        super(State_General,self).__init__(name,index,neighbor_state)

        self.feature_img_road:str='material\\fgo\\g_{}_{}.png'.format(str(index),name)
        self.feature_img:np.ndarray=cv2.imread(self.feature_img_road)


        self.feature_paspn:list[float]=total_tab.settings['fixed']['paspn']['{}_paspn'.format(name)]
        


        self.y:int=int(self.feature_paspn[0])
        self.x:int=int(self.feature_paspn[1])
        self.h:int=int(self.feature_paspn[2])
        self.w:int=int(self.feature_paspn[3])
        self.para:float=self.feature_paspn[4]
        self.num:int=int(self.feature_paspn[5])


class State_InFight(State):
    def __init__(self,name:str,index:int,neighbor_state:list[int]):
        super(State_InFight,self).__init__(name,index,neighbor_state)


class State_Init(State_General):
    def __init__(self,total_tab:TabWidget_set):
        super(State_Init,self).__init__(total_tab,'init',0,[1,2,3,4,5,6,7])

    def act(self):
        pass


class State_Before(State_General):
    def __init__(self,total_tab:TabWidget_set):
        super(State_Before,self).__init__(total_tab,'before',1,[2,3])
        self.x,self.y=100,390

    def act(self):
        # 进入
        adb_cmd('adb shell input tap {} {}'.format(int(self.y*bs),int(self.x*bs)))
        time.sleep(3)

        
class State_Drug(State_General):
    def __init__(self,total_tab:TabWidget_set):
        super(State_Drug,self).__init__(total_tab,'drug',2,[3,4])
        self.pos_lst:list[list[list]]=[
            [['t',130,290],['t',230,350],],
            [['t',190,290],['t',230,350],],
            [['s',floor(500/bs),floor(830/bs),floor(500/bs),floor(200/bs),500],['t',130,290],['t',230,350],],
            [['s',floor(500/bs),floor(830/bs),floor(500/bs),floor(200/bs),500],['t',190,290],['t',230,350],],
        ]

        self.apple_index:int=total_tab.settings['changable']['again']['appleIndex'] #0,1,2,3代表金银蓝铜苹果
        

    def act(self):
        #嗑药
        for pos in self.pos_lst[self.apple_index]:
            if pos[0]=='t':
                adb_cmd('adb shell input tap {} {}'.format(int(pos[2]*bs),int(pos[1]*bs)))
            elif pos[0]=='s':
                adb_cmd('adb shell input swipe {} {} {} {} {}'.format(int(pos[1]*bs),int(pos[2]*bs),int(pos[3]*bs),int(pos[4]*bs),pos[5]))
            time.sleep(0.3)
        time.sleep(3)


class State_AssistChoose(State_General):
    def __init__(self,total_tab:TabWidget_set,parent:Flow_General):
        super(State_AssistChoose,self).__init__(total_tab,'assistChoose',3,[4,5])

        self.console_log=total_tab.console_log
        # self.ocr=total_tab.ocr
        self.parent=parent

        self.assist_name=''


        self.isCloth=False

        self.servant_img_road_lst:list[str]=[]
        self.servant_img_lst:list[np.ndarray]=[]    
        self.cloth_img_road_lst:list[str]=[]
        self.cloth_img_lst:list[np.ndarray]=[]
        for index in range(3):
            self.servant_img_road_lst.append('material\\fgo\\assist_servant_{}.png'.format(str(index+1)))
            self.servant_img_lst.append(cv2.imread(self.servant_img_road_lst[index]))
            self.cloth_img_road_lst.append('material\\fgo\\assist_cloth_{}.png'.format(str(index+1)))
            self.cloth_img_lst.append(cv2.imread(self.cloth_img_road_lst[index]))

        self.x,self.y,self.w,self.h=72,15,90,90
        self.para,self.servant_num,self.cloth_num=0.8,5,5

        self.pos=[120,260]


    # def act_addidate(self):
    #     #判断是否有可用从者
    #     time.sleep(3)
    #     print('进行战斗次数'+str(self.parent.fight_current_count))
    #     self.console_log.log_update('进行战斗次数'+str(self.parent.fight_current_count))
    #     chooseTurn=1
    #     servantCount=0
    #     while True:
    #         servantCount+=1
    #     #判断从者、礼装是否正确
    #         flag=0
    #         print('Aassist Servant Choose Try {}'.format(str(servantCount)))
    #         self.console_log.log_update('assist servant choose try {}'.format(str(servantCount)))
    #         for index in range(3):
    #             servant_flag=check(self.servant_img_lst[index],scr[self.x:self.x+self.w,self.y:self.y+self.h],self.para,8)
    #             cloth_flag=check(self.cloth_img_lst[index],scr[self.x:self.x+self.w,self.y:self.y+self.h],self.para,5)
    #             print(servant_flag,cloth_flag)
    #             self.console_log.log_update('Servant:'+str(servant_flag)+'  Cloth:'+str(cloth_flag))
    #             if servant_flag and cloth_flag:
    #                 flag=1
    #                 break
    #         if flag==1:
    #             # 判断正确
    #             adb_cmd('adb shell input tap {} {}'.format(int(self.pos[1]*bs),int(self.pos[0]*bs)))
    #             print('Success')
    #             self.console_log.log_update('Success')
    #             time.sleep(4)
    #             break
    #         else:
    #             # 判断错误
    #             adb_cmd('adb shell input swipe 400 740 400 500 500')
    #             time.sleep(4)
    #             print('Fail')
    #             self.console_log.log_update('Fail')
    #         if servantCount==5:
    #             chooseTurn+=1
    #             servantCount=0
    #             adb_cmd('adb shell input tap {} {}'.format(int(380*bs),int(60*bs)))
    #             time.sleep(1)
    #             adb_cmd('adb shell input tap {} {}'.format(int(350*bs),int(230*bs)))
    #             time.sleep(2)


    def act(self):
        #判断是否有可用从者
        time.sleep(3)
        print('进行战斗次数'+str(self.parent.fight_current_count))
        self.console_log.log_update('进行战斗次数'+str(self.parent.fight_current_count))
        chooseTurn=1
        servantCount=0
        xca,yca,xcc,ycc=0,0,0,0
        flag=0
        while True:
            servantCount+=1
        #判断从者、礼装是否正确
            print('Aassist Servant Choose Try {}'.format(str(servantCount)))
            self.console_log.log_update('assist servant choose try {}'.format(str(servantCount)))
        
            if self.isCloth:
                for idx in range(3):
                    resa=cv2.matchTemplate(scr,self.servant_img_lst[idx],cv2.TM_CCOEFF_NORMED)
                    resc=cv2.matchTemplate(scr,self.cloth_img_lst[idx],cv2.TM_CCOEFF_NORMED)
                    if resa.max()>0.7 and resc.max()>0.7:
                        yca,xca=np.where(resa==np.max(resa))[0][0]+int(self.h/2),np.where(resa==np.max(resa))[1][0]+int(self.h/2)
                        ycc,xcc=np.where(resa==np.max(resa))[0][0]+int(self.h/2),np.where(resa==np.max(resa))[1][0]+int(self.h/2)
                        if abs(yca-ycc)<270:
                            flag=1
                            break
            else:
                for idx in range(3):
                    resa=cv2.matchTemplate(scr,self.servant_img_lst[idx],cv2.TM_CCOEFF_NORMED)
                    if resa.max()>0.7:
                        yca,xca=np.where(resa==np.max(resa))[0][0]+int(self.h/2),np.where(resa==np.max(resa))[1][0]+int(self.h/2)
                        flag=1
                        break

            if flag==1:
                # 判断正确
                adb_cmd('adb shell input tap {} {}'.format(int(xca*bs),int(yca*bs)))
                print('Success')
                self.console_log.log_update('Success')
                time.sleep(1)
                break
            else:
                # 判断错误
                print('Fail {}'.format(str(servantCount)))
                adb_cmd('adb shell input swipe 400 940 400 400 500')
                time.sleep(3)
                self.console_log.log_update('Fail {}'.format(str(servantCount)))
            if servantCount==6:
                chooseTurn+=1
                servantCount=0
                adb_cmd('adb shell input tap {} {}'.format(int(380*bs),int(60*bs)))
                time.sleep(1)
                adb_cmd('adb shell input tap {} {}'.format(int(350*bs),int(230*bs)))
                time.sleep(1)


class State_Prepare(State_General):
    def __init__(self,total_tab:TabWidget_set):
        super(State_Prepare,self).__init__(total_tab,'prepare',4,[3,5])
        self.x,self.y=270,460

    def act(self):
        #点击进入下一state
        adb_cmd('adb shell input tap {} {}'.format(int(self.y*bs),int(self.x*bs)))


class State_Fight(State_General):
    def __init__(self,total_tab:TabWidget_set):
        super(State_Fight,self).__init__(total_tab,'fight',5,[6])
        self.x,self.y=270,460
        self.flow_fight=total_tab.flow_fight
    
    def act(self):
        for i in range(1,len(self.flow_fight.state_lst)):
            self.flow_fight.state_lst[i].act()


class State_Result(State_General):
    def __init__(self,total_tab:TabWidget_set,parent:Flow_General):
        super(State_Result,self).__init__(total_tab,'result',6,[7])
        self.x,self.y=270,460
        self.parent=parent
    
    def act(self):
        #点击多下  进入再来一次环节
        for i in range(5):
            adb_cmd('adb shell input tap {} {}'.format(int(self.y*bs),int(self.x*bs)))
            time.sleep(0.3)
        self.parent.fight_current_count+=1


class State_FightAgain(State_General):
    def __init__(self,total_tab:TabWidget_set):
        super(State_FightAgain,self).__init__(total_tab,'fightAgain',7,[1,2,3])
        self.xAgain,self.yAgain=230,350
        self.xExit,self.yExit=20,40
        
        self.isAgain=total_tab.settings['changable']['again']['isAgain']
                
    
    def act(self):
        if self.isAgain:
            adb_cmd('adb shell input tap {} {}'.format(int(self.yAgain*bs),int(self.xAgain*bs)))
        else:
            adb_cmd('adb shell input tap {} {}'.format(int(self.yExit*bs),int(self.xExit*bs)))
        

class State_Skill(State_InFight):
    def __init__(self,total_tab:TabWidget_set,index:int):
        super(State_Skill,self).__init__('skill'+str(index+1),2*index+1,[2*index+2])

        self.parent_state:State_General=State_General(total_tab,'fight',5,[6])


        self.console_log:Log=total_tab.console_log
        strategyChoose=total_tab.settings['changable']['sao']['strategyChoose']
        self.strategy_str=total_tab.settings['changable']['sao']['strategy{}'.format(str(strategyChoose))]['skill{}_act'.format(str(index+1))]
        
        self.feature_img_road:str='material\\fgo\\f_skillGoal.png'
        self.feature_img:np.ndarray=cv2.imread(self.feature_img_road)
        self.feature_paspn:list[float]=total_tab.settings['fixed']['paspn']['f_skillGoal_paspn']

        self.y:int=int(self.feature_paspn[0])
        self.x:int=int(self.feature_paspn[1])
        self.h:int=int(self.feature_paspn[2])
        self.w:int=int(self.feature_paspn[3])
        self.para:float=self.feature_paspn[4]
        self.num:int=int(self.feature_paspn[5])


        self.pos_lst:dict[list[list[int]]]=total_tab.settings['fixed']['paspn']['skill_pas']

    def act(self):
        if self.strategy_str!='':
            part=re.compile(r'[0-9][0-9][0-9]')
            self.strategy_lst:list[int]=list(map(int,part.findall(self.strategy_str)))
            
        stayToFight(self.parent_state)
        for step in self.strategy_lst:
            # time.sleep(0.4)
            launcher=floor(step/100)
            skill_idx=floor(step/10)%10
            goal_servant=step%10
            launcher_lst=self.pos_lst['{}_{}'.format(str(launcher),str(skill_idx))]
            goal_lst=self.pos_lst[str(goal_servant)]
            self.console_log.log_update('turn'+str((self.index+1)/2)+'  skill'+str(step)+'  launcher')

            for act in launcher_lst:
                print('turn'+str((self.index+1)/2)+'  skill'+str(step)+'  launcher')
                adb_cmd('adb shell input tap {} {}'.format(int(bs*act[1]),int(bs*act[0])))
                time.sleep(1)

            for act in goal_lst:
                if goal_servant!=0:
                    stayToFight(self)
                adb_cmd('adb shell input tap {} {}'.format(int(bs*act[1]),int(bs*act[0])))
                print('turn'+str((self.index+1)/2)+'  skill'+str(step)+'  goal')
                self.console_log.log_update('turn'+str((self.index+1)/2)+'  skill'+str(step)+'  goal')
                act_nn=self.pos_lst['0'][0]
                adb_cmd('adb shell input tap {} {}'.format(int(bs*act_nn[1]),int(bs*act_nn[0])))
                time.sleep(2)
                
        
class State_Order(State_InFight):
    def __init__(self,total_tab:TabWidget_set,index:int):
        super(State_Order,self).__init__('order'+str(index+1),2*index+2,[(2*index+3)%7])
        
        self.console_log:Log=total_tab.console_log
        
        strategyChoose=total_tab.settings['changable']['sao']['strategyChoose']
        self.strategy_str=total_tab.settings['changable']['sao']['strategy{}'.format(str(strategyChoose))]['order{}_act'.format(str(index+1))]

        self.pos_lst:dict[list[list[int]]]=total_tab.settings['fixed']['paspn']['order_pas']

    def act(self):
        adb_cmd('adb shell input tap {} {}'.format(int(bs*445),int(bs*220)))
        time.sleep(1)
        print('enter order')
        self.console_log.log_update('enter order')
        for step in self.strategy_str:
            act=self.pos_lst[step]
            self.console_log.log_update(step)
            adb_cmd('adb shell input tap {} {}'.format(int(bs*act[1]),int(bs*act[0])))
            time.sleep(0.3)
            

        # for step_idx in range(3):
        #     step=self.strategy[step_idx]
        #     for pos_idx in range(len(self.pos_lst)):
        #         if self.pos_lst[pos_idx][0]==step:
        #             pos=list(map(int,self.pos_lst[pos_idx][1].split(',')))
        #             print(step)
        #             self.console_log.log_update(step)
        #             adb_cmd('adb shell input tap {} {}'.format(int(bs*pos[1]),int(bs*pos[0])))
        #             time.sleep(0.3)
        #             break
        time.sleep(15)
        print('finish order')
        self.console_log.log_update('finish order')


# #线程设计
class Thread_Minicap(QThread):#启动获取
    def __init__(self,total_tab:TabWidget_set):
        super(Thread_Minicap,self).__init__()
        self.mc=total_tab.mc

    def run(self):
        self.mc.consume()


class Thread_Update(QThread):#更新屏幕              ->主窗口
    def __init__(self,total_tab:TabWidget_set):
        super(Thread_Update,self).__init__()
        self.total_tab = total_tab
        self._isPause = False
        self._value = 0
        self.cond = QWaitCondition()
        self.mutex = QMutex()
    
    def run(self):
        global bs
        global time_count
        global scr
        while True:
            self.mutex.lock()       # 上锁
            if self._isPause:
                self.cond.wait(self.mutex)
            self.total_tab.update()
            time.sleep(0.5)
            self.mutex.unlock()  # 解锁
         
    def pause(self):    
        self._isPause = True
 
    def resume(self):
        self._isPause = False
        self.cond.wakeAll()


class Thread_Run(QThread):
    def __init__(self,total_tab:TabWidget_set):
        super(Thread_Run,self).__init__()
        
        self.console_log=total_tab.console_log
        self.flow_general=total_tab.flow_general

        self._isPause = False
        self._value = 0
        self.cond = QWaitCondition()
        self.mutex = QMutex()

    def run(self):
        global scr
        print('test running')
        self.console_log.log_update('test running')
        while True:
            self.mutex.lock()       # 上锁
            if self._isPause:
                self.cond.wait(self.mutex)
            state=self.flow_general.state_lst[self.flow_general.state_idx]
            if check(state):
                self.console_log.log_update('NOW {} RUNNING'.format(state.name))
                state.act()
            time.sleep(1)
            


            if self.flow_general.fight_current_count==self.flow_general.fight_count:
                break
            self.mutex.unlock()  # 解锁
        print('test finished')
        self.console_log.log_update('test finished')

    def pause(self):
        self._isPause = True
 
    def resume(self):
        self._isPause = False
        self.cond.wakeAll()


class Thread_Init(QThread):#启动获取
    def __init__(self,total_tab:TabWidget_set):
        super(Thread_Init,self).__init__()
        self.mc=total_tab.mc
        self.console_log=total_tab.console_log
        self.thread_mc=total_tab.thread_mc
        self.thread_update=total_tab.thread_update
        self.btn=total_tab.tab1.btn_script_start
    def run(self):
        global device
        init_thread()
        _DEVICE_ID = ipConnect[mnq_idx]
        
        device = MNTDevice(_DEVICE_ID)
        self.mc.connect()
        self.thread_mc.start()
        self.thread_update.start()
        self.console_log.log_update('start SERVER')
        self.btn.setEnabled(True)

#日志设计
class Log():
    def __init__(self,total_tab:TabWidget_set):
        self.console_log:str='none'
        self.la_log:QLabel=total_tab.tab1.hbox_screen.la_log
        self.lineNum=1

    def log_update(self,text:str,):
        self.console_log=time.strftime('%H:%M:%S',time.localtime(time.time()))+'\t'+text+'\n'+self.console_log
        self.lineNum+=1
        self.la_log.setFixedHeight((2*13-1)*self.lineNum)
        self.la_log.setText(self.console_log)

    def log_reset(self):
        self.console_log='none'
        self.la_log.setFixedHeight(2*13-1)
        self.la_log.setText(self.console_log)
        self.lineNum=1


#小功能
def img_shw_w(la: QLabel, roi,bs:float):               # img:image shw:show w:window 将图片展示在win中
    # roi:road or image

    # 重载  roi可为路径或图像
    if str(type(roi)) == "<class 'str'>":
        i = cv2.imread(roi)
    elif str(type(roi)) == "<class 'numpy.ndarray'>":
        i = roi
    # else:
    #     i=cv2.imread('mnq_screen.png',0)

    dx, dy = floor(i.shape[1]/bs), floor(i.shape[0]/bs)
    img_ysd = cv2.resize(i, [dx, dy])
    cv2.imwrite('tmp.png', img_ysd)
    img = QPixmap('tmp.png')
    la.setPixmap(img)


def scr_cap(pas:list[int],scr_road:str,cap_road:str) -> None:
    scr=cv2.imread(scr_road)
    cap=scr[pas[0]:pas[0]+pas[2],pas[1]:pas[1]+pas[3],:]
    cv2.imwrite(cap_road,cap)


def check(state) -> bool:
    if str(type(scr))!="<class 'NoneType'>":
        # x,y,w,h=state.x,state.y,state.w,state.h
        res=cv2.matchTemplate(scr,state.feature_img,cv2.TM_CCOEFF_NORMED)
        if res.max()<state.para:
            return False
        else:
            return True


def stayToFight(state):
    while True:
        if check(state):
            print('right')
            break
        time.sleep(2)


def set_win():
    # 创建进程
    app = QApplication(sys.argv)  # 创建进程
    app.setStyleSheet("QLabel,QPushButton,QGroupBox,QCheckBox,QComboBox,QTabWidget,QLineEdit{font-size: 13pt;}")
    total_tab = TabWidget_set()
    total_tab.show()
    sys.exit(app.exec_())          # 死循环，监听进程，如果没有这句，程序会闪退


def init_thread():
    global time_count
    global bs
    adb_cmd('adb disconnect')
    adb_cmd('adb connect '+ipConnect[mnq_idx])
    # 获取屏幕分辨率和放大倍数
    fbl=subprocess.getoutput('adb shell wm size')
    fbl_lst=[0,0]
    fbl_idx=0
    flag=0
    for i in range(len(fbl)):
        if '0'<=fbl[i] and fbl[i]<='9':
            flag=1
            fbl_lst[fbl_idx]=fbl_lst[fbl_idx]*10+int(fbl[i])
        if flag==1 and ('0'>fbl[i] or fbl[i]>'9'):
            fbl_idx+=1
            flag=0
            if fbl_idx>1:
                break
    bs=fbl_lst[0]/outputx
    
    os.popen('adb forward tcp:1717 localabstract:minicap')  # 执行了adb端口转发
    os.popen('adb shell LD_LIBRARY_PATH=/data/local/tmp /data/local/tmp/minicap -Q 40 -P {}x{}@{}x{}/0'.format(fbl_lst[0],fbl_lst[1],outputx,outputy))  # 启动了minicap服务
    
    time_count =0


def adb_cmd(text:str):
    adb_rec_str=re.compile(r'adb shell input')
    num_par=re.compile(r'\d+')
    if adb_rec_str.findall(text):
        num_lst=list(map(int,num_par.findall(text)))
        if re.findall('tap',text):
            num_lst=tuple(num_lst)
            device.tap([num_lst])
        elif re.findall('swipe',text):
            num=5
            (x0,y0,x1,y1,s)=num_lst
            if not x0-x1:
                x_lst=[x0]*5
            else:
                x_lst=range(x0,x1,int((x1-x0)/num))
            if not y0-y1:
                y_lst=[y0]*5
            else:
                y_lst=range(y0,y1,int((y1-y0)/num))
            pos_lst=[]
            for i in range(num):
                pos_lst.append((x_lst[i],y_lst[i]))
            device.swipe(pos_lst,duration=100)
    else:
        txt=text.replace('adb',r'platform-tools_r33.0.3-windows\platform-tools\adb.exe')
        subprocess.run(txt, shell=True)


def json_read() -> dict:
    f=open(setting_fn,'r')
    obj=json.loads(f.read())
    f.close()
    return obj


def json_save(obj):
    f=open(setting_fn,'w')
    json.dump(obj, f, skipkeys=False, ensure_ascii=True, check_circular=True,allow_nan=True, cls=None, indent=2, separators=None,default=None, sort_keys=False)
    f.close()


time_count=0
setting_fn='setting.json'
scr_road = 'mnq_screen.png'
scr=cv2.imread(scr_road)
settings=json_read()
mnq=list(settings['mnq'].keys())
ipConnect=[]
for name in mnq:
    ipConnect.append(settings['mnq'][name]['ip'])
outputx,outputy=512,288
bs=3.75


if __name__ == '__main__':                               # 主程zzzzzzzzzz
    

    set_win()


    b=0