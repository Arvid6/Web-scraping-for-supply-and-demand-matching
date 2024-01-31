import requests
import json
import os

# url till APIn
url = "https://privateapi.scb.se/nv0101/v1/sokpavar/api/Je/HamtaForetag"

# Path till certifikatet och nyckeln
cert_file_path = os.path.abspath("test_cert.crt")
private_key_path = os.path.abspath("test_key3.pem")

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
data_test = {"Arbetsställestatus": "1",
             "Variabler": [{"Varde1": "Luleå", "Operator": "ArLikaMed", "Variabel": "Postort"}],
             "Kategorier": [{"Kategori": "Bransch", "Kod": ["01110", "as"], "BranschNiva": "3"}]}

response = requests.post(url, cert=(cert_file_path, private_key_path,), json=data_test, headers=headers)
# response = requests.get(url, cert=(cert_file_path, private_key_path,), headers=headers)

# print(f"Response: {response.json()}")

test = response.content

filtrera = response.json()
print(filtrera)

with open('cnt.json', 'wb') as f:
    f.write(test)

fn = []

for d in filtrera:
    foretagsnamn = d.get('Företagsnamn')
    postort = d.get('PostOrt')
    fn.extend([foretagsnamn, postort])

fn_json = json.dumps(fn, indent=1)

with open("sample.json", "w") as outfile:
    outfile.write(fn_json)
