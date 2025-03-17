from stats import number_of_words
from stats import number_of_letters

def get_book_text(text):
    with open(text) as t:
        file_string = t.read()
    return file_string
   
def main():
    book = get_book_text("books/frankenstein.txt")
    # print(f"{number_of_words(book)} words found in the document") 
    print(number_of_letters(book))

main()
