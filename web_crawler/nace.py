import requests
import json
import os

# API url
url = "https://privateapi.scb.se/nv0101/v1/sokpavar/api/Je/HamtaForetag"

# Path to certificate and private key.
cert_file_path = os.path.abspath("test_cert.crt")
private_key_path = os.path.abspath("test_key3.pem")

# Arguments to be sent to the API
search_city = "Stockholm"
search_nace = "10840"
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
data_test = {"Arbetsställestatus": "1",
             "Variabler": [{"Varde1": search_city, "Operator": "ArLikaMed", "Variabel": "Postort"}],
             "Kategorier": [{"Kategori": "Bransch", "Kod": [search_nace, search_nace], "BranschNiva": "3"}]}

# Call to the API
response = requests.post(url, cert=(cert_file_path, private_key_path,), json=data_test, headers=headers)
# response = requests.get(url, cert=(cert_file_path, private_key_path,), headers=headers)


# Response from API saved as a JSON-file
content = response.content

with open('cnt.json', 'wb') as f:
    f.write(content)

# Response from API filtered on Company name and City
output = response.json()
print(output)
temp_list = []

for d in output:
    company_name = d.get('Företagsnamn')
    city = d.get('PostOrt')
    temp_list.extend([company_name, city])

filtered_output = json.dumps(temp_list, indent=1)

with open("found_companies.json", "w") as outfile:
    outfile.write(filtered_output)
