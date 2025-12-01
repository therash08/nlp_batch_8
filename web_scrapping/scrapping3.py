import requests
from bs4 import BeautifulSoup
import csv

# 1. Target URL (A public practice site)
URL = "http://books.toscrape.com/catalogue/category/books/travel_2/"

# Data structure to hold extracted information
scraped_data = []

# 2. Fetch the HTML content
try:
    response = requests.get(URL)
    response.raise_for_status()  # Check for HTTP errors
except requests.exceptions.RequestException as e:
    print(f"Error loading page: {e}")
    exit()

# 3. Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# 4. Extract specific information
# Find all product containers
all_articles = soup.find_all('article', class_='product_pod')

for article in all_articles:
    # Extract Title (found in the 'title' attribute of the link)
    title_tag = article.find('h3').find('a')
    title = title_tag['title']

    # Extract Price (found in the p tag with class 'price_color')
    price = article.find('p', class_='price_color').text

    # Add to the list
    scraped_data.append({'title': title, 'price': price})

print(f"✅ Successfully scraped {len(scraped_data)} items.")

# 5. Save the extracted data to a CSV file
csv_file = 'travel_books.csv'
fieldnames = ['title', 'price']

with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(scraped_data)

print(f"💾 Data saved to '{csv_file}'.")
