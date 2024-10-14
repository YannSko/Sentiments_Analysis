import pandas as pd
from preprocess import TextPreprocessor

def load_and_preprocess_data():
    
    df = pd.read_csv("https://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz", delimiter='\t')
    
    # Extraction des données et étiquettes
    X = df['review']
    y = df['sentiment']  # 1 = positif, 0 = négatif
    
    # Prétraitement des textes
    preprocessor = TextPreprocessor()
    X_preprocessed = X.apply(preprocessor.preprocess)
    
    return X_preprocessed, y
