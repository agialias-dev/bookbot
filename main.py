def main():
    book_path = "books/" + input("Enter the name of the book:") + ".txt"
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


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
        words = text.split()
        return len(words)

def get_letter_count(text):
    letter_dict = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,
                   'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,
                   'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,
                   'v':0,'w':0,'x':0,'y':0,'z':0}
    lower_case = text.lower()
    for char in lower_case:
        if char.isalpha():
            letter_dict[char] = letter_dict.get(char) + 1
    return letter_dict
    
def sort_dict_values(letter_count):
    values = sorted(letter_count.values(), reverse=True)
    return values

def sort_dict_keys(letter_count):
    keys = sorted(letter_count, key=lambda x: letter_count[x] , reverse=True)
    return keys

main()