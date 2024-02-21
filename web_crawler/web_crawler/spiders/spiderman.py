from typing import Iterable
import scrapy
from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from bs4 import BeautifulSoup
from urllib.parse import urlparse


class SpidermanSpider(CrawlSpider):
    name = "spiderman"
    def __init__(self, start_urls=None, *args, **kwargs):
        super(SpidermanSpider, self).__init__(*args, **kwargs)
        self.start_urls = start_urls if start_urls else []
        self.allowed_domains = [urlparse(url).netloc for url in self.start_urls]

    keywords =  ['om-','about', 'info', 'kontakt', 'address', "telefon", "tjänster", "services"]
    rules = (
        Rule(LinkExtractor(allow=keywords), callback='parse_item', follow=True),

        #Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        soppa = BeautifulSoup(response.text, features="html.parser")

        for script in soppa(["script", "style"]):
            script.extract()

        JensAndersjuveler = ' '.join(chunk for chunk in soppa.get_text().split() if chunk)

        momentan_data = " :VGQH545: " + JensAndersjuveler + " :CGDE345: "

        return {str(response.url)[8:]: momentan_data}

