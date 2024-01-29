import httpx
url = "https://privateapi.scb.se/nv0101/v1/sokpavar/api/AE/HamtaArbetsstallen"  # Replace this with the actual API endpoint URL

# Path to your .pfx file
cert_file_path = "C:\\Users\\Justf\\Desktop\\Scrape\\D0020E\\web_crawler\\test_cert.crt"
private_key_path = "C:\\Users\\Justf\\Desktop\\Scrape\\D0020E\\web_crawler\\Certifikat_SokPaVar_A00023.pem"
# Password for the certificate
cert_password = "LCBafWC6aMze"

with httpx.Client(cert=(cert_file_path, private_key_path)) as client:
    response = client.get(url)

print(response.text)