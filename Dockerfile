# Utiliser une image Python officielle
FROM python:3.9-slim

# Créer un répertoire de travail
WORKDIR /app

# Copier les fichiers requirements.txt dans le conteneur
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste des fichiers de l'application dans le conteneur
COPY . .

# Exposer le port sur lequel Streamlit fonctionne
EXPOSE 8501

# Commande pour lancer Streamlit
CMD ["streamlit", "run", "main.py"]
