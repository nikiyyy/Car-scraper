from scrapy.spiders import Spider
from scrapy import Selector, Request
from ..items import Vehicle

class Mixin():
    retailer = 'cars-bg'
    allowed_domains = ['www.cars.bg', 'g1.cars.bg']
    start_urls = ["https://www.cars.bg/sitemap.xml"]

class ParseSpider():
    def parse(self, response):
        vehicle = Vehicle()
        vehicle['Brand'] = self.product_name(response)
        return vehicle

    def product_name(self, response):
        return response.css('.mdc-layout-grid h2').get()

class CarsbgXMLSpider(Mixin, Spider):
    name = Mixin.retailer + "-crawl"
    parse_spider = ParseSpider()
    xml_type = "html"

    def parse(self, response):
        xml_selector = Selector(text=response.text, type=self.xml_type)
        raw_urls = xml_selector.xpath(f'//loc/text()').extract()

        yield from [response.follow(url, self.parse_pages) for url in raw_urls ] #limiter

    def parse_pages(self, response):
        xml_selector = Selector(text=response.text, type=self.xml_type)
        raw_urls = xml_selector.xpath(f'//loc/text()').extract()
        
        yield from [response.follow(url, self.parse_item) for url in raw_urls[:5] ] #limiter

    def parse_item(self, response):
        return self.parse_spider.parse(response)