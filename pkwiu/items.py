# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PkwiuItem(scrapy.Item):
    sek = scrapy.Field()
    dzial = scrapy.Field()
    dzial_name = scrapy.Field()
    symbol = scrapy.Field()
    opis = scrapy.Field()
    vat = scrapy.Field()
    
