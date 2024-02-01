from scrapy.crawler import CrawlerProcess
from web_crawler.googlesc import getSeach
from web_crawler.spiders.spiderman import SpidermanSpider

urls = getSeach(["Umida Brands AB", "Urban Market Stockholm AB", "FRKY Foods AB",], 1)

allowed_domains = ["example.com", "anotherexample.com"]
start_urls = urls
process = CrawlerProcess(settings={
    'assistant': 'my_bot',
    'ROBOTSTXT_OBEY': True,
})

process.crawl(SpidermanSpider, allowed_domains=allowed_domains, start_urls=start_urls)
process.start()  # the script will block here until the crawling is finished