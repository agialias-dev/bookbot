def get_book_text(book_path):
    with open(book_path) as f:
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
        if char.isalpha() and char in letter_dict:
            letter_dict[char] = letter_dict.get(char) + 1
    return letter_dict
    
def sort_dict_values(letter_count):
    values = sorted(letter_count.values(), reverse=True)
    return values

def sort_dict_keys(letter_count):
    keys = sorted(letter_count, key=lambda x: letter_count[x] , reverse=True)
    return keys