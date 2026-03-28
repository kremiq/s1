import requests
import json
import os

# Define the base URL
CONSOLE_URL = "https://usea1-purple.sentinelone.net"

# BEST PRACTICE: Load your API token from an environment variable rather than hardcoding it
# e.g., export S1_API_TOKEN="your_actual_token"
API_TOKEN = os.environ.get("S1_API_TOKEN", "YOUR_API_TOKEN_HERE")

# Construct the full endpoint URL
url = f"{CONSOLE_URL}/web/api/v2.1/update/agent/packages"

# Set up the request headers
headers = {
    "Authorization": f"ApiToken {API_TOKEN}"
}

try:
    # Make the GET request
    response = requests.get(url, headers=headers)
    
    # Raise an exception if the HTTP request returned an unsuccessful status code
    response.raise_for_status() 
    
    # Parse the JSON response
    parsed_json = response.json()
    
    # Pretty-print the JSON output (equivalent to `jq '.'`)
    print(json.dumps(parsed_json, indent=4))
    
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
    # Print the response body if available, as it often contains API error details
    if response.text:
        print(f"Response details: {response.text}")
except Exception as err:
    print(f"An error occurred: {err}")

    