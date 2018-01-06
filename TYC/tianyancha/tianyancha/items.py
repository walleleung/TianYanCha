# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CompanyInfo(scrapy.Item):
    # 公司id
    _id = scrapy.Field()
    # 公司名称
    company_name = scrapy.Field()
    # 法定代表人
    Legal_peopel = scrapy.Field()
    # 注册资本
    registered_capital = scrapy.Field()
    # 注册时间
    Registratio_time = scrapy.Field()
    # 经营状态
    state = scrapy.Field()
    # 地区
    region = scrapy.Field()
    # 企业评分
    score = scrapy.Field()
    # 企业电话
    telephone = scrapy.Field()
    # 企业链接
    link = scrapy.Field()