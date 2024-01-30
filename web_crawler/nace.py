import requests
url = "https://privateapi.scb.se/nv0101/v1/sokpavar/api/AE/HamtaArbetsstallen"

# Path till cert-filar. Måste hitta nåt universiellt på det här, men byt till din egna path medan.
cert_file_path = "C:\\Users\\Justf\\Desktop\\Scrape\\D0020E\\web_crawler\\test_cert.crt"
private_key_path = "C:\\Users\\Justf\\Desktop\\Scrape\\D0020E\\web_crawler\\test_key3.pem"


headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
data_test = {'Arbetsställestatus':'1','Variabler':[{'Varde1':'10017721','Operator':'ArLikaMed','Variabel':'CFARnr'}]}



response = requests.post(url, cert=(cert_file_path, private_key_path,), json=data_test, headers=headers)
#response = requests.get(url, cert=(cert_file_path, private_key_path,), headers=headers)

#print(f"Response: {response.json()}")

cnt = response.content

with open('cnt.json', 'wb') as f:
    f.write(cnt)

print(response.text)