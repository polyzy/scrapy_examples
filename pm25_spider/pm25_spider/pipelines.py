#!/usr/bin/python
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
# from twisted.enterprise import adbapi
# from scrapy.http import Request
from scrapy.contrib.pipeline.images import ImagesPipeline
import time
import  MySQLdb
import MySQLdb.cursors

class Pm25SpiderPipeline(object):
      def __init__(self):
            self.conn = MySQLdb.connect(host='localhost', user='root', passwd='1',db='pm25',charset='utf8')
            self.cursor = self.conn.cursor()

      def process_item(self, item, spider):
            print item['AQI'],item['grade'],item['pollution'],item['pm25'],item['pm10'],item['CO'],item['NO2'],item['O31'],item['O38'],item['SO2'],item['date'] 
            self.cursor.execute('insert into data (city,place,AQI,grade,pollution,pm25,pm10,CO,NO2,O31,O38,SO2,date) values ("%s","%s",%s,"%s","%s",%s,%s,%s,%s,%s,%s,%s,%s); '%(item['city'],item['place'],item['AQI'],item['grade'],item['pollution'],item['pm25'],item['pm10'],item['CO'],item['NO2'],item['O31'],item['O38'],item['SO2'],item['date']))
            self.conn.commit()
            return item