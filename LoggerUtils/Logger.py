#coding:utf-8
'''
淘直播日志模块  ---> LoggerHelper.py
date：2021-05-14
Anchor：Levon
'''
import os
import time
os.chdir(os.path.abspath(os.path.split(os.path.abspath(os.path.realpath(__file__)))[0] + "/../Log"))

class Logger():
    def __init__(self,SpiderName=''):
        self.wrongFile = f'{SpiderName + "_"}wrong.log'
        self.infoFile = f'{SpiderName + "_"}info.log'
        self.errorFile = f'{SpiderName + "_"}error.log'
        self.debuggerFile = f'{SpiderName + "_"}debugger.log'
        self.mode = 'a+'
    def SetLoggerFileName(self,name):
        self.wrongFile = f'{name + "_"}wrong.log'
        self.infoFile = f'{name + "_"}info.log'
        self.errorFile = f'{name + "_"}error.log'
        self.debuggerFile = f'{name + "_"}debugger.log'
    def info(self,msg):
        try:
            if(os.path.exists(self.infoFile) and os.path.getsize(self.infoFile)/float(1024) >500):
                self.mode = 'w'
            with open(self.infoFile,self.mode)as df:
                df.write(f'{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())} [Info Message] ======>>>> {msg}\n')
                print(f'\033[32m{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())} [Info Message] ======>>>> {msg}\033[0m')
        except BaseException as e:
            pass
    def wrong(self,msg):
        try:
            if (os.path.exists(self.wrongFile) and os.path.getsize(self.wrongFile)/float(1024) > 500):
                self.mode = 'w'
            with open(self.wrongFile, self.mode)as df:
                df.write(f'{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())} [Wrong Message] ======>>>> {msg}\n')
                print(f'\033[33m{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())} [Wrong Message] ======>>>> {msg}\033[0m')
        except BaseException as e:
            pass
    def error(self,msg):
        try:
            if (os.path.exists(self.errorFile)  and os.path.getsize(self.errorFile)/float(1024) > 500):
                self.mode = 'w'
            with open(self.errorFile, self.mode)as df:
                df.write(f'{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())} [Error Message] ======>>>> {msg}\n')
                print(f'\033[31m{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())} [Error Message] ======>>>> {msg}\033[0m')
        except BaseException as e:
            pass
    def debugger(self,msg):
        try:
            if (os.path.exists(self.debuggerFile)  and os.path.getsize(self.debuggerFile)/float(1024) > 500):
                self.mode = 'w'
            with open(self.debuggerFile, self.mode)as df:
                df.write(f'{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())} [Debugger Message] ======>>>> {msg}\n')
                print(f'\033[34m{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())} [Debugger Message] ======>>>> {msg}\033[0m')
        except BaseException as e:
            pass
