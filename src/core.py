from typing import List


def generate_key(word: str) -> str:
    # converts "aabbc" to 26-element english alphabet list
    # [2, 2, 1, 0, 0, ..., 0]
    word_tuple = [0] * 26
    shift_index = 97
    for c in word:
        ascii_index = ord(c)
        intern_index = ascii_index - shift_index
        word_tuple[intern_index] += 1
    return str(word_tuple)


def get_anagrams(words: List[str]) -> dict:
    words_map = {}
    for word in words:
        word_key = generate_key(word.lower())
        if words_map.get(word_key, None) is None:
            words_map[word_key] = [word]
        else:
            words_map[word_key].append(word)
    return words_map
