
import requests
import json

# The API endpoint for a single, random joke of any category
url = "https://v2.jokeapi.dev/joke/Any?type=single"

# Make the GET request to the API
try:
    response = requests.get(url)
    response.raise_for_status()  # This will raise an error for bad status codes (4xx or 5xx)

    # Parse the JSON data from the response
    joke_data = response.json()

    # Check if the API call was successful
    if joke_data['error']:
        print("Error fetching joke.")
    else:
        # Extract and print the joke text
        joke = joke_data['joke']
        print("Your random joke is:")
        print(joke)

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")