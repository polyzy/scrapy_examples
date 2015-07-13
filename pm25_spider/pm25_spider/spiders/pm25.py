# -*- coding: utf-8 -*-
from scrapy.spider import Spider
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from pm25_spider.items import Pm25SpiderItem
from scrapy.http import Request
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')


class Pm25Spider(Spider):
    name = 'pm25'
    start_urls = ['http://pm25.in']

    def parse(self, response):
        for sel in response.xpath("//ul[@class='unstyled']/div/li/a"):
            pagelink = sel.xpath("@href").extract()[0].strip()
            link = 'http://pm25.in' + pagelink
            yield Request(link, callback=self.parse_item)

    def no_data(self, value):
        if not value or value[0] == "_":
            result = -1
        else:
            result = value[0]
        return result

    def parse_item(self, response):
        items = []
        date = time.time()
        for sel in response.xpath("//tbody/tr"):
            item = Pm25SpiderItem()

            place = sel.xpath('td[1]/text()').extract()
            city = response.xpath("//div[@class='city_name']/h2/text()").extract()
            item['city'] = self.no_data(city)
            item['place'] = self.no_data(place)
            # item['date'] = response.xpath("//div[@class='live_data_time]/p")
            AQI = sel.xpath('td[2]/text()').extract()
            item['AQI'] = self.no_data(AQI)

            grade = sel.xpath('td[3]/text()').extract()
            item['grade'] = self.no_data(grade)

            pollution = sel.xpath('td[4]/text()').extract()
            item['pollution'] = self.no_data(pollution)

            pm25 = sel.xpath('td[5]/text()').extract()
            item['pm25'] = int(self.no_data(pm25))

            pm10 = sel.xpath('td[6]/text()').extract()
            item['pm10'] = int(self.no_data(pm10))

            CO = sel.xpath('td[7]/text()').extract()
            item['CO'] = float(self.no_data(CO))

            NO2 = sel.xpath('td[8]/text()').extract()
            item['NO2'] = int(self.no_data(NO2))

            O31 = sel.xpath('td[9]/text()').extract()
            item['O31'] = int(self.no_data(O31))

            O38 = sel.xpath('td[10]/text()').extract()
            item['O38'] = int(self.no_data(O38))

            SO2 = sel.xpath('td[11]/text()').extract()
            item['SO2'] = int(self.no_data(SO2))
            item['date'] = int(date)
            print item['AQI'], item['grade'], item['pollution'], item['pm25'],\
                item['pm10'], item['CO'], item['NO2'], item['O31'], item['O38'],\
                item['SO2'], item['date']
            items.append(item)

        return items
