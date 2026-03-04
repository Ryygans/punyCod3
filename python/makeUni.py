#!usr/bin/python

mapping = {
    "a": "а",
    "e": "е",
    "o": "о",
    "p": "р",
    "c": "с",
    "x": "х",
    "y": "у",
    "i": "і",
    "l": "ӏ"
}

def to_cyrillic(text):
    return "".join(mapping.get(c, c) for c in text)

word = input("enter your word to Unicode: ")
print("Result: ", to_cyrillic(word))
#You can add many character for a better result
