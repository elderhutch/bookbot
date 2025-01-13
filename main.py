def main():
    books_path = "books/frankenstein.txt"
    text = book(books_path)
    total_words = word_count(text)
    character_totals = character_count(text)
    print(total_words)
    print(character_totals)
    stat_report(character_totals)

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

def sort_list(dict):
    return dict[""]

# In retrospect, this actually just filters out non alphabet characters.  It doesn't properly create a sorted list as I'm looping over two different lists.
def stat_report(character_totals):
    sorted_dict = {}
    for letter in character_totals:
        if letter.isalpha():
            sorted_dict[letter] = character_totals[letter]
    sorted_keys_by_value = sorted(sorted_dict.keys(), reverse=reversed, key=lambda k: sorted_dict[k])
    
    for key in sorted_keys_by_value: print(f"Key: '{key}', Value: {sorted_dict[key]}")
    
        


main()


