import random 
import sys

# check if ch is a letter
def is_letter(ch):
    return len(ch) == 1 and  ch.isalpha()

# shuffle(s) returns a randomly shuffled copy of the string s
def shuffle(s):
    l = list(s)
    random.shuffle(l)
    return "".join(l)

def reorder_letters(s):
    i = 0
    while i < len(s) :
        break # modify this space
    print("")

args = sys.argv
if (len(args) != 2):
    print("Usage: python readable.py <filename>")
else:
    with open(args[1]) as f:
        for line in f.readlines():
            reorder_letters(line)