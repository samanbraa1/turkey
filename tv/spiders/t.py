import scrapy
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import TvItem



class TSpider(scrapy.Spider):
    name = 't'
    allowed_domains = ['daire.trovit.com.tr']

    start_urls = ['https://daire.trovit.com.tr/satilik/daire',

    'https://daire.trovit.com.tr/satilik/villa',

    'https://daire.trovit.com.tr/satilik/apart',

    'https://daire.trovit.com.tr/satilik/residence',

    'https://daire.trovit.com.tr/kiralik/daire',

    'https://daire.trovit.com.tr/kiralik/villa',

    'https://daire.trovit.com.tr/kiralik/apart',
    ]



    def parse(self, response):
            # self.logger.info('Got successful response from {}'.format(response.url))
           i=0
           a=response.css('div.lh-city')
           link=a.css('a::attr(href)').getall()
           for link1 in link:
              w=a.css('a::attr(title)')[i].get()
              x= link1+f"/index.php/cod.search_homes/what_d.{w}/order_by.source_date/"
              i=i+1
              yield response.follow(url=x,callback=self.parse_cat)


    def parse_cat(self,response):
        w=response.css('div.snippet-wrapper.js-item-wrapper')

        for h in w:
                 items=TvItem()

                 #name
                 name=h.css('.item-title span::text').get()
                 #image
                 img=h.css('img::attr(src)').get()
                 #price
                 price= h.css('.actual-price::text').get()
                 #tozihat
                 des=h.css('div.item-description p::text').get()
                 #date of publish
                 date=h.css('span.item-published-time::text').get()
                 ##site source
                 site=h.css('span.item-source::text').get()

                 items['name']=name
                 items['img']=img
                 items['price']=price
                 items['des']=des
                 items['date']=date
                 items['site']=site


                 yield items


        npage=response.xpath("//*[@id='paginate']/a[contains(text(), 'Next')]/@href").get()
        if npage:
              yield scrapy.Request(url=xx,callback=self.parse)




