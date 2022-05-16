import os
import csv


def save_book_csv(book_data):
    """
    Save all data of the book into csv
    """
    if os.path.isdir('scraping_csv') == False:  # si le dossier n'existe pas
        os.makedirs('scraping_csv')  # alors procéder à sa création
    file_exists = os.path.isfile(f"scraping/{list(book_data.values())[7].replace(' ', '_')}.csv")  # permettra verifier si csv existe
    file = open(f"scraping_csv/{list(book_data.values())[7].replace(' ', '_')}.csv", 'a',
                encoding='utf-8')  # retour get_book_data, value index 7, cat name
    headers = list(book_data)  # retourne clés book_data dans liste pour headers
    writer = csv.DictWriter(file, fieldnames=headers)  # preparation ecriture headers
    if not file_exists:
        writer.writeheader()  # si fichier n'existe pas, ecrire headers creation
    writer.writerow(book_data)  # ecrire contenu sous headers correspondants
    file.close()
