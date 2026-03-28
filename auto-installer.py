import requests
import json
import os


# Define the base URL NEED TO BE CHANGED TO CONFGUREABLE IN THE FILE
CONSOLE_URL = "https://usea1-purple.sentinelone.net"
API_TOKEN = "eyJraWQiOiJ1cy1lYXN0LTEtcHJvZC0wIiwiYWxnIjoiRVMyNTYifQ.eyJzdWIiOiJsdWJvcy5jaG92YW5Ac2VudGluZWxvbmUuY29tIiwiaXNzIjoiYXV0aG4tdXMtZWFzdC0xLXByb2QiLCJkZXBsb3ltZW50X2lkIjoiMTE2MzMiLCJ0eXBlIjoidXNlciIsImV4cCI6MTc3NzI4MDk1MSwiaWF0IjoxNzc0Njg4OTUxLCJqdGkiOiIyZjVlZjBlMi0wMzVkLTRkZjItYTE3YS0zZmRmNWRjYzhlOTYifQ.xeQT55_whEnEZKO8SHCoWsXVDlGaEUtejJuip-eDgcWHNxq6KBwL41Ct22qTBvbRcWiS7ezp1yT-jb_qobD_TQ"

# Construct the full endpoint URL
baseurl = f"{CONSOLE_URL}/web/api/v2.1/update/agent/packages"
filters = "?platformTypes=windows&fileExtension=.msi&status=ga"
url = f"{baseurl}{filters}"

# Set up the request headers
headers = {
    "Authorization": f"ApiToken {API_TOKEN}"
}

# Make the GET request
response = requests.get(url, headers=headers)

# Check if the request was successful (Status Code 200)
if response.status_code == 200:
    print("Successfully received response from the server!")

    data = response.json()  # Parse the JSON response
    packages = data['data']

    # Find the package with the highest version number
    latest_package = max(packages, key=lambda x: [int(i) for i in x['version'].split('.')])

    print(f"Latest Version: {latest_package['version']}")
    print(f"File Name: {latest_package['fileName']}")
    print(f"ID: {latest_package['id']}")

    # Construct the download URL
    download_url = f"{CONSOLE_URL}/web/api/v2.1/update/agent/download/{latest_package['id']}"
    print(f"Download URL: {download_url}")

    Path = os.path.join(os.getcwd(), latest_package['fileName'])
    print(f"File will be saved to: {Path}")
  
    # Download the file
    download_response = requests.get(download_url, headers=headers)
    if download_response.status_code == 200:
        with open(Path, 'wb') as f:
            f.write(download_response.content)
   
    
 
else:
    print(f"Request failed with status code: {response.status_code}")
    print(f"Response content: {response.text}")






