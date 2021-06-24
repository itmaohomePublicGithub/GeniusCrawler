#coding:utf-8
'''
SpiderUtils  ---> TaoBaoModule.py
date：2021-06-23
Anchor：Levon
'''

from SpiderUtils.Manger.SpiderManger import SpiderManager
from SpiderUtils.Module.TaoBaoModule import ModuleManger

class Tao():
    def __init__(self):
        self.SpiderManager = SpiderManager(SpiderName="com.taobao.tes")
        self.ModuleManager = ModuleManger(self.SpiderManager)

    def main(self):
        self.SpiderManager.SetHandlerData(self.ModuleManager.SaveData)
        for i in range(50):
            self.SpiderManager.FetchForword("https://www.taobao.com")
        self.SpiderManager.Fetch(self.Callback)

    def Callback(self,result):
        for item in result:
            yield item

b = Tao()
b.main()
