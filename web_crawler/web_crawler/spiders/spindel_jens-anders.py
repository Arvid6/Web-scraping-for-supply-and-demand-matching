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
lines = (line.strip() for line in JensAndersjuveler.splitlines())

#Delar upp headlines till egna rader
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))

#Tar bort onödiga blank spaces
JensAndersjuveler = '\n'.join(chunk for chunk in chunks if chunk)

print(JensAndersjuveler)

#Spara i Json fil
with open("SlutetgottAlltgott.json", "w") as outfile:
    json.dump(JensAndersjuveler, outfile)