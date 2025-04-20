import os


def num_words(file_contents):
    words = file_contents.split()
    count = len(words)
    return count


def count_characters(file_contents):
    char_count = {}
    for char in file_contents:
        lower = char.lower()
        char_count[lower] = char_count.get(lower,0) + 1
    return char_count


def sort_on(dict):
    return dict["count"]


def sort_list(letter_count):
    chars_list = []
    for char,count in letter_count.items():
        chars_list.append({"char": char, "count": count})

    chars_list.sort(reverse=True, key=sort_on)

    return chars_list