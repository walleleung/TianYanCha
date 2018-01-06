# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from scrapy.http import HtmlResponse
import time
from scrapy.conf import settings
import random
import base64

class SeleniumMiddleware(object):
    def process_request(self, request, spider):
        """ selenium 处理没有数据的代码"""

        agent = random.choice(settings['USER_AGENTS'])
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap["phantomjs.page.settings.userAgent"] = (agent)

        # 创建webdriver对象，禁止加载图片资源
        driver = webdriver.PhantomJS(desired_capabilities=dcap, service_args=['--load-images=false'])

        # print request.url
        driver.get(request.url)
        time.sleep(3)
        body = driver.page_source
        url = driver.current_url
        driver.quit()

        # 返回给引擎，引擎交给spider处理response
        return HtmlResponse(url, body=body, encoding='utf-8', request=request)

# # 处理随即User-Agent
# class RandomUserAgent(object):
#     def process_request(self, request, spider):
#         user_agent = random.choice(USER_AGENT_LIST)
#         # request.headers.setdefault("User-Agent", user_agent)
#         request.headers["User-Agent"] = user_agent

# # 给请求设置代理,有个base64的认证
# class ProxyMiddleware(object):
#
#     def process_request(self, request, item):
#         proxy = "122.114.214.159:16816"
#         request.meta["proxy"] = "http://" + proxy
#
#         passwd = "mr_mao_hacker:sffqry9r"
#         b_passwd = base64.b16decode(passwd)
#         request.headers["Proxy-Authorization"] = "Basic " + b_passwd #  Basic 后边有个空格
