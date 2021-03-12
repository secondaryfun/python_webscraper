import scrapy


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['succubuspublishing.com/downloads/']
    start_urls = ['http://succubuspublishing.com/downloads//']

    def parse(self, response):
        pass
