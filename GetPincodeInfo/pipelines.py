# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
import re
import sys

class JustdialPipeline(object):
    host = 'localhost'
    user = 'root'
    password = 'root'
    db = 'scrapydb'

    def __init__(self):
        self.connection = pymysql.connect(self.host, self.user, self.password, self.db)
        self.cursor = self.connection.cursor()


    def process_item(self, item, spider):
        try:
            #self.cursor.execute("INSERT INTO quotes (quote) VALUES (%s)", (item['joke_text']))
            self.cursor.execute("INSERT INTO pincodeinfo_data (pincode,area,region,source) VALUES (%s,%s,%s,%s)", (item['pincode'],item['area'],"kolkata-howrah","pincodeinfo"))
            self.connection.commit()
        except Exception as e:
            print("Error:",e)
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.connection.close()