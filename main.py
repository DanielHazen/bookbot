def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    printReport(sort_on(count_letters(text)), word_count)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(book_text):
    words = book_text.split()
    get_count = len(words)
    return get_count


def count_letters(book_text):
    my_string = book_text
    lowered_string = my_string.lower()
    letters = []
    letter_dict = {}
    for character in lowered_string:
        # print(f"character: {character} ")
        if character.isalpha():
            letters.append(character)
            if character in letter_dict:
                count = 1
                count += letter_dict[character]
                letter_dict.update({character: count})
            else:
                letter_dict.update({character: 1})

    return letter_dict


def sort_on(letter_dict):
    sorted_list = []
    for letter in letter_dict:
        sorted_list.append({"name": f"{letter}", "num": letter_dict[letter]})
    sorted_list.sort(reverse=True, key=sortKey)
    return sorted_list


def sortKey(dict_list):
    return dict_list["num"]


def printReport(sorted_list, word_count):
    print("Being Report of books/frankenstein.txt")
    print(f"{word_count} words found in this document")
    for letter in sorted_list:
        print(f"The '{letter["name"]}' character was found {letter["num"]} times")


if __name__ == "__main__":
    main()
