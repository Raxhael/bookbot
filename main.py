from stats import num_words
from stats import count_characters
from stats import sort_list
import os
import sys


def main():
    if len(sys.argv) == 1:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    filepath = sys.argv[1]
    print(filepath)
    file_contents = get_books_text(filepath)
    if file_contents is None:
        print(f"file {filepath} not found please try again")
        sys.exit(1)
    word_count = num_words(file_contents)
    letter_count = count_characters(file_contents)
    sorted_list = sort_list(letter_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for entry in sorted_list:
        char = entry["char"]
        count = entry["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")


def get_books_text(filepath):
    if not os.path.exists(filepath):
        print(f"Error: The File '{filepath}' does not exist")
        return None
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


main()
