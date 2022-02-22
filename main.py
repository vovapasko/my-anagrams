from core.anagrams import get_anagrams
from core.file_reader import file_reader
from core.helpers import set_default_filename, print_anagrams
from core.helpers import get_command_line


def main():
    command_line_args = get_command_line()
    if command_line_args.f:
        file_path = command_line_args.f
    else:
        file_path = set_default_filename()
    words = file_reader.read(file_path)
    words_dict = get_anagrams(words)
    print_anagrams(words_dict)


if __name__ == '__main__':
    main()
