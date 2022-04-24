import pandas as pd
import requests
from bs4 import BeautifulSoup
import json
import psycopg2

def scrapper():
    conn = psycopg2.connect(
        database='credicxo',
        user='postgres',
        password='test',
        host='localhost',
        port=5432
    )
    cursor = conn.cursor()

    df = pd.read_csv('Amazon Scraping - Sheet1.csv',
        usecols=['Asin', 'country'])
    # print(df.head(n=100))
    
    HEADERS = ({'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
                'Accept-Language': 'fr-CH, fr;q=0.9, en;q=0.8, de;q=0.7, *;q=0.5'})
    details = []
    file = open('product-details.json', 'w')

    for row in range(100):
        title = None
        image_url = None
        price = 0.00
        description = None

        base_url = f"https://www.amazon.{df.loc[row]['country']}/dp/{df.loc[row]['Asin']}"
        
        source_code = requests.get(base_url, headers=HEADERS)
        print(source_code.status_code)
        
        status = source_code.status_code
        if status == 200:
            source_content = source_code.content
            soup = BeautifulSoup(source_content, features="lxml")
            # print(soup.prettify())
            
            title_span = soup.find('span', attrs={'id': 'productTitle'})
            if title_span:
                title = title_span.text.strip()
                print(title) 

            image_tag = soup.find('img', attrs={'class': 'a-dynamic-image'})
            if image_tag:
                image_url = image_tag['src']
                print(image_url)

            price_span = soup.find('span', attrs={'class': 'a-price-whole'})
            if price_span:
                price = price_span.text.strip().replace(',', '')
                print(price)

            description_div = soup.find('div', attrs={'id': 'productDescription'})
            if description_div:
                description = description_div.find('span').text.strip()
                print(description)

            details_dict = {
                'title': title,
                'image_url': image_url,
                'price': price,
                'description': description
            }

            details.append(details_dict)

            cursor.execute('INSERT INTO scrapper_productdetails (title, image_url, price, description) VALUES(%s, %s, %s, %s)',
            (title, image_url, price, description))

            conn.commit()
        else:
            print(f'{base_url} is Not Available')

    details_json = json.dumps(details)
    file.write(details_json)
    file.close()



if __name__ == "__main__":
    scrapper()