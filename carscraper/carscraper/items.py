# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class Vehicle(Item):
    Brand = Field()
    Model = Field()
    Year = Field()
    Price = Field()
    Condition = Field()
    Type = Field()
    Fuel = Field()
    Horsepower = Field()
    Colour = Field()
    Cubature = Field()
    Image_urls = Field()
    Comfort = Field()
    Safety = Field()
    Other = Field()
    Publication_date = Field()
    Transmission = Field()
    Price_History = Field()
    Currency = Field()
    Comments = Field()
    Dealer = Field()
    Location = Field()
    Url = Field()
    Crawl_id = Field()
    Last_Seen = Field()
    Trail = Field()
