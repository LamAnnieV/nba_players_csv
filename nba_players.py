from datetime import datetime
import requests
import csv


# Set URL for NBA API
url = "https://free-nba.p.rapidapi.com/players"

# Input for NBA API Key
api_key = input(f"Please enter your API Key for {url}:")

def nba_player_data():
	    # Set API credentials to access the free-nba API 
    headers = {
        "X-RapidAPI-Key": api_key ,
        "X-RapidAPI-Host": "free-nba.p.rapidapi.com"
    }

    # Create a variable for the page parameter that would be passed later to the GET request
    page_parameters = {"page":"0","per_page":"1000"}


    # Make a GET request to API URL, passing in the parameters and setting it to a response to be used later
    response = requests.get(url, headers=headers, params=page_parameters)                                     

    # Get the total number of pages in the API response
    total_pages = response.json()["meta"]["total_pages"]
    # print(response.json())

    # Open a CSV file to write the API response
    with open("nba.csv", "w") as file:
        writer = csv.writer(file)
        # Loop through each page in the API response
        for page in range(total_pages):
            print("Writing to nba.csv")
            # For each row parse through the json formatted string into Python object 
            for row in response.json()["data"]:
                # and then write player data to a row in the CSV
                writer.writerow([row["id"], row["first_name"] + " " + row["last_name"], row["position"], row["team"]["full_name"]])

while True:
    try:
        nba_player_data()

    except(KeyError):
        print("Invalid API Key")
        users_response = input("Would you like to re-enter your API Key (Enter 'yes' or 'no' ONLY)? ")
        if users_response.lower() == "no":
            print("Exiting...")
            exit()
        elif users_response.lower() == "yes":
            api_key = input(f"Please enter your API Key for {url}:")
            nba_player_data()
        else:
            continue  # Continue the loop to ask for a valid response
    else:
        # The code inside the try block was successful, so exit the loop
        break
