#måste installera "pip install beautifulsoup4"
from urllib.request import urlopen
from bs4 import BeautifulSoup

#För att spara i Json fil
import json

#Intigers
url = "https://www.frakttjanst.se/" #denna ska bytas---------------------------------------------------------------
html = urlopen(url).read()
soppa = BeautifulSoup(html, features="html.parser")

#Ta bort srcripten och css kallelse
for script in soppa(["script", "style"]):
    script.extract()    #Gå igenom tekten och ta bort

#Spara texten
JensAndersjuveler = soppa.get_text()

#Delar upp allt
rader = (line.strip() for line in JensAndersjuveler.splitlines())

#Delar upp headlines till egna rader
bitar = (phrase.strip() for line in rader for phrase in line.split("  "))

#Tar bort onödiga blank spaces
JensAndersjuveler = '\n'.join(chunk for chunk in bitar if chunk)

#print(html)
print(JensAndersjuveler)

#Slår ihop URL med innehåll
momentan_data = url + "     " + JensAndersjuveler

#Kollar om json filen är tom
try:
    with open('SlutetgottAlltgott.json', 'r') as f:
        data = json.load(f)
    # If the file is not empty and contains valid JSON, data will contain that JSON
    tom = 0
except json.JSONDecodeError:
    # If the file is empty or not valid JSON, a JSONDecodeError will be raised
    tom = 1

if tom == 1:
    #Sparar det till SlutetgottAlltgott.json
    with open("SlutetgottAlltgott.json", "w") as outfile:
        json.dump(momentan_data, outfile)
else:
    #Laddar Slutetgottaltinggott.json in i kolonisten
    with open('SlutetgottAlltgott.json', 'r') as f:
        kolonisten = json.load(f)

    #Slår ihop nya datan med gamla datan
    Slutet = kolonisten + "     " + momentan_data

    #Sparar det till SlutetgottAlltgott.json
    with open("SlutetgottAlltgott.json", "w") as outfile:
        json.dump(Slutet, outfile)