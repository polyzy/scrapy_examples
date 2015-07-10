# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Pm25SpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    place = scrapy.Field()
    AQI = scrapy.Field()
    grade = scrapy.Field()
    pollution = scrapy.Field()
    pm25 = scrapy.Field()
    pm10 = scrapy.Field()
    CO = scrapy.Field()
    NO2 = scrapy.Field()
    O31 = scrapy.Field()
    O38 = scrapy.Field()
    SO2 = scrapy.Field()
    date = scrapy.Field()
    city = scrapy.Field()
