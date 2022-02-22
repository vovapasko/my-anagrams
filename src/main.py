from os import path
from src.core import get_anagrams
from src.file_reader import file_reader


def print_anagrams(words: dict):
    for key, value in words.items():
        if len(value) > 1:
            for el in value:
                print(el, end=" ")
            print()


def main():
    file_path = set_default_filename()
    words = file_reader.read(file_path)
    words_dict = get_anagrams(words)
    print_anagrams(words_dict)


def set_default_filename():
    filename = "words.txt"
    assets_folder = "assets"
    file_path = path.join(path.pardir, assets_folder, filename)
    return file_path


if __name__ == '__main__':
    main()
