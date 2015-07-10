# -*- coding: utf-8 -*-
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from csdn_spider.items import CsdnSpiderItem
from scrapy.http import Request


class CsdnSpider(CrawlSpider):
    name = 'csdn'
    allow_domains = ["blog.csdn.net"]
    start_urls = ["http://blog.csdn.net/column.html"]

    def parse(self, response):
        for sel in response.xpath("//div[@class='blog_list']//h1/a[2]"):
            pagelink = sel.xpath('@href').extract()[0].strip()
            link = "http://blog.csdn.net" + pagelink
            yield Request(link, callback=self.parse_title)

    def parse_title(self, response):
        items = []
        item = CsdnSpiderItem()
        for sel in response.xpath("//div[@class='blog_list']//h1"):
            item['link'] = sel.xpath('a[2]/@href').extract()[0].strip()
            item['title'] = sel.xpath('a[2]/text()').extract()[0].strip()
            print item['title']
            items.append(item)
        return items
