from pathlib import Path
from os import path
import argparse


def print_anagrams(words: dict):
    for key, value in words.items():
        if len(value) > 1:
            for el in value:
                print(el, end=" ")
            print()


def set_default_filename():
    ROOT_DIR = Path(__file__).parent.parent
    filename = "words.txt"
    assets_folder = "assets"
    file_path = path.join(ROOT_DIR, assets_folder, filename)
    return file_path


def get_command_line():
    """"""
    parser = argparse.ArgumentParser(
        description="Anagram finder. You can either run python main.py command and default file will be"
                    " set, or write an absolute path to the text file, you would like to parse. Pay attention that"
                    "all words have to be split by the line separator")
    parser.add_argument('-f', help='Absolute path to the file', type=str, action="store", required=False)

    return parser.parse_args()
