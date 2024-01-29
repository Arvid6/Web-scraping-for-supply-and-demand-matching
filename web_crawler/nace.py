import requests
url = "https://privateapi.scb.se/nv0101/v1/sokpavar/api/AE/KoptaVariabler"

# Path till cert-filar. Måste hitta nåt universiellt på det här, men byt till din egna path medan.
cert_file_path = "C:\\Users\\Justf\\Desktop\\Scrape\\D0020E\\web_crawler\\test_cert.crt"
private_key_path = "C:\\Users\\Justf\\Desktop\\Scrape\\D0020E\\web_crawler\\test_key3.pem"

response = requests.get(url, cert=(cert_file_path, private_key_path,))

print(response.text)