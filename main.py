from stats import count_words, count_characters, sort_dict
import sys

def get_book_text(path):
    file_contents = ""
    #opens the file in the filepath
    with open(path) as f:
        #read() method reads the contents of a file into a string
        file_contents = f.read()
    return file_contents

def main():
    check_sys(sys.argv)
    path = sys.argv[1]
    text = get_book_text(path)
    num_of_words = count_words(text)
    character_count = count_characters(text)
    sorted_list = sort_dict(count_characters(text))
    print_report(num_of_words, sorted_list, path)
    

def print_report(num_of_words, sorted_list, path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("------------ Word Count ------------")
    print(f"Found {num_of_words} total words")
    print("------------ Character Count ------------")
    for d in sorted_list:
        if d["char"].isalpha() == True:
            print(f"{d['char']}: {d['num']}")

def check_sys(x):
    if len(x) < 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)


main()