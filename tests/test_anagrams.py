from unittest import TestCase
from src import get_anagrams
from src import generate_key


class AnagramsTestCase(TestCase):
    def test_get_anagrams_correct_list(self):
        actual = get_anagrams(["Race", "Care", "Acre", "Bee", "Tree", "Mine"])
        expected = {
            generate_key("race"): ["Race", "Care", "Acre"],
            generate_key("bee"): ["Bee"],
            generate_key("tree"): ["Tree"],
            generate_key("mine"): ["Mine"],
        }
        self.assertEqual(actual, expected)

    def test_get_anagrams_empty_list(self):
        actual = get_anagrams([])
        expected = {}
        self.assertEqual(actual, expected)

    def test_get_anagrams_list_with_no_anagrams(self):
        actual = get_anagrams(["word", "No"])
        expected = {
            generate_key("word"): ["word"],
            generate_key("no"): ["No"]
        }
        self.assertEqual(actual, expected)
