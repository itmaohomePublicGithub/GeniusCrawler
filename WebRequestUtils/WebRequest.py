#coding:utf-8
'''
WebRequestUtils  ---> WebRequest.py
date：2021-06-23
Anchor：Levon
'''

import requests
from LoggerUtils.Logger import Logger

class WebRequest():
    def __init__(self):
        self.session = requests.session()
        self.logger = Logger()
        self.result = ''
        self.emsg = {
            'code': 200,
            'msg': '',
            'data': []
        }
    def FetchJson(self,url,headers):
        try:
            headers['Accept-Encoding'] = 'gzip'
            self.result = self.session.get(url,headers=headers,timeout=30,verify=False)
            self.emsg['data'] = self.result
        except BaseException as e:
            self.logger.error(e)
            self.emsg['code'] = self.result.status_code
        return self.emsg
    def PostJson(self,url,headers,data):
        try:
            headers['Accept-Encoding'] = 'gzip'
            self.result = self.session.post(url,headers=headers,json=data,timeout=30,verify=False)
            self.emsg['data'] = self.result
        except BaseException as e:
            self.logger.error(e)
            self.emsg['code'] = self.result.status_code
        return self.emsg

