# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import log
from twisted.enterprise import adbapi
from scrapy.http import Request
from scrapy.contrib.pipeline.images import 	ImagesPipeline
import time
import MySQLdb
import MySQLdb.cursors
import socket
import select
import sys
import os
import errno

class CsdnSpiderPipeline(object):
	def __init__(self):
		self.dbpool = adbapi.ConnectionPool('MySQLdb',
			db = 'csdn',
			user = 'root',
			passwd = '1',
			cursorclass = MySQLdb.cursors.DictCursor,
			charset = 'utf8',
			use_unicode = False
			)

        def process_item(self, item, spider):
            query = self.dbpool.runInteraction(self._conditional_insert, item)
            return item

    def _conditional_insert(self, tx, item):
        if item.get('title'):
            tx.execute('insert into article values(%s,%s)',(item['title'],item['link']))
