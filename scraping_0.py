class save_image_global: # pour créer fonction global
    global save_image_file # car appelé avant par get_book_data
    def save_image_file(url_image):
        if os.path.isdir('scraping_images') == False: # si le dossier n'existe pas 
            os.makedirs('scraping_images') # alors procéder à sa création
        img_url = url_image.replace('http://books.toscrape.com/media/cache/','').replace('/','_') # preparer nom image
        img_data = requests.get(url_image).content # preparer contenu image
        with open(f'scraping_images/{img_url}', 'wb') as handler: # from prepared image name
            handler.write(img_data) # ecrire contenu image (dessiner l'img)