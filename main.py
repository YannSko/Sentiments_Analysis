import streamlit as st
import psycopg2
import pandas as pd
from preprocess import TextPreprocessor
from model import SentimentModel
from data_loader import load_and_preprocess_data
import mlflow
import mlflow.sklearn

# Fonction pour initialiser la base de données PostgreSQL
def init_db():
    conn = psycopg2.connect(
        host="db",  # Le service 'db' est défini dans Docker Compose
        database="sentiment_db",
        user="postgres",
        password="password"
    )
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS reviews (
                    id SERIAL PRIMARY KEY, 
                    review TEXT, 
                    sentiment INTEGER)''')
    conn.commit()
    conn.close()

# Fonction pour ajouter un avis à la base de données
def add_review_to_db(review, sentiment):
    conn = psycopg2.connect(
        host="db",
        database="sentiment_db",
        user="postgres",
        password="password"
    )
    cur = conn.cursor()
    cur.execute("INSERT INTO reviews (review, sentiment) VALUES (%s, %s)", (review, sentiment))
    conn.commit()
    conn.close()

# Fonction pour récupérer toutes les données de la base
def get_all_reviews():
    conn = psycopg2.connect(
        host="db",
        database="sentiment_db",
        user="postgres",
        password="password"
    )
    reviews_df = pd.read_sql_query("SELECT * FROM reviews", conn)
    conn.close()
    return reviews_df

# Fonction pour entraîner le modèle initial
def train_sentiment_model():
    X, y = load_and_preprocess_data()
    sentiment_model = SentimentModel()
    sentiment_model.train(X, y)
    return sentiment_model, TextPreprocessor()

# Fonction pour retrainer avec les nouvelles données
def retrain_with_new_data(model):
    new_data = get_all_reviews()
    if len(new_data) > 0:
        X_new = new_data['review']
        y_new = new_data['sentiment']
        model.retrain_model(X_new, y_new)

# Interface Streamlit
def sentiment_analysis_app(model, preprocessor):
    st.title("Analyse des Sentiments")

    # Saisie de texte par l'utilisateur
    user_input = st.text_area("Entrez une critique de film :")
    
    if st.button("Analyser"):
        if user_input:
            preprocessed_text = preprocessor.preprocess(user_input)
            sentiment = model.predict(preprocessed_text)
            sentiment_str = "Positive" if sentiment == 1 else "Négative"
            st.write(f"Le sentiment prédit est : **{sentiment_str}**")
            
            # Sauvegarder l'avis dans la base de données
            sentiment_value = 1 if sentiment_str == "Positive" else 0
            add_review_to_db(user_input, sentiment_value)
            st.write("Votre avis a été ajouté à la base de données.")
        else:
            st.write("Veuillez entrer une critique de film.")
    
    # Téléverser un fichier CSV pour réentraînement
    uploaded_file = st.file_uploader("Importer un fichier CSV avec de nouveaux avis", type=["csv"])
    
    if uploaded_file is not None:
        new_data = pd.read_csv(uploaded_file)
        new_data = new_data.dropna()  # Supprimer les lignes vides
        for _, row in new_data.iterrows():
            add_review_to_db(row['review'], row['sentiment'])
        st.write("Les nouveaux avis ont été ajoutés à la base de données.")
    
    # Bouton pour réentraîner le modèle
    if st.button("Réentraîner le modèle avec les nouvelles données"):
        retrain_with_new_data(model)
        st.write("Le modèle a été réentraîné avec succès.")

# Point d'entrée
if __name__ == "__main__":
    init_db()
    st.write("Chargement du modèle d'analyse des sentiments...")
    model, preprocessor = train_sentiment_model()
    sentiment_analysis_app(model, preprocessor)
