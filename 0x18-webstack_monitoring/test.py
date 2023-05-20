#!/usr/bin/python3
import requests

# Set up the API endpoint and parameters
api_url = "https://api.datadoghq.com/api/v1/dashboard/"
api_key = "3f0589d7c11b7b2b70dd9bdc56dc49b8"
api_app_key = "3621221ae6b6b05e551eeb9bce4b68c5b3d6cd85"
headers = {'Content-type': 'application/json', 'DD-API-KEY': api_key, 'DD-APPLICATION-KEY': api_app_key}
query_params = {'filter': 'host:111665-web-01'}

# Make the API call to get the host details
response = requests.get(api_url, headers=headers, params=query_params)
# Check the response status code
if response.status_code == 200:
    # Parse the JSON response
    response_json = response.json()
    print(response_json)
