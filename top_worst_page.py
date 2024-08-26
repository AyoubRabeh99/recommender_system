import streamlit as st
import pandas as pd
from load_data import load_data
from top_worst_functions import (
    top_n_books_by_combined_score,
    top_n_genres_by_combined_score,
    top_n_authors_by_combined_score,
    worst_n_books_by_combined_score,
    worst_n_genres_by_combined_score,
    worst_n_authors_by_combined_score,
    top_n_books_by_rating,
    top_n_genres_by_rating,
    top_n_authors_by_rating,
    worst_n_books_by_rating,
    worst_n_genres_by_rating,
    worst_n_authors_by_rating
)

# Fonction principale de l'application Streamlit
def show_top_worst():
    # Charger les données
    data = load_data()

    # Titre de l'application
    st.title("Analyse des Livres, Genres et Auteurs")

    # Menu pour choisir entre Top N et Pire N
    option = st.sidebar.selectbox(
        'Sélectionnez une option',
        ['Top N', 'Pire N']
    )

    # Champ pour entrer la valeur de n
    n = st.sidebar.slider('Sélectionnez le nombre de résultats (N)', min_value=1, max_value=20, value=5)

    # Menu pour choisir le type de tri
    criteria = st.sidebar.selectbox(
        'Choisissez le critère',
        ['avg_rating et no_of_ratings', 'avg_rating uniquement']
    )

    # Conditions pour afficher les résultats
    if option == 'Top N':
        if criteria == 'avg_rating et no_of_ratings':
            top_books = top_n_books_by_combined_score(data, n)
            top_genres = top_n_genres_by_combined_score(data, n)
            top_authors = top_n_authors_by_combined_score(data, n)
            st.write("### Top Livres (avg_rating et no_of_ratings)")
            st.dataframe(top_books)
            st.write("### Top Genres (avg_rating et no_of_ratings)")
            st.dataframe(top_genres)
            st.write("### Top Auteurs (avg_rating et no_of_ratings)")
            st.dataframe(top_authors)
        elif criteria == 'avg_rating uniquement':
            top_books = top_n_books_by_rating(data, n)
            top_genres = top_n_genres_by_rating(data, n)
            top_authors = top_n_authors_by_rating(data, n)
            st.write("### Top Livres (avg_rating uniquement)")
            st.dataframe(top_books)
            st.write("### Top Genres (avg_rating uniquement)")
            st.dataframe(top_genres)
            st.write("### Top Auteurs (avg_rating uniquement)")
            st.dataframe(top_authors)

    elif option == 'Pire N':
        if criteria == 'avg_rating et no_of_ratings':
            worst_books = worst_n_books_by_combined_score(data, n)
            worst_genres = worst_n_genres_by_combined_score(data, n)
            worst_authors = worst_n_authors_by_combined_score(data, n)
            st.write("### Pires Livres (avg_rating et no_of_ratings)")
            st.dataframe(worst_books)
            st.write("### Pires Genres (avg_rating et no_of_ratings)")
            st.dataframe(worst_genres)
            st.write("### Pires Auteurs (avg_rating et no_of_ratings)")
            st.dataframe(worst_authors)
        elif criteria == 'avg_rating uniquement':
            worst_books = worst_n_books_by_rating(data, n)
            worst_genres = worst_n_genres_by_rating(data, n)
            worst_authors = worst_n_authors_by_rating(data, n)
            st.write("### Pires Livres (avg_rating uniquement)")
            st.dataframe(worst_books)
            st.write("### Pires Genres (avg_rating uniquement)")
            st.dataframe(worst_genres)
            st.write("### Pires Auteurs (avg_rating uniquement)")
            st.dataframe(worst_authors)

"""if __name__ == "__main__":
    main()"""
