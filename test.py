from Server import Server
import unittest

class TestFibonacci(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    """
    tests cleaning text on server.
    """
    def test_twitter(self):
        sent_scorer = Server.DataAnalysis()
        sentence = "[Dirty-] sentence that (/needs/) {cleaning}"
        ans = sent_scorer.clean(sentence)
        self.assertEqual(ans, "Dirty sentence that needs cleaning")
        
        
    """
    tests sentiment analysis on server.
    """
    def test_sentiment(self):
        sent_scorer = Server.DataAnalysis()
        obj = {'length': 80, 'method': 'reddit',
           'text': 'I m A Democrat And The Left s Russia Gaslighting Scares Me More Than Trump Does'}
        ans = sent_scorer.analyze_sentiment(obj)
        self.assertEqual(int(ans.sentiment), 0.25)

    
if __name__ == '__main__':
  unittest.main()
