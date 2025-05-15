from stats import count_words, count_characters

def get_book_text(path):
    file_contents = ""
#opens the file in the filepath
    with open(path) as f:
#read() method reads the contents of a file into a string
        file_contents = f.read()
    return file_contents

def main():
    text = get_book_text("books/frankenstein.txt")
    print(f"{count_words(text)} words found in the document")
    print(count_characters(text))
    
main()