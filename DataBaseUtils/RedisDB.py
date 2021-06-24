#coding:utf-8
'''
DataBasesUtils  ---> RedisDB.py
date：2021-06-23
Anchor：Levon
'''
import redis
import json

class RedisDB():
    def __init__(self):
        pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
        self.db = redis.Redis(connection_pool=pool)

    def lpush(self, key, value):
        self.db.lpush(key, value)

    def lpushx(self, keys, values):
        for item in range(len(keys)):
            self.db.lpush(keys[item], values[item])

    def lpop(self, key):
        data = self.db.lpop(key)
        if data == None:
            return None
        else:
            return data.decode('utf-8')

    def lcount(self, key):
        return self.db.llen(key)

    def lscran(self,keyName):
        bb = self.db.lrange(keyName, 0, -1)
        ts = []
        for item in bb:
            tt = json.loads((item.decode('utf-8')).replace("'", "\"").replace('None', 'null'))
            if tt['uri'] not in ts:
                ts.append(tt['uri'])
        return ts