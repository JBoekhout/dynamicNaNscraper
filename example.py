# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'funda'

    custom_settings = {'CONCURRENT_REQUESTS': 1,
 'DOWNLOAD_DELAY': 3,
 'USER_AGENT':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5)'
}
    # i = 0
    start_urls = ['https://www.funda.nl/koop/gemeente-ijsselstein/+15km/']
    ##keeping count         
    #i += 1
    #log('{} request(s) parsed'.format())

    def parse(self, response):
        hitlist = response.css('li.search-result')
        for hit in hitlist:
            print(hit.extract())
	    #//fundafilter.py
    

