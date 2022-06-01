import requests
from bs4 import BeautifulSoup
import time

import extract_book
import load_book

index_url = 'http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html'  # global var

def save_one_category(index_url):
    """
    #Save all data of the books
    #of the entire category (it handles pagination)
    """
    suivant = 1  # permettra de relancer la boucle
    url = index_url  # preserve global var
    while suivant == 1:  # condition relance boucle
        response = requests.get(url)  # 200 si ok
        print(response)  # afficher code retour
        if response.ok:  # si justement ok
            soup = BeautifulSoup(response.text, features='html.parser')  # format txt, delete warnings
            for i in soup.find_all('div', {'class': 'image_container'}):  # plusieurs classes image_container
                lien = i.find('a')['href'].replace('../..', 'http://books.toscrape.com/catalogue')  # recup lien
                book_data = extract_book.get_book_data(lien)  # appel fonction get_book_data, retour dans book_data
                load_book.save_book_csv(book_data)  # appel foncion save_book_csv, enregistrer valeurs retournées
                time.sleep(0.00)  # meilleure lecture dans interpreter, si corrections bugs
            if soup.find('li', {'class': 'next'}):  # si presence bouton suivant
                base_url = url[:url.rfind('/')]  # sup derniere partie url (initialement index)
                suffix_url = soup.find('li', {'class': 'next'}).find('a')['href']  # isole lien bouton suivant
                url = f"{base_url}/{suffix_url}"  # ajout lien bouton suivant au reste
                # url = f"{url[:url.rfind('/')]}/{soup.find('li', {'class': 'next'}).find('a')['href']}"
                suivant = 1  # relancer la boucle (car bouton suivant present)
            else:
                suivant = 0  # sortir de la boucle (car bouton suivant absent)
