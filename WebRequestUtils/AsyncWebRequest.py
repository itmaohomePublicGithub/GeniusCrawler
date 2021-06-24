#coding:utf-8
'''
WebRequestUtils  ---> AsyncWebRequest.py
date：2021-06-23
Anchor：Levon
'''
import asyncio


from SpiderUtils.Manger.StatusUtils import Status
import aiohttp


class AsyncWebRequest():
    def __init__(self,StatusObj,Logger,timeout=30,):
        self.statusObj = StatusObj
        self.logger = Logger
        self.timeout = timeout
    async def Fetch(self,method, url,headers=None,data=None,**kwargs):
        try:
            headers = headers or None
            if headers is None:headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (GeniusCrawler; Version:1.0)"
            if method.upper() == "POST":
                async with aiohttp.ClientSession()as session:
                    async with session.post(url=url,headers=headers,data=data,**kwargs) as response:
                        # self.logger.info(f"【AsyncFetchStatus】：{response.status}")
                        return await response.text()
            else:
                async with aiohttp.ClientSession()as session:
                    async with session.get(url=url,headers=headers,**kwargs) as response:
                        # self.logger.info(f"【AsyncFetchStatus】：{response.status}")
                        return await response.text()
        except BaseException as e:
            self.statusObj.status = Status.Failure
            self.logger.error(f'【AsyncFetchException】：{e}')

    async def FetchJson(self,method, url,headers=None,data=None,**kwargs):
        try:
            headers = headers or None
            if headers is None:headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (GeniusCrawler; Version:1.0)"
            if method.upper() == "POST":
                async with aiohttp.ClientSession()as session:
                    async with session.post(url=url,headers=headers,data=data,**kwargs) as response:
                        # self.logger.info(f"【AsyncFetchStatus】：{response.status}")
                        return await response.json()
            else:
                async with aiohttp.ClientSession()as session:
                    async with session.get(url=url,headers=headers,**kwargs) as response:
                        # self.logger.info(f"【AsyncFetchStatus】：{response.status}")
                        return await response.json()
        except BaseException as e:
            self.statusObj.status = Status.Failure
            self.logger.error(f'【AsyncFetchJsonException】：{e}')

