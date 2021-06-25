#coding:utf-8
'''
DataBasesUtils  ---> SQLiteDB.py
date：2021-06-23
Anchor：Levon
'''

import sqlite3
from LoggerUtils.Logger import Logger

class SQLiteDB():
    def __init__(self,dbpath='./sql.db'):
        self.logger = Logger()
        self.db = sqlite3.connect(dbpath)
        self.cursor = self.db.cursor()
    def CreateTable(self,sql,**args):
        try:
            self.db = sqlite3.connect('./sql.db')
            self.cursor = self.db.cursor()
            if len(args) == 0:
                self.cursor.execute(sql)
            else:
                self.cursor.execute(sql, args)
            self.db.commit()
        except BaseException as e:
            self.logger.error(f"【表名创建失败】：{e}")
        finally:
            self.db.close()

    def InsertData(self,sql,**args):
        try:
            self.db = sqlite3.connect('./sql.db')
            self.cursor = self.db.cursor()
            if len(args) == 0:
                self.cursor.execute(sql)
            else:
                self.cursor.execute(sql,args)
            self.db.commit()
        except BaseException as e:
            self.logger.error(f'【SQL语句插入异常】：{e}')
    def DropData(self,sql,**args):
        try:
            self.db = sqlite3.connect('./sql.db')
            self.cursor = self.db.cursor()
            if len(args) == 0:
                self.cursor.execute(sql)
            else:
                self.cursor.execute(sql, args)
            self.db.commit()
        except BaseException as e:
            self.logger.error(f'【删除失败】：{e}')
    def UpdateData(self,sql,**args):
        try:
            self.db = sqlite3.connect('./sql.db')
            self.cursor = self.db.cursor()
            if len(args) == 0:
                self.cursor.execute(sql)
            else:
                self.cursor.execute(sql, args)
            self.db.commit()
        except BaseException as e:
            self.logger.error(f'【SQL语句更新异常】：{e}')
    def SearchData(self,sql,**args):
        try:
            self.db = sqlite3.connect('./sql.db')
            self.cursor = self.db.cursor()
            if len(args) == 0:
                self.cursor.execute(sql)
            else:
                self.cursor.execute(sql, args)
            self.db.commit()
        except BaseException as e:
            self.logger.error(f'【SQL语句查询异常】：{e}')