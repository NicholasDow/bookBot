# with open('books/frankenstein.txt') as file:
#     text = file.read()
#     print(text)
from collections import Counter

def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    print(text)
    num_words = get_num_words(text)
    print(num_words)
    print(count_each(text))

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        # can just return it here wow
        return f.read()

def count_each(s):
    return Counter(list(s.lower()))

main()
