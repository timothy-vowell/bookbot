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