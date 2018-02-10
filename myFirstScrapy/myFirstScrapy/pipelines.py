# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from myFirstScrapy import settings
import pymongo

class MyfirstscrapyPipeline(object):

    def open_spider(self, spider):
        self.file = open('items.jl', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):#会在spider中有函数yield item 时触发么？
        line = json.dumps(dict(item)) + '\n'
        self.file.write(line)
        return item

