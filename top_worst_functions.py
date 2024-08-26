import pandas as pd
import numpy as np
from load_data import load_data

# Top N en fonction de avg_rating et no_of_ratings
def top_n_books_by_combined_score(data, n):
    # Calculer une métrique combinée pour les livres : avg_rating * no_of_ratings
    data['combined_score'] = data['avg_rating'] * data['no_of_ratings']
    
    # Trier les livres par la métrique combinée en ordre décroissant
    sorted_books = data.sort_values(by='combined_score', ascending=False)
    
    # Supprimer les doublons basés sur les colonnes clés (name, genre, author)
    sorted_books = sorted_books.drop_duplicates(subset=['name', 'genre', 'author'])
    
    # Prendre les n premiers livres
    top_books = sorted_books.head(n)
    
    # Sélectionner et organiser les colonnes nécessaires
    top_books_df = top_books[['name', 'genre', 'author', 'avg_rating', 'no_of_ratings']]
    
    return top_books_df

def top_n_genres_by_combined_score(data, n):
    # Calculer la moyenne des avg_rating et la somme des no_of_ratings par genre
    genre_stats = data.groupby('genre').agg({
        'avg_rating': 'mean',
        'no_of_ratings': 'sum'
    }).reset_index()
    
    # Calculer une métrique combinée pour chaque genre
    genre_stats['combined_score'] = genre_stats['avg_rating'] * genre_stats['no_of_ratings']
    
    # Meilleur auteur et livre dans chaque genre
    best_authors = data.loc[data.groupby('genre')['avg_rating'].idxmax()][['genre', 'author']].drop_duplicates()
    best_books = data.loc[data.groupby('genre')['avg_rating'].idxmax()][['genre', 'name']].drop_duplicates()

    # Fusionner les informations pour chaque genre
    genre_stats = genre_stats.merge(best_authors, on='genre').merge(best_books, on='genre')
    
    # Renommer les colonnes
    genre_stats.columns = ['Genre', 'Avg Rating', 'No of Ratings', 'Combined Score', 'Best Author', 'Best Book']
    # Trier par la métrique combinée et prendre les n premiers genres
    top_genres_df = genre_stats.sort_values(by='Combined Score', ascending=False).head(n)
    return top_genres_df

def top_n_authors_by_combined_score(data, n):
    # Calculer la moyenne des avg_rating et la somme des no_of_ratings par auteur
    author_stats = data.groupby('author').agg({
        'name': lambda x: ', '.join(x),
        'genre': lambda x: ', '.join(set(x)),
        'avg_rating': 'mean',
        'no_of_ratings': 'sum'
    }).reset_index()
    
    # Calculer une métrique combinée pour chaque auteur
    author_stats['combined_score'] = author_stats['avg_rating'] * author_stats['no_of_ratings']
    
    # Renommer les colonnes
    author_stats.columns = ['Author', 'Books', 'Genres', 'Avg Rating', 'No of Ratings', 'Combined Score']
    # Trier par la métrique combinée et prendre les n premiers auteurs
    top_authors_df = author_stats.sort_values(by='Combined Score', ascending=False).head(n)
    return top_authors_df

# Pire N en fonction de avg_rating et no_of_ratings
def worst_n_books_by_combined_score(data, n):
    # Calculer une métrique combinée pour les livres : avg_rating * no_of_ratings
    data['combined_score'] = data['avg_rating'] * data['no_of_ratings']
    
    # Trier les livres par la métrique combinée en ordre croissant
    sorted_books = data.sort_values(by='combined_score', ascending=True)
    
    # Supprimer les doublons basés sur les colonnes clés (name, genre, author)
    sorted_books_unique = sorted_books.drop_duplicates(subset=['name', 'genre', 'author'])
    
    # Prendre les n premiers livres (les pires)
    worst_books = sorted_books_unique.head(n)
    
    # Sélectionner et organiser les colonnes nécessaires
    worst_books_df = worst_books[['name', 'genre', 'author', 'avg_rating', 'no_of_ratings']]
    
    return worst_books_df

def worst_n_genres_by_combined_score(data, n):
    # Calculer la moyenne des avg_rating et la somme des no_of_ratings par genre
    genre_stats = data.groupby('genre').agg({
        'avg_rating': 'mean',
        'no_of_ratings': 'sum'
    }).reset_index()
    
    # Calculer une métrique combinée pour chaque genre
    genre_stats['combined_score'] = genre_stats['avg_rating'] * genre_stats['no_of_ratings']
    
    # Meilleur auteur et livre dans chaque genre
    best_authors = data.loc[data.groupby('genre')['avg_rating'].idxmax()][['genre', 'author']].drop_duplicates()
    best_books = data.loc[data.groupby('genre')['avg_rating'].idxmax()][['genre', 'name']].drop_duplicates()

    # Fusionner les informations pour chaque genre
    genre_stats = genre_stats.merge(best_authors, on='genre').merge(best_books, on='genre')
    
    # Renommer les colonnes
    genre_stats.columns = ['Genre', 'Avg Rating', 'No of Ratings', 'Combined Score', 'Worst Author', 'Worst Book']
    
    # Trier par la métrique combinée et prendre les n derniers genres (les pires)
    worst_genres_df = genre_stats.sort_values(by='Combined Score', ascending=True).head(n)
    
    return worst_genres_df

def worst_n_authors_by_combined_score(data, n):
    # Calculer la moyenne des avg_rating et la somme des no_of_ratings par auteur
    author_stats = data.groupby('author').agg({
        'name': lambda x: ', '.join(x),
        'genre': lambda x: ', '.join(set(x)),
        'avg_rating': 'mean',
        'no_of_ratings': 'sum'
    }).reset_index()
    
    # Calculer une métrique combinée pour chaque auteur
    author_stats['combined_score'] = author_stats['avg_rating'] * author_stats['no_of_ratings']
    
    # Renommer les colonnes
    author_stats.columns = ['Author', 'Books', 'Genres', 'Avg Rating', 'No of Ratings', 'Combined Score']
    
    # Trier par la métrique combinée et prendre les n derniers auteurs (les pires)
    worst_authors_df = author_stats.sort_values(by='Combined Score', ascending=True).head(n)
    
    return worst_authors_df

# Top N en fonction de avg_rating uniquement
def top_n_books_by_rating(data, n):
    # Trier les livres par avg_rating de manière décroissante
    top_books = data.sort_values(by='avg_rating', ascending=False).head(n)
    # Sélectionner et organiser les colonnes nécessaires
    top_books_df = top_books[['name', 'genre', 'author', 'avg_rating', 'no_of_ratings']]
    return top_books_df

def top_n_genres_by_rating(data, n):
    # Calculer les statistiques par genre
    genre_stats = data.groupby('genre').agg({
        'avg_rating': 'mean',
        'no_of_ratings': 'sum'
    }).reset_index()
    
    # Meilleur auteur et livre dans chaque genre
    best_authors = data.loc[data.groupby('genre')['avg_rating'].idxmax()][['genre', 'author']].drop_duplicates()
    best_books = data.loc[data.groupby('genre')['avg_rating'].idxmax()][['genre', 'name']].drop_duplicates()

    # Fusionner les informations pour chaque genre
    genre_stats = genre_stats.merge(best_authors, on='genre').merge(best_books, on='genre')
    
    # Renommer les colonnes
    genre_stats.columns = ['Genre', 'Avg Rating', 'No of Ratings', 'Best Author', 'Best Book']
    # Trier par la moyenne des notes et prendre les n premiers genres
    top_genres_df = genre_stats.sort_values(by='Avg Rating', ascending=False).head(n)
    return top_genres_df

def top_n_authors_by_rating(data, n):
    # Calculer les statistiques par auteur
    author_stats = data.groupby('author').agg({
        'name': lambda x: ', '.join(x),
        'genre': lambda x: ', '.join(set(x)),
        'avg_rating': 'mean',
        'no_of_ratings': 'sum'
    }).reset_index()
    
    # Renommer les colonnes
    author_stats.columns = ['Author', 'Books', 'Genres', 'Avg Rating', 'No of Ratings']
    # Trier par la moyenne des notes et prendre les n premiers auteurs
    top_authors_df = author_stats.sort_values(by='Avg Rating', ascending=False).head(n)
    return top_authors_df

# Pire N en fonction de avg_rating uniquement
def worst_n_books_by_rating(data, n):
    # Trier les livres par avg_rating de manière croissante
    worst_books = data.sort_values(by='avg_rating', ascending=True).head(n)
    # Sélectionner et organiser les colonnes nécessaires
    worst_books_df = worst_books[['name', 'genre', 'author', 'avg_rating', 'no_of_ratings']]
    return worst_books_df

def worst_n_genres_by_rating(data, n):
    # Calculer les statistiques par genre
    genre_stats = data.groupby('genre').agg({
        'avg_rating': 'mean',
        'no_of_ratings': 'sum'
    }).reset_index()
    
    # Meilleur auteur et livre dans chaque genre
    best_authors = data.loc[data.groupby('genre')['avg_rating'].idxmax()][['genre', 'author']].drop_duplicates()
    best_books = data.loc[data.groupby('genre')['avg_rating'].idxmax()][['genre', 'name']].drop_duplicates()

    # Fusionner les informations pour chaque genre
    genre_stats = genre_stats.merge(best_authors, on='genre').merge(best_books, on='genre')
    
    # Renommer les colonnes
    genre_stats.columns = ['Genre', 'Avg Rating', 'No of Ratings', 'Best Author', 'Best Book']
    # Trier par la moyenne des notes et prendre les n derniers genres (les pires)
    worst_genres_df = genre_stats.sort_values(by='Avg Rating', ascending=True).head(n)
    return worst_genres_df

def worst_n_authors_by_rating(data, n):
    # Calculer les statistiques par auteur
    author_stats = data.groupby('author').agg({
        'name': lambda x: ', '.join(x),
        'genre': lambda x: ', '.join(set(x)),
        'avg_rating': 'mean',
        'no_of_ratings': 'sum'
    }).reset_index()
    
    # Renommer les colonnes
    author_stats.columns = ['Author', 'Books', 'Genres', 'Avg Rating', 'No of Ratings']
    # Trier par la moyenne des notes et prendre les n derniers auteurs (les pires)
    worst_authors_df = author_stats.sort_values(by='Avg Rating', ascending=True).head(n)
    return worst_authors_df