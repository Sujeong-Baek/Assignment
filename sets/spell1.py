# spell1.py
# A simple spell checker

def read_words():
    s = open("words.txt", "r")
    words = set()
    for w in s.readlines():
        words.add(w.strip())
    s.close()
    return words


def spell():
    words = read_words()
    while True:
        w = input("Tell me a word> ").strip().lower()
        if w == "":
            return
        if w in words:
            print("'%s' is a word" % w)
        else:
            print("Error: '%s' is not a word" % w)


spell()
