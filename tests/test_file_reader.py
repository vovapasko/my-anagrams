from pathlib import Path
from unittest import TestCase
from os import path
from core.file_reader import file_reader


class TestTxtFileReader(TestCase):
    ROOT_DIR = Path(__file__).parent.parent
    existing_file_path = path.join(ROOT_DIR, "assets", "words.txt")
    not_existing_file_path = "file_not_exist.txt"

    def test_read_successfully(self):
        actual = file_reader.read(self.existing_file_path)
        expected = ["Tree", "Race", "Bee", "Care", "Acre", "Mine"]
        self.assertIsNotNone(actual)
        self.assertEqual(actual, expected)

    def test_read_not_existing_file_throws_exception(self):
        self.assertRaises(FileNotFoundError, file_reader.read, self.not_existing_file_path)
