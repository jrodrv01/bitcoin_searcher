import scrapy
from scrapy.selector import Selector
from scrapy.http import HtmlResponse

class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'toscrape-xpath'
    start_urls = [
        'https://www.forocoches.com/foro/showthread.php?t={tx}'.format(tx=tx)
            for tx in range(1, 7300000) 
    ]

    def parse(self, selector):
        
        for quote in selector.xpath('//div[starts-with(@id, "post_message_")]'):
            yield {

                'text': quote.xpath('//text()').getall(),
                

                
            }


