# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from pkwiu.items import PkwiuItem

class Pkwiu08Spider(CrawlSpider):
    name = "pkwiu08"
    allowed_domains = ["www.klasyfikacje.gofin.pl"]
    start_urls = (
        'http://www.klasyfikacje.gofin.pl/pkwiu/',
    )
    rules = (
        # Extract only adds
        Rule(LinkExtractor(allow=( ),
                           restrict_xpaths=('//div[@class="sekcje"]',)),
             callback='parse_page',
        ),
        
    )

    def parse_page(self, response):
        print "Parsing"
        sek = response.xpath('//div[@class="naglowek_tresc"]/text()').extract()[0]
        dzial = response.xpath('//div[@class="tabelka_dzialow_nr"]/text()').extract()
        dzial_name = response.xpath('//div[@class="tabelka_dzialow"]/text()').extract()
        
        for res in response.xpath('//table[@class="spis"]/tr'):
            item = PkwiuItem()
            

            item['sek'] = sek

            item['dzial'] = dzial

            item['dzial_name'] = dzial_name

            row = [r.xpath('string()').extract() for r in res.xpath('.//td')]
            if row[1][0] == "Nazwa grupowania":
                continue
            item['symbol'] = row[0][0]
    
            item['opis'] = row[1][0]

            item['vat'] = row[2][0]
            yield item
