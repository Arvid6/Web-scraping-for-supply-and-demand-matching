import requests
import json
import os
from requests import Session
from requests_pkcs12 import Pkcs12Adapter
from dotenv import load_dotenv
def find_cert():
    """
        Find the path to the certificate file in the current working directory.

        Returns:
            str: The absolute path to the SCB API certificate file.
    """
    directory = os.getcwd()
    files = os.listdir(directory)
    cert_name = [file for file in files if file.startswith("Certifkat") or file.endswith(".pfx")]
    for file in cert_name:
        cert_path = os.path.abspath(file)
    return cert_path

def getNace(nace_code, region):
    """
        Get company information based on NACE code and region using the SCB API.

        Args:
            nace_code (str): The NACE code for the industry.
            region (str): The region to search for companies in.

        Returns:
            list: A list of company names matching the criteria.
    """
    session = Session()

    # API url
    url = "https://privateapi.scb.se/nv0101/v1/sokpavar/api/Je/HamtaForetag"

    # Path to certificate and private key.
    cert_pfx = find_cert()

    # Password from environment variables
    load_dotenv()
    api_password = os.getenv("API_KEY")

    # Arguments to be sent to the API
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    data_test = {"Arbetsställestatus": "1",
                 "Variabler": [{"Varde1": region, "Operator": "ArLikaMed", "Variabel": "Postort"}],
                 "Kategorier": [{"Kategori": "Bransch", "Kod": [nace_code, nace_code], "BranschNiva": "3"}]}

    # Call to the API
    session.mount('https://privateapi.scb.se', Pkcs12Adapter(pkcs12_filename=cert_pfx, pkcs12_password=api_password))
    response = session.post(url, json=data_test)

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
print(naces)