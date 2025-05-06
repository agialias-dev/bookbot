from stats import get_book_text, get_word_count, get_letter_count, sort_dict_values, sort_dict_keys
import sys

def main():
#    raw = "books/" + input("Enter the name of the book:") + ".txt"
#    book_path = raw.lower()
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    letter_count = get_letter_count(text)
    sorted_letter_values = sort_dict_values(letter_count)
    sorted_letter_keys = sort_dict_keys(letter_count)
    print(f"""--- Beginning Report of {book_path} ---
    This document contains {word_count} words.
    """)
    for i in range(26):
        print(f"    The letter '{sorted_letter_keys[i]}' appears {sorted_letter_values[i]} times.")
    print("""
--- End of Report ---""")

try:
    main()
except FileNotFoundError:
    print("This book couldn't be found in the /books directory")
except Exception as e:
    print(e)