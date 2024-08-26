import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from load_data import load_data

def plot_histograms(data, numeric_columns):
    st.subheader('Histogrammes des Variables Numériques')
    for col in numeric_columns:
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.hist(data[col], bins=20, edgecolor='black')
        ax.set_title(f'Histogramme de {col}')
        ax.set_xlabel(col)
        ax.set_ylabel('Fréquence')
        st.pyplot(fig)

def plot_boxplots(data, numeric_columns):
    st.subheader('Boxplots des Variables Numériques')
    for col in numeric_columns:
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.boxplot(x=data[col], ax=ax)
        ax.set_title(f'Boxplot de {col}')
        ax.set_xlabel(col)
        st.pyplot(fig)

def plot_correlation_matrix(data, numeric_columns):
    st.subheader('Matrice de Corrélation des Variables Numériques')
    fig, ax = plt.subplots(figsize=(10, 8))
    correlation_matrix = data[numeric_columns].corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', ax=ax)
    ax.set_title('Matrice de Corrélation des Variables Numériques')
    st.pyplot(fig)

def plot_count_plots(data, categorical_columns):
    st.subheader('Distribution des Variables Catégorielles')
    for col in categorical_columns:
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.countplot(y=data[col], order=data[col].value_counts().index, palette='Set2', ax=ax)
        ax.set_title(f'Distribution de {col}')
        ax.set_xlabel('Nombre d\'occurrences')
        ax.set_ylabel(col)
        st.pyplot(fig)

def show_data_exploration_page():
    # Page Streamlit
    st.title('Exploration des Données')

    # Charger les données
    data = load_data()

    # Séparer les variables numériques et catégorielles
    numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
    categorical_columns = data.select_dtypes(include=['object']).columns.tolist() + ['user_id', 'book_id']

    # Exclure user_id et book_id des variables numériques
    numeric_columns = [col for col in numeric_columns if col not in ['user_id', 'book_id']]

    # Afficher les graphiques directement
    plot_histograms(data, numeric_columns)
    plot_boxplots(data, numeric_columns)
    plot_correlation_matrix(data, numeric_columns)
    plot_count_plots(data, categorical_columns)

"""if __name__ == "__main__":
    show_data_exploration_page()
"""