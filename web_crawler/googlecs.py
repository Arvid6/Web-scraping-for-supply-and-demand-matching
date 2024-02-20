# pip install serpapi FÖRST
# pip install google-search-results
from serpapi import GoogleSearch

def getSeach(swag, num):
    blacklist = ["allabolag.se", "merinfo.se", "bolagsfakta.se", "proff.se", "hitta.se", "ratsit.se", "creditsafe.com", "s360digital.com", "vinjournalen.se", "largestcompanies.com", "axfood.se", "facebook.com", "instagram.com", "wikipedia.org", "infoo.se"]
    params = {
        "q": swag,
        "location": "Stockholm County, Sweden",  # OPTIONAL
        "hl": "sv",  # OPTIONAL
        "gl": "se",  # OPTIONAL
        "google_domain": "google.se",
        "api_key": "5f4693b65a0e9d1a165d3581f1f4ab4dd2dab0a7a77248a0d09da6fa33d01821"
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    organic_results = results.get('organic_results', [])

    filtered_results = [result for result in organic_results if not any(blacklisted in result.get('link', '') for blacklisted in blacklist)]

    urls = [result.get('link') for result in filtered_results[:num]] # NUMBER OF RESULTS

    return urls


#getSeach(["Umida Brands AB", "Urban Market Stockholm AB", "FRKY Foods AB"], "Stockholm County, Sweden", 4)
