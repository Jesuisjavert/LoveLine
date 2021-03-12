import scrapy
import pandas as pd
from time import sleep

from datetime import datetime as dt

class DaummapSpider(scrapy.Spider):
    name = 'daumMap'
    allowed_domains = ['map.kakao.com']
    start_urls = ['http://map.kakao.com']
    # custom_settings= {
    #     'DOWNLOADER_MIDDLEWARES': {
    #         'loveLine.middlewares.LovelineDownloaderMiddleware': 500
    #     }
    # }
    
 
    def start_requests(self):
        data = pd.read_csv("./data/test.csv")
        print(data["0"])

        for url in data["0"]:
            yield scrapy.Request( url=url, callback=self.parse, method='GET', encoding='utf-8')
 
    def parse(self, response):
        # contents = response.xpath('//*[@id="main_content"]/div[1]/ul/li')
        # print(response.text)
        # title = response.xpath('//*[@id="mArticle"]/div[1]/div[1]/div[2]/div/h2').text
        print("===================================================================")
        print(response.text)
        print("===================================================================")
        title = 'z'
        item = {
            'title': title.strip() if title else title
        }

        yield item
    
    # def parse(self, response):
    #     print(response.text)
