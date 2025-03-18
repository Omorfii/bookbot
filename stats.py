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
        
def sort_on(dict):
    return dict["count"]

def sorted_dictionaries(letter):
    sorted_letter = []
    for char, count in letter.items():
        char_info = {"char": char, "count": count}
        sorted_letter.append(char_info)
    sorted_letter.sort(reverse=True, key=sort_on)
    return sorted_letter

