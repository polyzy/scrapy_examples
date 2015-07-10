# Overview
一些使用scrapy爬虫框架抓取的例子，目前暂时抓取了两个网站，[PM25.in](http://pm25.in)和[CSDN博客专栏](http://blog.csdn.net)

# Requirements
* Python: 2.7.6
* Scrapy: 0.24
* System: Linux 14.04 32bit

# Usage
```
$ cd csdn
$ scrapy crwal csdn
```
如果想把抓取结果保存成文本文件：
```
$ scrapy crwal csdn -o filename.json/filename.csv/filename.txt
```
