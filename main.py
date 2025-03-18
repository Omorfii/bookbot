from stats import number_of_words
from stats import number_of_letters
from stats import sorted_dictionaries

def get_book_text(text):
    with open(text) as t:
        file_string = t.read()
    return file_string

def main():
    import sys
    number_arguments = len(sys.argv)
    if number_arguments == 2:
        book = get_book_text(sys.argv[1])
        word_count = number_of_words(book)
        letter = number_of_letters(book)
        sorted_letter = sorted_dictionaries(letter)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        for item in sorted_letter:
            char = item["char"]
            count = item["count"]        
            if char.isalpha():
                print(f"{char}: {count}")
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()
