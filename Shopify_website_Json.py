import requests
import json
import pandas as pd

url = 'https://helmboots.com/products.json?limit=500&page=1'

res = requests.get(url)

data = res.json()
# print(data)
product_list = []

for iteams in data['products']:
    id = iteams['id']
    title = iteams['title']
    handle = iteams['handle']
    published_at = iteams['published_at']
    created_at = iteams['created_at']
    product_type = iteams['product_type']
    # print(product_type)

    for image in iteams['images']:
        try:
            imagesrc = image['src']

        except:
            imagesrc = None

    for variant in iteams['variants']:
        sku = variant['sku']
        price = variant['price']
        available = variant['available']
        grams = variant['grams']


    product = {
        'Id': id,
        'Title': title,
        'Handle': handle,
        'Published_date': published_at,
        'Created_date': created_at,
        'Product_Type': product_type,
        'Sku': sku,
        'Price': price,
        'Available': available,
        'Grams': grams,
        'Image': imagesrc

    }
    product_list.append(product)

data = pd.DataFrame(product_list, columns=['Id', 'Title', 'Handle', 'Published_date', 'Created_date', 'Product_Type', 'Sku',
                                           'Price', 'Available', 'Grams', 'Image'])
data.to_csv('shopify_helmboots_json.csv', index=False, encoding='utf-8')
print(data)
