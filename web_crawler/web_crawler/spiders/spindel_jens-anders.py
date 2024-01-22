#måste installera "pip install beautifulsoup4"
from urllib.request import urlopen
from bs4 import BeautifulSoup

#För att spara i Json fil
import json

#Intigers
url = "https://www.llt.lulea.se/" #denna ska bytas---------------------------------------------------------------
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
momentan_data = url + " :VGQH545: " + JensAndersjuveler + " :CGDE345: " # " :CGDE345: " Är koden för ny webbsida i json fil. Medans koden mellan webbsidan och htmlkoden är " :VGQH545: "

#Kollar om json filen är tom
try:
    with open('SlutetgottAlltgott.json', 'r') as f:
        data = json.load(f)
    #Om datan lyckas laddas så blir tom 0
    tom = 0
except json.JSONDecodeError:
    #Om filen är tom så sätts tom till 1
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
    Slutet = kolonisten + momentan_data

    #Sparar det till SlutetgottAlltgott.json
    with open("SlutetgottAlltgott.json", "w") as outfile:
        json.dump(Slutet, outfile)