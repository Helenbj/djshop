# -*- coding: utf-8 -*-

import pymysql
import datetime
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DjspiderPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host="39.106.98.42", user="developer", passwd="123wasd", db="djshop", charset="utf8")

    def process_item(self, item, spider):
        title = item['title']
        lkurl = item['lkurl']
        imgurl = item['imgurl']
        merchant = item['merchant']
        category = item['category']
        date = str(datetime.date.today())
        sql = 'insert into wechat_discountinfo(title,lkurl,imgurl,merchant,category,date) values("' + title + '","' + lkurl + '","' + imgurl + '","' + merchant + '","' + category + '","' + date + '");'
        print(sql)
        self.conn.query(sql)
        self.conn.commit()
        return item

    def close_spider(self, spider):
       self.conn.close()
