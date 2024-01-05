import unittest
import re
from src.main.lab import retrieveVector, similarPairExercise, retrieveSimilarWordsExercise,w2vDoesntMatchExercise
import gensim.downloader as api

class TestWord2VecExercises(unittest.TestCase):
    w2v = api.load('word2vec-google-news-300')
    def test_retrieveVector(self):
        
        test = 'cat'
        expectation = self.w2v['cat']

        result = retrieveVector(test)

        self.assertTrue((expectation == result).all())

    def test_retrieveVector_2(self):
        test = "revature"
        expectation = -1;
        result = retrieveVector(test)

        self.assertEqual(expectation, result)

    def test_similarPairExercise(self):
        result = similarPairExercise()
        self.assertTrue(result>0.4)

    def test_retrieveSimilarWordsExercise(self):
        testLimit = 2
        result = retrieveSimilarWordsExercise(testLimit)
        self.assertTrue(len(result) <= testLimit)
    
    def test_w2DoesntMatchExercise(self):
        words = ["cat","feline","dog"]
        result = w2vDoesntMatchExercise(words)
        self.assertEqual(self.w2v.doesnt_match(words), result)
    

if __name__ == '__main__':
    unittest.main()