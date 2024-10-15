import unittest
import psycopg2
import os

class TestDatabase(unittest.TestCase):
    
    def setUp(self):
        self.conn = psycopg2.connect(
            host="localhost",
            database="sentiment_db",
            user="postgres",
            password="password"
        )
        self.cur = self.conn.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS reviews (id SERIAL PRIMARY KEY, review TEXT, sentiment INTEGER)''')
        self.conn.commit()
    
    def test_add_review(self):
        review = "This movie was amazing"
        sentiment = 1
        self.cur.execute("INSERT INTO reviews (review, sentiment) VALUES (%s, %s)", (review, sentiment))
        self.conn.commit()
        self.cur.execute("SELECT * FROM reviews WHERE review=%s", (review,))
        result = self.cur.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result[1], review)
        self.assertEqual(result[2], sentiment)
    
    def tearDown(self):
        self.cur.execute("DROP TABLE IF EXISTS reviews")
        self.conn.commit()
        self.conn.close()

if __name__ == '__main__':
    unittest.main()
