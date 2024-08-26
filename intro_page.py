import streamlit as st

# Fonction pour afficher la page de présentation
def show_intro_page():
    # Configuration de la page

    # Titre principal
    st.title("Bienvenue dans l'Application de Recommandation de Livres 📚")

    # Introduction
    st.write("""
    Cette application est conçue pour vous offrir une expérience interactive d'exploration et de recommandation de livres. 
    Vous pourrez découvrir des livres intéressants, explorer des tendances dans les données, et obtenir des recommandations personnalisées basées sur la similarité entre les livres.
    """)

    # Objectifs de l'application
    st.header("Objectifs de l'Application")
    st.write("""
    L'application vise à :
    - **Explorer les Données des Livres :** Visualisez des statistiques et des graphiques pour comprendre les tendances et les caractéristiques des livres disponibles.
    - **Analyser les Meilleurs et Pires Livres :** Identifiez les livres, genres, et auteurs les mieux et les moins bien notés selon différentes métriques.
    - **Recommander des Livres :** Recevez des recommandations personnalisées en fonction de vos préférences et des similarités entre les livres.
    """)

    # Fonctionnalités principales
    ##st.header("Fonctionnalités Principales")
    ##st.write("""
    ##1. **Exploration des Données :** Analysez la répartition des genres, des auteurs, et les statistiques descriptives des variables numériques.
    #2. **Analyse des Top et Pires Livres :** Découvrez les meilleurs et les pires livres, genres et auteurs en fonction des notes et des évaluations.
    #3. **Système de Recommandation :** Recevez des suggestions de livres similaires basées sur la similarité des livres et des évaluations.

    #Utilisez les onglets ci-dessus pour naviguer entre les différentes sections de l'application.
    ##""")

    # Instructions d'utilisation
    st.header("Instructions d'Utilisation")
    st.write("""
    1. **Page de Traitement des Données :** Découvrez comment les données sont nettoyées et préparées avant l'analyse.
    2. **Page d'Exploration des Données :** Explorez les données à travers des graphiques interactifs.
    3. **Page des Top et Pires Livres :** Consultez les livres, genres, et auteurs les mieux et les moins bien notés.
    4. **Page du Système de Recommandation :** Entrez le titre d'un livre pour obtenir des recommandations personnalisées.

    Pour commencer, utilisez le menu de navigation à gauche pour accéder à chaque section de l'application.
    """)

    # Information de contact ou feedback
    st.header("Nous Contacter")
    st.write("""
    Pour toute question ou retour sur l'application, veuillez contacter l'équipe de développement à l'adresse suivante : [ayoub.rabeh1999@gmail.com](mailto:ayoub.rabeh1999@gmail.com).
    """)

    # Message de bienvenue ou note finale
    st.write("""
    Nous espérons que vous trouverez cette application utile et facile à utiliser. Bonnes explorations et bonnes lectures !
    """)

"""# Appel de la fonction pour afficher la page de présentation
if __name__ == "__main__":
    show_intro_page()
"""