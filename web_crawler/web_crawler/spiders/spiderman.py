import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from spindel_jens_anders import *


class SpidermanSpider(CrawlSpider):
    name = "spiderman"
    allowed_domains = ["transportfirma.se"]
    start_urls = ["https://www.transportfirma.se/"]
    #skriv in den nedanför i sluturl
    #slut_url =
    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        #item["domain_id"] = response.xpath('//input[@id="sid"]/@value').get()
        #item["name"] = response.xpath('//div[@id="name"]').get()
        #item["description"] = response.xpath('//div[@id="description"]').get()
        return item
        #fixa url så att det fungerar nedanför
        #avancera_jens_anders(url)
