#coding:utf-8
'''
SpiderUtils  ---> SpiderManager.py
date：2021-06-23
Anchor：Levon
'''
import random
import sys
import time
from LoggerUtils.Logger import Logger
from DataBaseUtils.RedisDB import RedisDB
from WebRequestUtils.WebRequest import WebRequest
from WebRequestUtils.AsyncWebRequest import AsyncWebRequest
from SpiderUtils.Manger.StatusUtils import TasksStatus,Status
from SpiderUtils.Manger.EventCallback import EventCallback

class SpiderManager():
    def __init__(self,SpiderName,status=Status.STOP):
        if SpiderName == None:
            print('实例化SpiderManager前需要先设置爬虫名称！')
            sys.exit()
        self.eventCallback = EventCallback()
        self.SpiderName = SpiderName
        self.Redis = RedisDB()
        self.WebRequest = WebRequest()
        self.TaskStatus = TasksStatus()
        self.TaskStatus.SetStatus(status)
        self.Logger = Logger(self.SpiderName)
        self.AsyncRequest = AsyncWebRequest(self.TaskStatus,self.Logger)
        self.HandlerData = None
    def SetHandlerData(self,dv):
        self.HandlerData = dv
    def PushTasks(self,clo_name,value):
        """
        PushTasks，向任务队列插入一条任务
        :param clo_name: 队列名称，str类型（即：Redis键名称）
        :param value: 任务实际值，通常为字典类型（即：Redis存储的值）
        :return: 无返回
        """
        self.Redis.lpush(clo_name,value)
    def PoPTasks(self,clo_name):
        """
        PoPTasks，任务队列获取一条任务
        :param clo_name: 队列名称，str类型（即：Redis键名称）
        :return: 返回一条记录或为None
        """
        self.Redis.lpop(clo_name)
    def SaveData(self,col,data):
        pass
    def SyncStatus(self):
        return self.TaskStatus.GetStatus()
    def FetchForword(self,url,method='GET',headers=None,data=None):
        """
        FetchForword 异步请求框架前置迭代方法，通常用于单或批量任务时生成一个RequestTasks任务列表。
        :param url: 请求的资源URI
        :param method: 请求的资源方法
        :param headers: 请求的资源头部
        :param data: 请求的资源Body
        :return: 无返回值
        """
        self.eventCallback.handler_async_push_tasks_callback(self.AsyncRequest.Fetch, method=method.upper(), url=url,headers=headers, data=data)
    def Fetch(self,callback = None):
        """
        Fetch 异步请求框架批量请求方法，通常用于处理RequestTasks列队，注调用该方法前需先执行FetchForword方法生成迭代。
        :param callback: 异步回调函数，支持解析异步返回的数据
        :return: 返回callbackResult或Result
        """
        if callback == None:
            return self.eventCallback.handler_async_start_callback(lambda x: self.eventCallback.GCTasks.clear(),self.HandlerData)
        return self.eventCallback.handler_async_start_callback(callback,self.HandlerData)



