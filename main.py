def main():
    books_path = "books/frankenstein.txt"
    text = book(books_path)
    total_words = word_count(text)
    character_totals = character_count(text)
    print(total_words)
    print(character_totals)

def book(books_path):
    with open(books_path) as f:
        file_contents = f.read()
        return file_contents
    
def word_count(text):
    split = text.split()
    counter = 0
    for i in split:
        counter += 1
    return counter

def character_count(text):
    unique_dict = {}
    for char in text:
        lowercase = char.lower()
        if lowercase not in unique_dict:
            unique_dict[lowercase] = 1
        else:
            unique_dict[lowercase] += 1
    return unique_dict


main()
