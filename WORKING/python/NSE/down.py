
import requests
from bs4 import BeautifulSoup

# Replace with the URL of the website you want to scrape
url = 'https://www.nseindia.com/all-reports'

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the page content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all elements with the 'data-link' attribute
    elements_with_data_link = soup.find_all(attrs={'data-link': True})

    # Extract and print the 'data-link' attributes
    for element in elements_with_data_link:
        print(element['data-link'])
else:
    print(f'Failed to retrieve the page. Status code: {response.status_code}')
