#coding:utf-8
'''
SpiderUtils  ---> TaoBaoModule.py
date：2021-06-23
Anchor：Levon
'''

import json
import time

from SpiderUtils.Manger.SpiderManger import SpiderManager
# from WebRequestUtils.AsyncWebRequest import AsyncWebRequest
from SpiderUtils.Manger.StatusUtils import Status
from enum import Enum


class Tes():
    def __init__(self):
        self.manager = SpiderManager(SpiderName="com.taobao.tes")
        self.logger = self.manager.Logger

    def CreateTasks(self):
        for i in range(1,5001):
            data = {
                'page':i,
                'name':'taoTes',
                'status':str(self.manager.TaskStatus.GetStatus().value),
                'timestamp':f'{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}'
            }
            self.manager.PushTasks('taoTes',json.dumps(data))
            self.logger.info("【任务推送】：CreateTasks向Redis插入了一条新记录.")

bb = Tes()
bb.CreateTasks()















        # self.AsyncRequest = AsyncWebRequest(self.TaskStatus)

    # async def te(self):
    #     url = 'https://www.taobao.com'
    #     raise await self.AsyncRequest.Fetch("GET",url)

# b = Tes()
# task = []
# loop = asyncio.get_event_loop()
# for i in range(5):
#     task.append(loop.create_task(b.te()))
# loop.run_until_complete(asyncio.wait(task))

