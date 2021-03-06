from __future__ import unicode_literals
from django.test import TestCase
from common.utils.metrics import cosine_similarity
from common.utils.nlp import join_words, is_contextfree, sentence_to_tree
from common.utils.wiki import uri_to_name


class WikiUtilsTestCase(TestCase):

    def test_uri_to_name(self):
        """
        URIs are correctly transformed to names.
        """
        for uri, expected_name in [
                ('http://en.wikipedia.org/wiki/USA', 'USA'),
                ('http://cs.wikipedia.org/wiki/Pan_Tau', 'Pan Tau'),
                ('http://en.wikipedia.org/wiki/A', 'A')]:
            self.assertEqual(uri_to_name(uri), expected_name)


class NlpUtilsTestCase(TestCase):

    def test_join_words(self):
        for words, sentence in [
            (['Hello', ',', 'World', '!'], 'Hello, World!'),
            (['Sentence', '.', 'Sentence', '.'], 'Sentence. Sentence.'),
            (['Out', '(', 'in', ')', 'out'], 'Out (in) out'),
            (['18', 'things', 'vs', '.', '17', 'th'], '18 things vs. 17th'),
        ]:
            self.assertEqual(join_words(words), sentence)

    def test_contextfree(self):
        self.assertEqual(is_contextfree(sentence_to_tree('Abraham Lincoln was the 16th president of USA.')), True)
        self.assertEqual(is_contextfree(sentence_to_tree('Too short.')), False)
        self.assertEqual(is_contextfree(sentence_to_tree('Question question question question question?')), False)
        self.assertEqual(is_contextfree(sentence_to_tree('His primary goal was to reunite the nation.')), False)
        self.assertEqual(is_contextfree(sentence_to_tree('He preserved the Union and abolished slavery.')), False)


class MetricsUtilsTestCase(TestCase):

    def test_cosine_similarity(self):
        doc1 = {'a': 4, 'b': 3}
        doc2 = {'a': 4}
        self.assertAlmostEqual(cosine_similarity(doc1, doc2), 0.8)

        doc1 = {'a': 2, 'b': 1, 'c': 3}
        doc2 = {'b': 1, 'c': 3, 'd': 5}
        self.assertAlmostEqual(cosine_similarity(doc1, doc2), 0.45175395145262565)
