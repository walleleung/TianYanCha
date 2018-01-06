# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import json
from tianyancha.items import CompanyInfo
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# class MongoDBPipeline(object):
#     """把数据存入到mongodb数据库"""
#     def __init__(self):
#         # pymongo.MongoClient创建MongoDB连接
#         client = pymongo.MongoClient("localhost", 27017)
#         # 指定数据库
#         db = client['tianyancha']
#         # 指定存向的表名
#         self.company_info = db['company_info']
#
#     def process_item(self,item, spider):
#         if isinstance(item,CompanyInfo):
#             self.company_info.insert(dict(item))
#
#         return item



class TianyanchaPipeline(object):
    """把数据存入到以json格式的文件"""
    def __init__(self):
        self.f = open("tianyan.json", "w")

    def process_item(self, item, spider):
        if isinstance(item, CompanyInfo):
            content = json.dumps(dict(item), ensure_ascii=False) + "\n"
            self.f.write(content)
        return item

    def close_spider(self, spider):
        self.f.close()