import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class PostnordSpider(CrawlSpider):
    name = "postnord"
    allowed_domains = ["transportfirma.se", "merchsweden.se"]
    start_urls = ["https://www.transportfirma.se/", "https://merchsweden.se/"]

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )
    def parse(self, response):
        self.links.append(response.url)
        for href in response.css('a::attr(href)'):
            yield response.follow(href, self.parse)
