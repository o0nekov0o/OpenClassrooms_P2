
# Utilisez les bases de Python pour l'analyse de marché (Projet No.2 OpenClassrooms)

Ci-après le détail des éléments présents dans ce répertoire :
- script de récupération de données vers un fichier CSV à partir du site http://books.toscrape.com/
- tous les fichiers présents en racine servent à l'exécution du script (départagé en plusieurs fichiers)
- procéder à l'utilisation en exécutant les fichiers home.py ou main.py au choix (récupération données livres)
(au préalable installer les paquets nécessaires ainsi que leurs dépendances à l'aide du fichier requirements)
- création automatique, après exécution, des sous-répertoires "scraping_csv" et "scraping_img" pour stocker les données
(un fichier excel pour chaque catégorie, ainsi que les images, de chacun des produits du site)

## Voici ci-dessous une aide pour procéder aux étapes d'installation
A l'aide de votre invite de commandes, placez-vous à la racine du répertoire téléchargé.
Lancez-y ensuite la commande suivante afin de créer votre environnement virtuel :
```bash
  python -m venv env
```
Depuis Windows, exécutez la commande suivante pour activer votre environnement virtuel :
```bash
  call env/Scripts/activate.bat
```
Si jamais cela ne fonctionne pas, exécutez Powershell en tant qu'administrateur. Une fois que la nouvelle invite de commandes est alors ouverte, exécutez-y le code suivant :
```bash
  Set-ExecutionPolicy RemoteSigned
```
Une fois que cela est fait, revenez à votre première invite de commandes puis entrez-y : 
```bash
  env/Scripts/activate
```
Depuis un autre OS, vous n'aurez qu'à rentrer ceci à l'intérieur de votre invite de commandes afin de pouvoir activer votre environnement virtuel (Mac/Linux/Autres systèmes) :
```bash
  source env/bin/activate
```
Enfin, pour installer les paquets requis, rentrez ensuite le code ci-dessous :
```bash
  pip install -r requirements.txt
