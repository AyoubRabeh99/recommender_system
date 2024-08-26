import pandas as pd

def load_data(path_books="books.csv", path_listing="listing.csv"):
    """
    Cette fonction charge les données des fichiers CSV et les fusionne en un seul DataFrame.

    Args:
    - path_books (str): Chemin vers le fichier books.csv
    - path_listing (str): Chemin vers le fichier listing.csv

    Returns:
    - pd.DataFrame: DataFrame fusionné contenant les données des deux fichiers
    """
    # Chargement des données
    books = pd.read_csv(path_books)
    listing = pd.read_csv(path_listing, encoding="ISO-8859-1")

    # Fusion des datasets
    data = pd.merge(books, listing, on='book_id')
    
    return data
