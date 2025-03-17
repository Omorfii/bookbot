def get_book_text(text):
    with open(text) as t:
        file_string = t.read()
    return file_string
   
def number_of_words(book):
    return len(book.split())

def main():
    book = get_book_text("books/frankenstein.txt")
    print(f"{number_of_words(book)} words found in the document") 

main()
