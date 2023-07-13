# For questions: @author Sandro
# script to demonstrate http requests in python

# prerequisites: pip install requests

import requests

# API endpoint URL
url = "https://dummyjson.com/products"

# GET request
response = requests.get(url)
data = response.json()

# Print the response
print("Response:")
print(data)