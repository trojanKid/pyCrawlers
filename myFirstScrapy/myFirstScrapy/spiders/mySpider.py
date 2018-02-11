import scrapy
import re
from bs4 import BeautifulSoup
from scrapy.http import Request
from myFirstScrapy.items import MyfirstscrapyItem


class mySpider(scrapy.Spider):
    name = 'myspider'

    def start_requests(self):
        urls = [
            "https://www.linkedin.com/mynetwork/"
        ]
        for url in urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        # item = MyfirstscrapyItem()
        # authors = BeautifulSoup(response.text, 'lxml').find_all('small', itemprop='author')
        # quotes = BeautifulSoup(response.text, 'lxml').find_all('span', itemprop="text")
        # nums = len(authors)
        # for i in range(0, nums-1):
        #     item['author'] = authors[i].get_text()
        #     print(authors[i].get_text())
        #     item['quote'] = quotes[i].get_text()
        #     print(quotes[i].get_text())
        #     yield item
        print(response.text)