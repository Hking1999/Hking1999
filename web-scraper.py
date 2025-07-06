import requests
from bs4 import BeautifulSoup
import pandas as pd

# Target website
URL = 'http://books.toscrape.com/'

# Send GET request
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all product containers
products = soup.find_all('article', class_='product_pod')

# Prepare list for scraped data
data = []

for product in products:
    title = product.h3.a['title']
    price = product.find('p', class_='price_color').text
    availability = product.find('p', class_='instock availability').text.strip()
    
    data.append({'Title': title, 'Price': price, 'Availability': availability})

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('products.csv', index=False)

print("Scraping completed. Data saved to 'products.csv'.")