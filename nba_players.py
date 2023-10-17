from datetime import datetime
import requests
import csv


# Set URL for NBA API
url = "https://free-nba.p.rapidapi.com/players"

# User input for NBA API Key and set it to a variable
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

    # Open a CSV file to write the API response
    with open("nba.csv", "w") as file:
        #Create a writer object variable to write into the CSV
        writer = csv.writer(file)
        #Loop through each page in the API response
        for page in range(total_pages):
            print("Writing to nba.csv")
            # For each row parse through the JSON formatted string into a Python object 
            for row in response.json()["data"]:
                # and then write player data to a row in the CSV
                writer.writerow([row["id"], row["first_name"] + " " + row["last_name"], row["position"], row["team"]["full_name"]])

#While this is true, continue looping
while True:
    try:
        #Run function
        nba_player_data()

    #Error handling for incorrect API key
    except(KeyError):
        print("Invalid API Key")
        #Set user response to if they want to re-enter their API key
        users_response = input("Would you like to re-enter your API Key (Enter 'yes' or 'no' ONLY)? ")
        #If the user response is "no", do this:
        if users_response.lower() == "no":
            print("Exiting...")
            exit()
        #If the user's response is "yes", do this:
        elif users_response.lower() == "yes":
            #ask for the user API key and set it to a variable
            api_key = input(f"Please enter your API Key for {url}:")
            #run function
            nba_player_data()
        #until a valid response is given
        else:
            #continue looping through the if statement 
            continue 
    else:
        # Exit the while loop
        break
