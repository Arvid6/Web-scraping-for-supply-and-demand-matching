from scrapy.crawler import CrawlerProcess
from googlesc import getSeach
from web_crawler.spiders.spiderman import SpidermanSpider
from nace import getNace

def webCrawler(nt, reg):
    gudsord = getNace(nt, reg)#["Umida Brands AB", "FRKY Foods AB", "Gutang Handelsbolag"] # GET COMPANY NAMES
    start_urls = []
    print(gudsord)

    for x in gudsord:
        start_urls.extend(getSeach(x, 3)) # GET URLS FROM SEARCH WORDS
        print(start_urls)
    process = CrawlerProcess(settings={
        'assistant': 'spiderman',
        'ROBOTSTXT_OBEY': True,
        'FEED_FORMAT': 'json',  # OUTPUT FORMAT
        'FEED_URI': 'output.json'  # OUTPUT FILE
    })

    process.crawl(SpidermanSpider, start_urls=start_urls)
    process.start()  # START THE CRAWL


webCrawler('17211', 'Stockholm')