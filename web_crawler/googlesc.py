from serpapi import GoogleSearch

swag = ["Pizza", "Burger", "Pasta"]
numr = 4 # NUMBER OF RESULTS
loc = "Lulea, Norrbotten County, Sweden"

def setSearch(txt):
    global swag
    swag = txt


def setLoc(txt):
    global loc
    loc = txt


def getSeach():
    for word in swag:
        params = {
          "q": word,
          "location": loc, # OPTIONAL
          "google_domain": "google.se",
          "api_key": "5f4693b65a0e9d1a165d3581f1f4ab4dd2dab0a7a77248a0d09da6fa33d01821"
        }

        search = GoogleSearch(params)
        results = search.get_dict()

        organic_results = results.get('organic_results', [])

        # NUMBER OF RESULTS
        urls = [result.get('link') for result in organic_results[:numr]]

        print(f"Search word: {word} ")
        print(urls)


getSeach()