import string

BOOK = 'books/frankenstein.txt'

def read_txt(file: str) -> str:
    with open(file, 'r') as f:
        txt = f.read()

        return txt

def count_words(txt:str) -> int:
    word_count = len(txt.split())

    return word_count

def create_dict() -> dict:
    d = dict.fromkeys(string.ascii_lowercase, 0)
    return d

def count_letters(letters: dict, txt: str) -> int:
    for c in txt.lower():
        if c in letters.keys():
            letters[c] += 1
        else:
            pass
    
    return letters

def print_letters(letters: dict):
    for c in letters.keys():
        print(f'Number of time the character {c} appears: {letters[c]}')

def main():
    txt = read_txt(BOOK)
    print(f'--- Begin report of {BOOK} ---\n')
    print(f'Number of words found in document: {count_words(txt)}\n')
    print_letters(count_letters(create_dict(), txt))

main()