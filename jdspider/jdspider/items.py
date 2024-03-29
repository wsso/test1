# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JdspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()  # 标题

    price = scrapy.Field()  # 价格

    url = scrapy.Field()  # 商品链接

    info = scrapy.Field()  # 详细信息

    goods = scrapy.Field()  # 商品信息

    id = scrapy.Field()  # id
