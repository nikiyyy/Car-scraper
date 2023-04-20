# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class Car(Item):
    Brand = Field()
    Model = Field()
    Year = Field()
    Price = Field()
    Price_History = Field()
    Currency = Field()
    Comments = Field()
    Dealer = Field()
    Location = Field()
    Url = Field()
    Crawl_id = Field()
    Last_Seen = Field()
    Trail = Field()
