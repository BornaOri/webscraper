import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.spareroom.co.uk/flatshare/london"
CSV_FILENAME = "prices.csv"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

# variable for unique values using set
unique_prices = set()


price_tags = soup.find_all(class_ = 'listingPrice')
if not price_tags:
    print("No price tags in listingprice- website probably changed")
else: 
    for price_tag in price_tags:
        price = price_tag.text.strip()
        unique_prices.add(price)
    if unique_prices:
        for price in unique_prices:
            print(price) #print to console

        with open(CSV_FILENAME, 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['Price'])
            #each unique price to be writte on new row, sorting prices for organisation.
            for price in sorted(list(unique_prices)):
                csv_writer.writerow([price])


