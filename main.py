def main():
    books_path = "books/frankenstein.txt"
    text = book(books_path)
    total_words = word_count(text)
    print(total_words)

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

main()
