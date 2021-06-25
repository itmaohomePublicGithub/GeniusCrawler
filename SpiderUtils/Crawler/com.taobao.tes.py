#coding:utf-8
'''
SpiderUtils  ---> TaoBaoModule.py
date：2021-06-23
Anchor：Levon
'''
import json
import time

from SpiderUtils.Manger.SpiderManger import SpiderManager
from SpiderUtils.Module.TaoBaoModule import ModuleManger

class Tao():
    def __init__(self):
        self.SpiderManager = SpiderManager(SpiderName="com.taobao.tes")
        self.ModuleManager = ModuleManger(self.SpiderManager)

    def FetchSellCount(self,itemId):
        url = f'https://sycm.taobao.com/mc/ci/config/rival/item/queryItem.json?firstCateId=1801&sellerType=-1&rivalType=item&keyword={itemId}&_={int(time.time() * 1000)}&token=d30c625ff'
        referer = f'https://sycm.taobao.com/mc/ci/item/analysis?cateFlag=1&cateId=1801&dateRange=2021-04-25|2021-04-25&dateType=today&spm=a21ag.11815275.LeftMenu.d574.3c5250a5kDSkh6&rivalItem1Id=&rivalItem2Id=&selfItemId='
        headers = {
            'Host': 'sycm.taobao.com',
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'sec-ch-ua': 'Google Chrome 81',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Origin-Policy': '0',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Dest': 'document',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Referer': f'https://detail.tmall.com/item.htm?id={itemId}'
        }
        headers['Referer'] = referer
        self.SpiderManager.FetchForword(url,headers=headers)

    def main(self):
        self.SpiderManager.SetHandlerData(self.ModuleManager.SaveData)
        try:
            self.ModuleManager.CreateTable("TaoGoods")
        except:
            pass
        GoodsList = ['612357753445',"569336348562","627118700346","582269452395","611025448985"]
        for goods in GoodsList:
            self.FetchSellCount(goods)
        self.SpiderManager.Fetch(self.Callback)

    def Callback(self,result):
        for item in result:
            if item is not None:
                data = json.loads(item)
                ite = data.get('data', None)['data']
                title = ite['name']
                url = ite['linkUrl']
                userId = ite['userId']
                dp = {
                    'title':title,
                    'url':url,
                    'user_id':userId
                }
                yield dp

b = Tao()
b.main()
