from typing import Iterable
import scrapy
from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from bs4 import BeautifulSoup

class SpidermanSpider(CrawlSpider):
    name = "spiderman"
    allowed_domains = ["shop.actionbutton.net", "llt.lulea.se"]
    start_urls = ["https://shop.actionbutton.net/", "https://www.llt.lulea.se/"]
    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, dont_filter=True)

    def parse_item(self, response):
        soppa = BeautifulSoup(response.text, features="html.parser")

        for script in soppa(["script", "style"]):
            script.extract()

        JensAndersjuveler = ' '.join(chunk for chunk in soppa.get_text().split() if chunk)

        momentan_data = response.url + " :VGQH545: " + JensAndersjuveler + " :CGDE345: "

        return {'data': momentan_data}

