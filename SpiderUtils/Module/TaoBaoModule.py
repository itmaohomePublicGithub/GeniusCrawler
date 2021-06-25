#coding:utf-8
'''
SpiderUtils  ---> TaoBaoModule.py
date：2021-06-24
Anchor：Levon
'''

from DataBaseUtils.SQLiteDB import SQLiteDB

class ModuleManger():
    def __init__(self,SpiderManager):
        self.SpiderManager = SpiderManager
        self.db = SQLiteDB()
    def CreateTable(self,tables_name):
        sql = '''
            CREATE TABLE %s (title varchar(255),user_id varchar(20),url varchar(255));
        ''' % tables_name
        self.db.CreateTable(sql)
    def SaveData(self,items):
        """
        实现数据保存方法，请务必以SaveData作为函数命名，否则回调会触发异常！
        :param items: 由yield返回的一个可迭代对象，通过in关键词遍历即可。
        :return:
        """
        for item in items:
            title = item['title']
            url = item['url']
            user_id = str(item['user_id'])
            sql = """
                INSERT INTO %s (title,user_id,url) VALUES('%s','%s','%s');
            """%("TaoGoods",title,user_id,url)
            self.db.InsertData(sql)
            self.SpiderManager.Logger.info('【模拟入库状态】：正在更新一条记录到数据库！')