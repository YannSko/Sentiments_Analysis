import mlflow
import mlflow.sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class SentimentModel:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(max_features=5000)
        self.model = LogisticRegression()
    
    def train(self, X, y):
        # Vectorisation et division des données
        X_vec = self.vectorizer.fit_transform(X)
        X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, random_state=42)
        
        # Démarrer une nouvelle session MLflow
        with mlflow.start_run():
            # Entraîner le modèle
            self.model.fit(X_train, y_train)
            
            # Faire des prédictions
            y_pred = self.model.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            
            # Loguer les métriques et hyperparamètres dans MLflow
            mlflow.log_param("max_features", 5000)
            mlflow.log_param("model", "LogisticRegression")
            mlflow.log_metric("accuracy", accuracy)
            
            # Enregistrer le modèle
            mlflow.sklearn.log_model(self.model, "model")
            
            print(f"Accuracy: {accuracy}")
    
    def predict(self, text):
        text_vec = self.vectorizer.transform([text])
        return self.model.predict(text_vec)[0]
    
    def retrain_model(self, X_new, y_new):
        # Ajouter les nouvelles données et réentraîner le modèle
        X_new_vec = self.vectorizer.transform(X_new)
        self.model.fit(X_new_vec, y_new)
        
        # Loguer le nouveau modèle dans MLflow
        with mlflow.start_run():
            mlflow.sklearn.log_model(self.model, "model")
            print("Modèle réentraîné et logué avec succès dans MLflow.")
