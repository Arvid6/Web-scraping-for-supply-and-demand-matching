from typing import Iterable
import scrapy
from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from bs4 import BeautifulSoup
from urllib.parse import urlparse


class infoCrawler(CrawlSpider):
    name = "getinfo"
    custom_settings = {
        'DEPTH_LIMIT': 1,
        'DOWNLOAD_TIMEOUT': 15,
    }

    def __init__(self, start_urls=None, *args, **kwargs):
        super(infoCrawler, self).__init__(*args, **kwargs)
        self.start_urls = start_urls if start_urls else []
        self.allowed_domains = [urlparse(url).netloc for url in self.start_urls]

    keywords = ['om-', 'about-', 'info', 'kontakt', 'address', 'telefon', 'tjänster', 'services', 'about']
    rules = (
        Rule(LinkExtractor(allow=keywords), callback='parse_item', follow=True),

        # Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def parse_start_url(self, response):
        return self.parse_item(response)

    def parse_item(self, response):
        #if any(keyword in response.url for keyword in self.keywords):
        soppa = BeautifulSoup(response.text, features="html.parser")

        for script in soppa(["script", "style"]):
            script.extract()

        JensAndersjuveler = ' '.join(chunk for chunk in soppa.get_text().split() if chunk)

        momentan_data = " :VGQH545: " + JensAndersjuveler + " :CGDE345: "

        return {str(response.url)[8:]: momentan_data}
