import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
#måste installera "pip install beautifulsoup4"
from urllib.request import urlopen
from bs4 import BeautifulSoup

#För att spara i Json fil
import json


class SpidermanSpider(CrawlSpider):
    name = "spiderman"
    # Ska bytas till en lista av hemsidor som ska och kan sökas
    allowed_domains = ["shop.actionbutton.net"]
    start_urls = ["https://shop.actionbutton.net/"]
    # Regler för hemsidor som söks
    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # Intigers
        print(response)
        print(str(response)[5:-1])
        # Intigers
        url = str(response)[5:-1]
        html = urlopen(url).read()
        soppa = BeautifulSoup(html, features="html.parser")

        # Ta bort srcripten och css kallelse
        for script in soppa(["script", "style"]):
            script.extract()  # Gå igenom tekten och ta bort

        # Spara texten
        JensAndersjuveler = soppa.get_text()

        # Delar upp allt
        rader = (line.strip() for line in JensAndersjuveler.splitlines())

        # Delar upp headlines till egna rader
        bitar = (phrase.strip() for line in rader for phrase in line.split("  "))

        # Tar bort onödiga blank spaces
        JensAndersjuveler = ' '.join(chunk for chunk in bitar if chunk)

        # print(html)
        # print(JensAndersjuveler)


        # Slår ihop URL med innehåll
        momentan_data = url + " :VGQH545: " + JensAndersjuveler + " :CGDE345: "  # " :CGDE345: " Är koden för ny webbsida i json fil. Medans koden mellan webbsidan och htmlkoden är " :VGQH545: "

        # Kollar om json filen är tom
        try:
            with open("SlutetgottAlltgott.json", "r") as f:
                data = json.load(f)
            # Om datan lyckas laddas så blir tom 0
            tom = 0
        except json.JSONDecodeError:
            # Om filen är tom så sätts tom till 1
            tom = 1

        if tom == 1:
            # Sparar det till SlutetgottAlltgott.json
            with open("SlutetgottAlltgott.json", "w") as outfile:
                json.dump(momentan_data, outfile)
        else:
            # Laddar Slutetgottaltinggott.json in i kolonisten
            with open("SlutetgottAlltgott.json", "r") as f:
                kolonisten = json.load(f)

            # Slår ihop nya datan med gamla datan
            Slutet = kolonisten + momentan_data

            # Sparar det till SlutetgottAlltgott.json
            with open("SlutetgottAlltgott.json", "w") as outfile:
                json.dump(Slutet, outfile)


