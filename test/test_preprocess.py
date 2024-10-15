import unittest
from preprocess import TextPreprocessor

class TestTextPreprocessor(unittest.TestCase):
    
    def setUp(self):
        self.preprocessor = TextPreprocessor()

    def test_tokenization(self):
        text = "Natural language processing is fascinating!"
        result = self.preprocessor.preprocess(text)
        expected_tokens = "natural language processing fascinating"
        self.assertEqual(result, expected_tokens)
    
    def test_removal_stopwords(self):
        text = "This is a simple example"
        result = self.preprocessor.preprocess(text)
        expected_result = "simple example"
        self.assertEqual(result, expected_result)

    def test_lemmatization(self):
        text = "The cats are running"
        result = self.preprocessor.preprocess(text)
        expected_result = "cat run"
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
