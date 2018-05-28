from Server import Server
import pytest

"""
tests sentiment analysis on server.
"""
def test_sentiment():
    sent_scorer = Server.DataAnalysis()
    obj = {'length': 80, 'method': 'reddit',
           'text': 'I m A Democrat And The Left s Russia Gaslighting Scares Me More Than Trump Does'}
    ans = sent_scorer.analyze_sentiment(obj)
    assert int(ans.sentiment) == 0.25


"""
tests cleaning text on server.
"""
def test_twitter():
    sent_scorer = Server.DataAnalysis()
    sentence = "[Dirty-] sentence that (/needs/) {cleaning}"
    ans = sent_scorer.clean(sentence)
    assert ans == "Dirty sentence that needs cleaning"

