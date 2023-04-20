from scrapy.spiders import Spider
from scrapy import Selector, Request
from ..items import Car

class Mixin():
    retailer = 'cars-bg'
    allowed_domains = ['www.cars.bg', 'g1.cars.bg']
    start_urls = ["https://www.cars.bg/sitemap.xml"]

class ParseSpider(Spider):
    def parse(self, response):
        pass


class CarsbgXMLSpider(Mixin, Spider):
    name = Mixin.retailer + "-crawl"
    parse_spider = ParseSpider

    def parse(self, response):
        xml_selector = Selector(text=response.text, type="html")
        raw_urls = xml_selector.xpath(f'//loc/text()').extract()

        yield from [response.follow(url, self.parse_item) for url in raw_urls ]

    def parse_item(self, response):
        xml_selector = Selector(text=response.text, type="html")
        raw_urls = xml_selector.xpath(f'//loc/text()').extract()

        yield from [Request(url, ParseSpider.parse) for url in raw_urls ]