# -*- coding: utf-8 -*-
import scrapy
import re
import sys
sys.path.append("..")
from tianyancha.items import CompanyInfo
from tianyancha.start_url import StartUrl

class TycspiderSpider(scrapy.Spider):
    name = 'tycSpider'
    allowed_domains = ['http://www.tianyancha.com/']
    # start_urls = ['http://www.tianyancha.com//']
    start_urls = StartUrl.Urls

    def parse(self, response):
        # company_list_url = re.findall(r'http://www.tianyancha.com/company/\d+')
        company_list_url = response.xpath("//a[@class='query_name sv-search-company f18 in-block vertical-middle']/@href")
        for url in company_list_url:
            yield scrapy.Request(url, callback=self.company_page)

    def company_page(self, response):
        """公司信息提取"""
        company_name = response.xpath("//a[@class='query_name sv-search-company f18 in-block vertical-middle']/span/text()").extract_first()
        Legal_peopel = response.xpath("//a[@class='legalPersonName']/text()").extract.first()
        registered_capital = response.xpath("//div[@class='title overflow-width']/span/text()").extract()[0]
        Registratio_time = response.xpath("//div[@class='title overflow-width']/span/text()").extract()[1]
        state = response.xpath("//div[@class='statusTypeNor in-block f12 vertical-middle ml10 statusType1']/text()")
        region = response.xpath("//span[@class='pr30']/text()").extract.first()
        score = response.xpath("//span[@class='c9 f20']/text()").extract.first()
        telephone = response.xpath("//span[@class='overflow-width over-hide vertical-bottom in-block']/text()").extract.first()
        link = response.xpath("//a[@class='query_name sv-search-company f18 in-block vertical-middle']/@href").extract.first()

        items = CompanyInfo()
        items['_id'] = re.compile(r'\d+').findall(link)
        items['company_name'] = company_name
        items['Legal_peopel'] = Legal_peopel
        items['registered_capital'] = registered_capital
        items['Registratio_time'] = Registratio_time
        items['state'] = state
        items['region'] = region
        items['score'] = score
        items['telephone'] = telephone

        yield items

