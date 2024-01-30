import requests
import json

url = "https://privateapi.scb.se/nv0101/v1/sokpavar/api/Je/HamtaForetag"

# Path till cert-filar. Måste hitta nåt universiellt på det här, men byt till din egna path medan.
cert_file_path = "C:\\Users\\Justf\\Desktop\\Scrape\\D0020E\\web_crawler\\test_cert.crt"
private_key_path = "C:\\Users\\Justf\\Desktop\\Scrape\\D0020E\\web_crawler\\test_key3.pem"


headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
data_test = {"Arbetsställestatus":"1",
             "Variabler":[{"Varde1":"Luleå","Operator":"ArLikaMed","Variabel":"Postort"}],
             "Kategorier":[{"Kategori":"Bransch","Kod": ["01110","as"], "BranschNiva":"3"}]}



response = requests.post(url, cert=(cert_file_path, private_key_path,),json=data_test, headers=headers)
#response = requests.get(url, cert=(cert_file_path, private_key_path,), headers=headers)

#print(f"Response: {response.json()}")

test = response.content

filtrera = response.json()
print(test)

namn = filtrera[0]['Företagsnamn']
print(namn)


with open('cnt.json', 'wb') as f:
    f.write(test)


foretagsnamn = ([d['Företagsnamn'] for d in filtrera])

fn_json = json.dumps(foretagsnamn)

with open("sample.json", "w") as outfile:
    outfile.write(fn_json)




