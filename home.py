import category_2

web_url = 'https://books.toscrape.com/catalogue/category/books_1/index.html'  # global var

def save_home_pages(web_url):
    """
    Save all books of the home page (it handles pagination)
    """
    web_url = 'https://books.toscrape.com/catalogue/category/books_1/page-1.html'
    for nb in range(1):
        category_2.save_one_category(web_url)  # même variable pour appeler fonction

save_home_pages(web_url)

if __name__ == "__main__":
    book_data = get_book_data(EXAMPLE_URL)
    save_book_csv(book_data)
    save_one_category(index_url)
    save_all_categories(site_url)
    save_image_file(url_image)