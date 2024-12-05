# Import the requests library
import requests

# Define the URL of the website to scrape

URL = "https://www.kraftheinzcompany.com"

# Send a GET request to the specified URL and store the response in 'resp'
response = requests.get(URL)

# Print the HTTP status code of the response to check if the request was successful
print("Status Code:", response.status_code)

# Print the HTML content of the response
print("\nResponse Content:")
print(response.text)