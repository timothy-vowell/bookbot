def count_words(text):
    return len(text.split())

def count_characters(text):
    text = text.lower()
    dict = {}
    for char in text:
        if char in dict:
            dict[char] += 1
        else: dict[char] = 1
    return dict

def sort_on(dict):
    return dict["num"]

def sort_dict(dict):
    lst = list()
    for k in dict:
        lst.append({"char": k, "num": dict[k]})
    lst.sort(reverse=True, key=sort_on)
    return lst