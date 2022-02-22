from unittest import TestCase
from src import get_anagrams
from src import generate_key


class AnagramsTestCase(TestCase):
    test_filename = "assets/words.txt"

    def test_get_anagrams(self):
        actual = get_anagrams(["Race", "Care", "Acre", "Bee", "Tree", "Mine"])
        expected = {
            generate_key("race"): ["Race", "Care", "Acre"],
            generate_key("bee"): ["Bee"],
            generate_key("tree"): ["Tree"],
            generate_key("mine"): ["Mine"],
        }
        self.assertEqual(actual, expected)
