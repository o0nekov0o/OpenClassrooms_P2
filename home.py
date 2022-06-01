import category_2

web_url = 'http://books.toscrape.com/index.html'

def save_pages_part1(web_url):
    """
    Save all books from the homepage (it handles pagination)
    """
    web_url = 'http://books.toscrape.com/catalogue/category/books_1/page-1.html'
    for nb in range(1):  # afin de mettre try dans une boucle
        try:
            category_2.save_one_category(web_url)  # même variable pour appeler fonction
        except AttributeError:  # si description absente
            continue

def save_pages_part2(web_url):
    """
    Save all books from the homepage (it handles pagination)
    """
    web_url = 'http://books.toscrape.com/catalogue/category/books_1/page-10.html'
    for nb in range(1):  # afin de mettre try dans une boucle
        try:
            category_2.save_one_category(web_url)  # même variable pour appeler fonction
        except AttributeError:  # si description absente
            continue
            
save_pages_part1(web_url)
save_pages_part2(web_url)

if __name__ == "__main__":
    book_data = get_book_data(EXAMPLE_URL)
    save_book_csv(book_data)
    save_one_category(index_url)
    save_pages_part1(web_url)
    save_pages_part2(web_url)
    save_image_file(url_image)
