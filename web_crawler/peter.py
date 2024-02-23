from scrapy.crawler import CrawlerProcess
from googlecs import getSeach
from web_crawler.spiders.spiderman import SpidermanSpider
from nace import getNace

def webCrawler(nt, reg):
    """
        Perform web crawling to gather information about companies based on NACE code and region.

        Args:
            nt (str): The NACE code for the industry.
            reg (str): The region to search for companies in.

        Returns:
            None
    """

    gudsord = getNace(nt, reg)#["Umida Brands AB", "FRKY Foods AB", "Gutang Handelsbolag"] # GET COMPANY NAMES
    start_urls = []
                #["https://www.lpsignal.se", "https://swedtel.com", "https://mikrotema.se", "https://teamteknik.se/",
                #"https://tvent.se/", "https://www.airbus.com/en", "https://www.elgiganten.se/", "https://www.power.no/",
                #"https://vainu.io/company/digital-growth-sweden-ab-omsattning-och-nyckeltal/2151969340/foretagsinfo", "https://hagshult.se/",
                #"https://polkaprinsen.se/", "https://www.tekniskamuseet.se/", "https://miljogarden.se/", "https://svampkonsulent.se/",
                #"https://www.stadsmissionen.se/", "https://verktygsboden.se/", "https://bonaj.se/"]

    #https://www.jpinfonet.se/
    print(gudsord)

    for x in gudsord:
        start_urls.extend(getSeach(x, 2)) # GET URLS FROM SEARCH WORDS
        print(start_urls)

    process = CrawlerProcess(settings={
        'assistant': 'spiderman',
        'ROBOTSTXT_OBEY': True,
        'FEED_FORMAT': 'json',  # OUTPUT FORMAT
        'FEED_URI': 'output.json'  # OUTPUT FILE
    })

    process.crawl(SpidermanSpider, start_urls=start_urls)
    process.start()  # START THE CRAWL


webCrawler('26300', 'Stockholm')