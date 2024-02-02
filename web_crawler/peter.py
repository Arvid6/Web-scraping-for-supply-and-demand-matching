from scrapy.crawler import CrawlerProcess
from googlesc import getSeach
from web_crawler.spiders.spiderman import SpidermanSpider
#from nace import kys

#gudsord = [] #call to nace

#for x in gudsord:
start_urls = getSeach("Umida Brands AB", 3)
print(start_urls)
process = CrawlerProcess(settings={
    'assistant': 'spiderman',
    'ROBOTSTXT_OBEY': True,
    'FEED_FORMAT': 'json',  # specify the output format
    'FEED_URI': 'output.json'  # specify the output file
})

process.crawl(SpidermanSpider, start_urls=start_urls)
process.start()  # the script will block here until the crawling is finished