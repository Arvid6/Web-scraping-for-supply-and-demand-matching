from scrapy.crawler import CrawlerProcess
from googlecs import getSeach
from web_crawler.spiders.spiderman import SpidermanSpider
from nace import getNace

def webCrawler(nt, reg):
    gudsord = getNace(nt, reg)#["Umida Brands AB", "FRKY Foods AB", "Gutang Handelsbolag"] # GET COMPANY NAMES
    start_urls = []
    print(gudsord)

    for x in gudsord:
        start_urls.extend(getSeach(x, 3)) # GET URLS FROM SEARCH WORDS
        print(start_urls)



webCrawler('26300', 'Stockholm')