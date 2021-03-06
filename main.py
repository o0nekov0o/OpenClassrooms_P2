import requests
from bs4 import BeautifulSoup

import category

site_url = 'https://books.toscrape.com/index.html'  # global var

def save_all_categories(site_url):
    """
    Save all data of the books
    of the entire category (it handles pagination)
    and for each site's category
    """
    global links  # reutilisation apres boucle
    url = site_url  # preserve global var
    response = requests.get(url)  # 200 si ok
    print(response)  # afficher code retour
    if response.ok:  # si justement ok
        soup = BeautifulSoup(response.text, features='html.parser')  # format txt, delete warnings
        for x in soup.find_all('ul', {'class': 'nav nav-list'}):  # unique classe 'nav nav-list' mais find_all iteration
            links = x.find('ul').find_all('a')  # autre ul, lister tous les lien des iterations
        for n in range(len(links)):  # parcourir toute la liste de liens récupérés
            link = links[n]['href'].replace('catalogue', 'http://books.toscrape.com/catalogue')  # affecter dans variable
            category.save_one_category(link)  # même variable pour appeler fonction

save_all_categories(site_url)

if __name__ == "__main__":
    book_data = get_book_data(EXAMPLE_URL)
    save_book_csv(book_data)
    save_one_category(index_url)
    save_all_categories(site_url)
    save_image_file(url_image)