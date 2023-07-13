# For questions: @author Sandro
# script to demonstrate http requests in python

import json


####################################
############ Parse Json ############
####################################

# JSON string
json_string = '''
{
    "name": "John Doe",
    "age": 99
}
'''

# Parse the JSON string
data = json.loads(json_string)

# Access the parsed data
name = data["name"]
age = data["age"]

# Print the parsed data
print("Name:", name)
print("Age:", age)

####################################
######### Json from webapi #########
####################################

import requests

print("")
print("From Web Api")
print("____________")

# API endpoint URL
url = "https://dummyjson.com/products"

# GET request
response = requests.get(url)
data = response.json()

for product in data["products"]:
    print(product["title"])


####################################
######### Json serializing #########
####################################

# Create a Python dictionary
data = [
        {
            "name": "Peter",
            "lastname": "Gryffin"
        },
        {
            "name": "Homer",
            "lastname": "Simpson"
        }
    ]

# Convert dictionary to JSON string
json_string = json.dumps(data)

# Print the JSON string
print(json_string)
