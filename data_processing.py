import pandas as pd

def preprocess_data(data):
    """
    Cette fonction effectue les étapes de nettoyage et de préparation des données.
    Elle prend en entrée un DataFrame brut et retourne un DataFrame nettoyé.
    """
    # 1. Suppression des lignes avec des valeurs manquantes
    data_cleaned = data.dropna()
    print("Après suppression des valeurs manquantes :")
    print(data_cleaned.shape)

    # 2. Vérification et suppression des doublons
    duplicates = data_cleaned.duplicated()
    print(f"Nombre de doublons : {duplicates.sum()}")
    data_cleaned = data_cleaned.drop_duplicates()
    print("Après suppression des doublons :")
    print(data_cleaned.shape)

    # 3. Vérification des valeurs aberrantes dans les ratings
    print("Statistiques descriptives pour les ratings :")
    print(data_cleaned[['user_rating', 'avg_rating']].describe())

    # Identification des valeurs aberrantes dans user_rating
    user_rating_outliers = data_cleaned[(data_cleaned['user_rating'] < 0) | (data_cleaned['user_rating'] > 5)]
    print(f"Valeurs aberrantes dans user_rating :\n{user_rating_outliers}")

    # Identification des valeurs aberrantes dans avg_rating
    avg_rating_outliers = data_cleaned[(data_cleaned['avg_rating'] < 0) | (data_cleaned['avg_rating'] > 5)]
    print(f"Valeurs aberrantes dans avg_rating :\n{avg_rating_outliers}")

    # 4. Statistiques pour les valeurs numériques et catégoriques
    print("Statistiques descriptives pour les variables numériques :")
    print(data_cleaned.describe())

    print("Distribution des genres :")
    print(data_cleaned['genre'].value_counts())

    print("Distribution des auteurs :")
    print(data_cleaned['author'].value_counts())

    # 5. Suppression des espaces en début et en fin de texte pour chaque colonne catégorielle
    categorical_columns = data_cleaned.select_dtypes(include=['object']).columns

    for col in categorical_columns:
        data_cleaned[col] = data_cleaned[col].str.strip()

    # Vérification des résultats
    print(data_cleaned[categorical_columns].head())

    return data_cleaned

"""# Exemple d'utilisation (peut être supprimé ou commenté si le fichier est uniquement importé dans d'autres scripts)
if __name__ == "__main__":
    # Chargement des données brutes (remplacer par le chemin de vos données)
    data = pd.read_csv('path_to_your_raw_data.csv')

    # Appel de la fonction de prétraitement
    data_cleaned = preprocess_data(data)

    # Optionnel : Sauvegarde des données nettoyées
    data_cleaned.to_csv('path_to_save_cleaned_data.csv', index=False)"""
