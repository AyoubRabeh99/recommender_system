import streamlit as st

def main():
    # Titre de l'application
    st.title("Application de Recommandation de Livres")

    # Navigation entre les pages
    st.sidebar.header("Navigation")
    page = st.sidebar.radio("Choisissez une page", ["Présentation","Traitement des données", "Exploration des données","Top et Pires","Recommandation"])

    if page == "Présentation":
        import intro_page
        intro_page.show_intro_page()
    
    elif page == "Traitement des données":
        import data_processing_steps_page
        data_processing_steps_page.show_data_processing_steps_page()
    
    elif page == "Exploration des données":
        import data_exploration_page
        data_exploration_page.show_data_exploration_page()

    elif page == "Recommandation":
        import recommender_system_page
        recommender_system_page.show_recommender_system_page()
    elif page == "Top et Pires":
        import top_worst_page
        top_worst_page.show_top_worst()

if __name__ == "__main__":
    main()
