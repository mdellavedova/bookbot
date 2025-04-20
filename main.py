from stats import (
    count_words,
    count_chars,
    create_char_list_of_dicts,
    sort_list_of_dicts,
    print_report,
)
import sys


def main():
    # book_path = ""
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]

    text = get_book_text(book_path)
    word_count = count_words(text)
    characther_count = count_chars(text)
    character_list_of_dicts = create_char_list_of_dicts(characther_count)
    sort_list_of_dicts(character_list_of_dicts)
    print_report(book_path, word_count, character_list_of_dicts)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
