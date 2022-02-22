from unittest import TestCase
from src import get_anagrams


class AnagramsTestCase(TestCase):
    test_filename = "assets/words.txt"

    def test_get_anagrams(self):
        actual = get_anagrams(self.test_filename)
        expected = {
            str({'r', 'a', 'c', 'e'}): ["Race", "care", "acre"],
            str({'b', 'e', 'e'}): ["bee"],
            str({'t', 'r', 'e'}): ["tree"],
            str({'m', 'i', 'n', 'e'}): ["mine"],
        }
        self.assertEqual(actual, expected)
