from scrapy.crawler import CrawlerProcess
from googlecs import getSeach
from web_crawler.spiders.infoCrawler import infoCrawler
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

    loc = getNace(nt, reg)#["Umida Brands AB", "FRKY Foods AB", "Gutang Handelsbolag"] # GET COMPANY NAMES
    start_urls = []
                #["https://www.lpsignal.se", "https://swedtel.com", "https://mikrotema.se", "https://teamteknik.se/",
                #"https://tvent.se/", "https://www.airbus.com/en", "https://www.elgiganten.se/", "https://www.power.no/",
                #"https://vainu.io/company/digital-growth-sweden-ab-omsattning-och-nyckeltal/2151969340/foretagsinfo", "https://hagshult.se/",
                #"https://polkaprinsen.se/", "https://www.tekniskamuseet.se/", "https://miljogarden.se/", "https://svampkonsulent.se/",
                #"https://www.stadsmissionen.se/", "https://verktygsboden.se/", "https://bonaj.se/"]

    #https://www.jpinfonet.se/
    print(loc)

    for x in loc:
        start_urls.extend(getSeach(x, 1, "Stockholm County, Sweden")) # GET URLS FROM SEARCH WORDS
        print(x)

    print(start_urls)
    process = CrawlerProcess(settings={
        'assistant': 'getinfo',
        'ROBOTSTXT_OBEY': False,
        'FEED_FORMAT': 'json',  # OUTPUT FORMAT
        'FEED_URI': 'output.json'  # OUTPUT FILE
    })

    process.crawl(infoCrawler, start_urls=start_urls)
    process.start()  # START THE CRAWL


#('26300', 'Stockholm')