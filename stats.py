def count_words(text):
    split_text = text.split()
    word_count = len(split_text)
    return word_count


def count_chars(text):
    lowercase_text = text.lower()
    char_count = {}
    for char in lowercase_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


def create_char_list_of_dicts(characther_count):
    character_list_of_dicts = []
    for character in characther_count:
        if character.isalpha():
            character_list_of_dicts.append(
                {"char": character, "count": characther_count[character]}
            )
    return character_list_of_dicts


def sort_on(dict):
    return dict["count"]


def sort_list_of_dicts(character_list_of_dicts):
    character_list_of_dicts.sort(reverse=True, key=sort_on)
    return character_list_of_dicts


def print_report(book_path, word_count, character_list_of_dicts):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for character in range(len(character_list_of_dicts) - 1):
        print(
            f"{character_list_of_dicts[character]['char']}: {character_list_of_dicts[character]['count']}"
        )
    print("============= END ===============")
