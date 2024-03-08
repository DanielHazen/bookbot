def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)

    print(word_count)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(book_text):
    words = book_text.split()
    get_count = len(words)
    return get_count


if __name__ == "__main__":
    main()
