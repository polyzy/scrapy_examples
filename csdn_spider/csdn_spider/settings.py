# -*- coding: utf-8 -*-

# Scrapy settings for csdn_spider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'csdn_spider'

SPIDER_MODULES = ['csdn_spider.spiders']
NEWSPIDER_MODULE = 'csdn_spider.spiders'
DOWNLOAD_DELAY = 0.5
LOG_ENABLED = False
# ITEM_PIPELINES = ['csdn_spider.pipelines.CsdnSpiderPipeline']
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'csdn_spider (+http://www.yourdomain.com)'
