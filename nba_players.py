# Import requests module that makes HTTP requests
import requests

# Import csv library to write API response to a CSV file
import csv

# Set URL for NBA API
url = "https://free-nba.p.rapidapi.com/players"

# Set API credentials to access the free-nba API 
headers = {
    "X-RapidAPI-Key": "b4241d60f9mshbc56ef08a1934e2p13cc0ajsnb60b64943db7",
    "X-RapidAPI-Host": "free-nba.p.rapidapi.com"
}

# Create a variable for the page parameter that would be passed later to the GET request
page_parameters = {"page":"0","per_page":"1000"}

######################################################################
# Make a GET request to API URL, passing in the parameters and setting it to a reponse to be use later
response = requests.get(url, headers=headers, params=page_parameters)                                               #, params=querystring

# Get the total number of pages in the API response
total_pages = response.json()["meta"]["total_pages"]

# Open a CSV file to write the API response
with open("nba.csv", "w") as file:
    writer = csv.writer(file)
    # Loop through each page in the API response
    for page in range(total_pages):
        print("Writing to nba.csv")
        # For each row parse through the json fromatted string into python object 
        for row in response.json()["data"]:
            # and then write player data to a row in the CSV
            writer.writerow([row["id"], row["first_name"] + " " + row["last_name"], row["position"], row["team"]["full_name"]]) 
