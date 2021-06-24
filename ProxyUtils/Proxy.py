#coding:utf-8
'''
ProxyUtils  ---> Proxy.py
date：2021-06-23
Anchor：Levon
'''


class Proxy():
    def __init__(self):
        self.proxy = None
        self.host = None
        self.port = None
        self.userName = None
        self.Password = None
        self.protocol = "https"
    def SetProxy(self,ip,port,userName=None,Password=None,Protocol='https'):
        self.host = ip
        self.port = port
        self.userName = userName
        self.Password = Password
        self.protocol = Protocol
    def GetProxyForJson(self):
        self.proxy = {self.protocol:f"{self.protocol}://{self.host}:{self.port}"}
        return self
    def GetProxyForStr(self):
        self.proxy = f"{self.protocol}://{self.host}:{self.port}"
        return self