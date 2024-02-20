import requests
import json
import os


def getNace(nace_code, region):
    # API url
    url = "https://privateapi.scb.se/nv0101/v1/sokpavar/api/Je/HamtaForetag"

    # Path to certificate and private key.
    cert_file_path = os.path.abspath("nyttcrt.crt")
    private_key_path = os.path.abspath("nykey3.pem")

    # Arguments to be sent to the API
    search_city = "Stockholm"
    search_nace = "10840"
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    data_test = {"Arbetsställestatus": "1",
                 "Variabler": [{"Varde1": region, "Operator": "ArLikaMed", "Variabel": "Postort"}],
                 "Kategorier": [{"Kategori": "Bransch", "Kod": [nace_code, nace_code], "BranschNiva": "3"}]}

    # Call to the API
    response = requests.post(url, cert=(cert_file_path, private_key_path,), json=data_test, headers=headers)
    # response = requests.get(url, cert=(cert_file_path, private_key_path,), headers=headers)

    # Response from API saved as a JSON-file
    content = response.content

    with open('cnt.json', 'wb') as f:
        f.write(content)

    # Response from API filtered on Company name and City
    output = response.json()
    temp_list = []

    for d in output:
        company_name = d.get('Företagsnamn')
        # city = d.get('PostOrt')
        temp_list.extend([company_name])

    filtered_output = json.dumps(temp_list, indent=1)

    with open("found_companies.json", "w") as outfile:
        outfile.write(filtered_output)

    # Return list with compaines to the Google scrape file (?)
    return temp_list


naces = getNace("10840", "Stockholm")
#print(naces)