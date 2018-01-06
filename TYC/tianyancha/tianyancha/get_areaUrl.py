# coding=utf-8
from selenium import webdriver
from lxml import etree


def get_url():
    driver = webdriver.PhantomJS()
    driver.get('http://www.tianyancha.com/')
    text = driver.page_source
    print(text)
    html = etree.HTML(text)
    url = html.xpath("//div[@class='industry_container js-industry-container bace_box']//a/@href")
    area_url = set(url)
    for each in area_url:
        with open("start_url1.py", "a") as f:
            f.write('"'+each+'"'+',\n')


if __name__ == "__main__":
    get_url()