import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

class TextPreprocessor:
    def __init__(self):
        self.stop_words = set(stopwords.words("english"))
        self.lemmatizer = WordNetLemmatizer()
        
    def preprocess(self, text):
        # Tokenization
        tokens = word_tokenize(text.lower())
        
        # Suppression des stopwords
        tokens = [word for word in tokens if word not in self.stop_words and word.isalpha()]
        
        # Lemmatization
        tokens = [self.lemmatizer.lemmatize(word) for word in tokens]
        
        return " ".join(tokens)
