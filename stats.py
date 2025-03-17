def number_of_words(book):
    return len(book.split())

def number_of_letters(book):
    letter = {}
    lowercases = book.lower()
    for lowercase in lowercases:
        if lowercase in letter:
            letter[lowercase] += 1

        else:
            letter[lowercase] = 1

    
    return letter
        
