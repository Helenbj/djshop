# -*- coding: utf-8 -*-
import scrapy
import urllib.request
from scrapy.http import Request
from djspider.items import DjspiderItem

class DiscountSpiderSpider(scrapy.Spider):
    name = 'discount_spider'
    allowed_domains = ['quanmama.com']
#    start_urls = ['http://www.quanmama.com/staticfiles/HomeMallPanel.html']

    def start_requests(self):
        fp = urllib.request.urlopen('http://www.quanmama.com/staticfiles/HomeMallPanel.html')
        html = fp.read()
        sel = scrapy.Selector(text=html, type="html")
        category_list = sel.xpath('//div[@class="mall-pane JPanel90"]/div[@class="list-shop-word"]/div')
        for category in category_list:
            category_str = category.xpath('h4/text()').extract()[0]
            category_str = category_str.strip('\r').strip('\n').strip(' ')
            if category_str == '用车' or category_str == '外卖' or category_str == '电影票' or category_str == '团购网站':
                merchant_list = category_list.xpath('ul/li')
                for merchante in merchant_list:
                     tourl = merchante.xpath('span/a/@href').extract()[0]
                     yield Request(tourl)
            
    def parse(self, response):
        item = DjspiderItem()
        sel = scrapy.Selector(response)
        li_list = response.xpath('//ul[@id="J_CouponsList"]/li')
        for li in li_list:
            item['title'] = li.xpath('div/h2/span/a/text()').extract()[0].strip('\r').strip('\n').strip(' ')
            item['lkurl'] = li.xpath('div/h2/span/a/@href').extract()[0].strip('\r').strip('\n').strip(' ')
            item['imgurl'] = li.xpath('div/div[@class="coupon"]/span[@class="left"]/span[@class="store-logo"]/a/img/@src').extract()[0].strip('\r').strip('\n').strip(' ')
            item['keywords'] = li.xpath('div/div[@class="coupon"]/span[@class="left"]/span[@class="store-logo"]/a/img/@title').extract()[0].strip('\r').strip('\n').strip(' ')
            yield item
        
