# -*- coding: utf-8 -*-
import scrapy
import time


class CurlieSpider(scrapy.Spider):
    name = 'curlie'
    allowed_domains = ['curlie.org']
    start_urls = ['http://curlie.org/ja/']

    def parse(self, response):
        for quote in response.css('#category-section'):
            category_url = quote.css('div > h2 > a::attr(href)').extract()
            

