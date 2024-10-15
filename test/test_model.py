import unittest
import pandas as pd
from model import SentimentModel

class TestSentimentModel(unittest.TestCase):
    
    def setUp(self):
        self.model = SentimentModel()

    def test_train(self):
        X = pd.Series(["This movie was great", "I hated the movie", "It was okay", "Best movie ever"])
        y = pd.Series([1, 0, 0, 1])
        self.model.train(X, y)
        self.assertIsNotNone(self.model.model.coef_)
    
    def test_predict(self):
        X = pd.Series(["This movie was great", "I hated the movie"])
        y = pd.Series([1, 0])
        self.model.train(X, y)
        prediction = self.model.predict("This movie is fantastic")
        self.assertEqual(prediction, 1)

if __name__ == '__main__':
    unittest.main()
