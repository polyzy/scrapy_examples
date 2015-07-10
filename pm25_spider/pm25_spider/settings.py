# -*- coding: utf-8 -*-

# Scrapy settings for pm25_spider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'pm25_spider'

SPIDER_MODULES = ['pm25_spider.spiders']
NEWSPIDER_MODULE = 'pm25_spider.spiders'
DOWNLOAD_DELAY = 0.5
#ITEM_PIPELINES = {
#    'pm25_spider.pipelines.Pm25SpiderPipeline':300
#}
LOG_ENABLED = False
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'pm25_spider (+http://www.yourdomain.com)'
