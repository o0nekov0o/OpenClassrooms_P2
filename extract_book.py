import requests
from bs4 import BeautifulSoup

import save_image

EXAMPLE_URL = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'  # global var

def get_book_data(EXAMPLE_URL):
    """
    Extract all data of the book
    """
    url = EXAMPLE_URL
    response = requests.get(url)  # 200 si ok
    print(response)  # affichage code retour
    if response.ok:  # si justement ok
        soup = BeautifulSoup(response.text, features='html.parser')  # format txt, delete warnings
        product_page_url = url  # soup.find pour nom classe exacte, soup.select nom classe inexacte
        universal_product_code = soup.find('th', text='UPC').find_next_sibling('td').text  # colonne suivante, conversion txt
        title = soup.select('div.col-sm-6.product_main > h1')[0].text  # unique indice, conversion txt
        price_excluding_tax = soup.find('th', text='Price (excl. tax)').find_next_sibling('td').text.replace('Â', '')  # comme title, enleve specialchar
        price_including_tax = soup.find('th', text='Price (incl. tax)').find_next_sibling('td').text.replace('Â', '')  # comme title, enleve specialchar
        number_available = soup.find('th', text='Availability').find_next_sibling('td').text  # comme title, conversion txt
        product_description = soup.find('div', {'id': 'product_description'}).find_next_sibling('p').text  # comme title, balises differentes
        category = soup.find('li', {'class': 'active'}).find_previous_sibling('li').find('a').text  # inverse title, balises differentes, recuperation lien
        review_rating = f"{soup.select('p.star-rating')[0]['class'][1]} Star(s) on Five"  # print interpreter, comportement code, liste dans liste
        image_url = soup.select('div.item.active > img')[0]['src'].replace('../..', 'http://books.toscrape.com')  # comme review_rating, liste attribut src
        print(f"Product Page URL : {product_page_url}")  # fprint on evite, + et \n, code plus lisible
        print(f"UPC: {universal_product_code}")
        print(f"Title: {title}")
        print(f"Price Excluding Tax: {price_excluding_tax}")
        print(f"Price Including Tax: {price_including_tax}")
        print(f"Number Available: {number_available}")
        print(f"product_description: {product_description}")
        print(f"category: {category}")
        print(f"Review Rating: {review_rating}")
        print(f"Image URL: {image_url}")
        print('―' * 100)  # ligne separation
        save_image.save_image_file(image_url)  # appel fonction, sauvegarde image
        return {'Product Page URL': product_page_url, 'UPC': universal_product_code, 'Title': title,
                # strings headers, vars contents
                'Price Excluding Tax': price_excluding_tax, 'Price Including Tax': price_including_tax,
                # pour ecrire contenu sous headers correspondants
                'Number Available': number_available, 'Product Description': product_description,
                'Category': category, 'Review Rating': review_rating, 'Image URL': image_url}
