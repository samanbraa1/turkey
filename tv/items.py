# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TvItem(scrapy.Item):
    # define the fields for your item here like:
     name = scrapy.Field()

     img = scrapy.Field()

     price = scrapy.Field()
     #tozih marboote
     des = scrapy.Field()
      # ads date
     date = scrapy.Field()
     #site source
     site = scrapy.Field()


