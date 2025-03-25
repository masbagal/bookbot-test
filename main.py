import sys
from stats import get_word_count, get_char_count, print_stats

def get_book_text(path):
    content = ""
    with open(path) as f:
        content = f.read()
    return content

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        text = get_book_text(sys.argv[1])
        word_count = get_word_count(text)
        char_count = get_char_count(text)
        print_stats(sys.argv[1], word_count, char_count)


main()
