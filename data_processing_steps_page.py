import streamlit as st

# Fonction pour afficher la page des étapes de traitement des données
def show_data_processing_steps_page():
    # Titre principal de la page
    st.title("Étapes de Traitement des Données")

    # Introduction
    st.write("""
    Dans cette section, nous décrivons les différentes étapes de traitement des données qui ont été effectuées 
    pour préparer les données avant l'analyse. Ces étapes sont essentielles pour garantir la qualité et la fiabilité des résultats.
    """)

    # Étape 1: Suppression des valeurs manquantes
    st.header("1. Suppression des valeurs manquantes")
    st.write("""
    La première étape consiste à supprimer les lignes qui contiennent des valeurs manquantes. 
    Cette action est cruciale pour éviter les biais dans les analyses ultérieures, car les valeurs manquantes peuvent fausser les résultats.
    """)

    # Étape 2: Vérification et suppression des doublons
    st.header("2. Vérification et suppression des doublons")
    st.write("""
    Ensuite, nous avons vérifié l'existence de doublons dans les données. 
    Les doublons peuvent entraîner une sur-représentation de certaines observations, 
    ce qui pourrait nuire à la précision des modèles d'analyse et de recommandation. 
    Les doublons identifiés ont été supprimés.
    """)

    # Étape 3: Vérification des valeurs aberrantes dans les évaluations (ratings)
    st.header("3. Vérification des valeurs aberrantes dans les évaluations (ratings)")
    st.write("""
    Les valeurs aberrantes dans les évaluations des utilisateurs (user_rating) et les moyennes d'évaluation (avg_rating) 
    ont été identifiées et examinées. Les évaluations doivent se situer dans une plage valide, généralement de 0 à 5. 
    Toute évaluation en dehors de cette plage est considérée comme une valeur aberrante.
    """)

    # Étape 4: Statistiques descriptives pour les valeurs numériques et catégorielles
    st.header("4. Statistiques descriptives pour les valeurs numériques et catégorielles")
    st.write("""
    Des statistiques descriptives ont été calculées pour les variables numériques et catégorielles. 
    Cela inclut la distribution des évaluations, des genres et des auteurs. 
    Ces statistiques fournissent un aperçu général des données et aident à détecter d'éventuels problèmes.
    """)

    # Étape 5: Nettoyage des espaces dans les colonnes catégorielles
    st.header("5. Nettoyage des espaces dans les colonnes catégorielles")
    st.write("""
    Enfin, les espaces en début et en fin de texte dans les colonnes catégorielles (comme les noms des genres et des auteurs) 
    ont été supprimés. Cela garantit que les mêmes valeurs sont correctement identifiées et traitées uniformément.
    """)

    # Conclusion
    st.write("""
    Ces étapes de traitement des données sont essentielles pour préparer les données pour des analyses précises 
    et pour garantir que les résultats de l'application de recommandation soient fiables et pertinents.
    """)

"""# Appel de la fonction pour afficher la page de traitement des données
if __name__ == "__main__":
    show_data_processing_steps_page()
"""