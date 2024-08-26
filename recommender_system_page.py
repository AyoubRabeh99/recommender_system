import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import precision_recall_curve
from load_data import load_data


# Préparation des données
data = load_data()

# Création de la matrice utilisateur-livre
user_book_matrix = data.pivot_table(index='user_id', columns='name', values='user_rating')

# Calcul de la similarité entre les livres
def compute_book_similarity(user_book_matrix):
    matrix_filled = user_book_matrix.fillna(0)
    similarity = cosine_similarity(matrix_filled.T)
    book_similarity = pd.DataFrame(similarity, index=user_book_matrix.columns, columns=user_book_matrix.columns)
    return book_similarity

# Calcul de la similarité entre les livres
book_similarity = compute_book_similarity(user_book_matrix)

# Fonction pour recommander des livres similaires
def recommend_books(book_name, book_similarity, top_n=10):
    if book_name not in book_similarity.columns:
        st.error(f"Book '{book_name}' not found in the similarity matrix.")
        return []
    
    similar_scores = book_similarity[book_name].sort_values(ascending=False)
    similar_books = similar_scores[similar_scores.index != book_name].head(top_n).index.tolist()
    return similar_books

# Évaluation de la précision et du rappel
def precision_recall_at_k(test_data, book_similarity, k=10):
    y_true = []
    y_scores = []
    
    for user_id in test_data['user_id'].unique():
        user_data = test_data[test_data['user_id'] == user_id]
        actual_books = user_data['name'].values
        for book in actual_books:
            recommended_books = recommend_books(book, book_similarity, top_n=k)
            y_true.extend([1 if b in actual_books else 0 for b in recommended_books])
            y_scores.extend([1] * len(recommended_books))
    
    if not y_true:
        return 0, 0
    
    precision, recall, _ = precision_recall_curve(y_true, y_scores)
    return precision.mean(), recall.mean()

# Préparer les données de test
test_data = data.sample(frac=0.2, random_state=42)  # Utiliser 20% des données comme test

# Évaluation
precision, recall = precision_recall_at_k(test_data, book_similarity)

def show_recommender_system_page():

    # Interface utilisateur Streamlit
    st.title("Système de Recommandation de Livres")

    # Affichage des métriques d'évaluation
    st.write(f"**Precision:** {precision:.2f}")
    st.write(f"**Recall:** {recall:.2f}")

    # Sélecteur de livre
    book_name = st.selectbox('Choisissez un livre pour obtenir des recommandations:', user_book_matrix.columns)

    # Saisie du nombre de recommandations
    n_recommendations = st.slider('Nombre de livres similaires à recommander:', min_value=1, max_value=20, value=10)

    if book_name:
        # Recommandations
        recommended_books = recommend_books(book_name, book_similarity, top_n=n_recommendations)
        if recommended_books:
            st.write(f"### Livres similaires à '{book_name}':")
            st.write(recommended_books)
        else:
            st.write(f"Aucun livre similaire trouvé pour '{book_name}'.")
