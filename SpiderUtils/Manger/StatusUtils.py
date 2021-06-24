#coding:utf-8
'''
SpiderUtils  ---> StatusUtils.py
date：2021-06-23
Anchor：Levon
'''

from enum import Enum

class Status(Enum):
    STOP = 0
    Runing = 1
    Finsh = 2
    Cancel = 3
    Failure = 4

class TasksStatus():
    def __init__(self):
        self.status = Status.STOP
    def SetStatus(self,status):
        try:
            self.status = Status[status]
        except BaseException as e:
            pass
    def GetStatus(self):
        return self.status
