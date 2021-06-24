#coding:utf-8
'''
SpiderUtils  ---> TaoBaoModule.py
date：2021-06-24
Anchor：Levon
'''


class ModuleManger():
    def __init__(self,SpiderManager):
        self.db = None
        self.SpiderManager = SpiderManager
    def SaveData(self,items):
        for item in items:
            self.SpiderManager.Logger.info('【模拟入库状态】：正在更新一条记录到数据库！')