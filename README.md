Sentiments Analysis with :
Streamlit, PostgreSQL, Docker & MLflow
Description

Ce projet utilise une application Streamlit pour réaliser une analyse des sentiments sur des critiques de films. L'application est connectée à une base de données PostgreSQL pour stocker les avis et utilise MLflow pour suivre et gérer les expérimentations d'entraînement du modèle de machine learning. Le projet est entièrement dockerisé avec Docker Compose, ce qui permet de démarrer l'application et ses services facilement.
Fonctionnalités principales :

    1 Analyse des sentiments : Saisie d'une critique de film via l'interface Streamlit, prédiction si l'avis est positif ou négatif.
    2 Téléversement CSV : Importation de nouveaux avis via un fichier CSV et ajout à la base de données.
    3 Réentraînement du modèle : Réentraîne le modèle avec les nouvelles données ajoutées à la base de données.
    4 Tracking avec MLflow : Suit les métriques d'entraînement et enregistre les modèles à chaque réentraînement.
    5 Base de données PostgreSQL : Stocke les avis des utilisateurs et les nouvelles données.
    6 Dockerisé : Utilisation de Docker Compose pour orchestrer l'application, la base de données PostgreSQL, et le serveur MLflow.

Technologies

    Python : Langage de programmation principal.
    Streamlit : Framework pour créer des interfaces web interactives.
    PostgreSQL : Base de données relationnelle pour stocker les avis.
    MLflow : Outil pour suivre et gérer les expérimentations de machine learning.
    Docker & Docker Compose : Outils de conteneurisation pour déployer facilement l'application et ses services.

Installation et Configuration
1. Cloner le dépôt

Commence par cloner le dépôt sur ta machine locale :

bash

git clone https://github.com/your-username/sentiment-analysis-app.git
cd sentiment-analysis-app

2. Installer les dépendances Python (si utilisé hors Docker)

Si tu exécutes le projet localement sans Docker, installe les dépendances via pip :

bash

pip install -r requirements.txt

3. Démarrer avec Docker Compose

Le projet est entièrement dockerisé. Utilise Docker Compose pour démarrer l'application, la base de données PostgreSQL et le serveur MLflow.
a. Construire et démarrer les conteneurs :

Assure-toi d'avoir Docker et Docker Compose installés sur ta machine, puis exécute la commande suivante dans le répertoire racine du projet :

bash

docker-compose up --build

Cela démarre trois services :

    L'application Streamlit (disponible à http://localhost:8501)
    La base de données PostgreSQL (exposée sur le port 5432)
    Le serveur MLflow (disponible à http://localhost:5000)

4. Accéder à l'application
a. Streamlit App :

Une fois les conteneurs démarrés, tu peux accéder à l'interface Streamlit en ouvrant ton navigateur à l'adresse suivante :

bash

http://localhost:8501

    Analyse des Sentiments : Saisie de texte ou téléversement d'un fichier CSV pour l'analyse des sentiments.
    Réentraînement du modèle : Réentraîne le modèle avec les nouvelles données ajoutées à la base.

b. MLflow UI :

Pour suivre et visualiser les expérimentations d'entraînement du modèle, accède à l'interface MLflow UI à l'adresse suivante :

bash

http://localhost:5000

Cette interface te permet de voir les métriques, les paramètres et les artefacts associés à chaque réentraînement du modèle.
5. Persistance des données

    Base de données PostgreSQL : Les avis et autres données persistantes sont stockés dans la base de données PostgreSQL, qui est montée sur un volume Docker.
    Artefacts MLflow : Les modèles entraînés et autres artefacts sont également sauvegardés dans un volume Docker dédié.

6. Tests unitaires et linting

Le projet inclut des tests unitaires pour vérifier le bon fonctionnement du code, ainsi qu'un système de linting pour garantir la qualité du code.
a. Exécuter les tests unitaires :

Tu peux exécuter les tests unitaires via Docker Compose :

bash

docker-compose run app python -m unittest discover -s tests/

b. Exécuter le linting :

Pour exécuter flake8 et vérifier le respect des normes PEP8 :

bash

docker-compose run app flake8 .

Contribution

Les contributions sont les bienvenues ! N'hésite pas à soumettre des pull requests ou à ouvrir des issues pour toute suggestion d'amélioration.
Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.