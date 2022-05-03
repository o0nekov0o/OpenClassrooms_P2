from extract_book import *

def save_book_csv(book_data):
    """
    Load all data of the book into csv
    """
    file_exists = os.path.isfile(f"scraping_{list(book_data.values())[7].replace(' ','_')}.csv") # permettra verifier si csv existe
    file = open(f"scraping_{list(book_data.values())[7].replace(' ','_')}.csv", 'a', encoding='utf-8') # retour get_book_data, value index 7, cat name
    headers = list(book_data) # retourne clés book_data dans liste pour headers
    writer = csv.DictWriter(file, fieldnames=headers) #preparation ecriture headers
    if not file_exists:
        writer.writeheader() # si fichier n'existe pas, ecrire headers creation
    writer.writerow(book_data) # ecrire contenu sous headers correspondants
    file.close()