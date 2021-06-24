#coding:utf-8
'''
SpiderUtils  ---> com.taobao.tes.py
date：2021-06-23
Anchor：Levon
'''
import aiohttp

from SpiderUtils.Manger.SpiderManger import SpiderManager

def dv(dv):
    print(dv)

def callback(result):
    for i in result:
        print(i)
        yield
b = SpiderManager(SpiderName="com.taobao.tes")
b.SetHandlerData(dv)
for i in range(2):
    b.FetchForword('https://www.taobao.com')
b.Fetch(callback)
