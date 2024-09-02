def main():
    path = "books/frankenstein.txt"
    text = get_text(path)
    #print(text)
    word_count = count_words(text)
    character_count = count_characters(text)
    generate_report(path, word_count, character_count)


def get_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def count_words(book):
    word_list = book.split()
    word_count = len(word_list) 
    return word_count

def count_characters(book):
    character_dict = {}
    lower_case_book = book.lower()
    for b in lower_case_book:
        if b.isalpha() == True:
            if b not in character_dict:
                character_dict[b] = 1
            else:
                character_dict[b] += 1
    return character_dict

def generate_report(p, w, c):
    print(f"--- Begin report of {p} ---")
    print(f"{w} words found in the document")
    print("")
    list_of_dict = []
    for char in c:
        list_of_dict.append({"name": char, "num": c[char]})
    def sort_dict(dict):
        return dict["num"]
    list_of_dict.sort(reverse=True, key=sort_dict)
    for d in list_of_dict:
        print(f"The '{d['name']}' character was found {d['num']} times")


main()