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

def reorder_letters(s): # this language. course we will use the python programming  -> nI siht cureso ~~
                        # nI siht euaglang.
    i = 0 # 1    
    while i < len(s) : # i >= len(s)
         word = "" # a
         while i < len(s): # 0 < 2            
            if not is_letter(s[i]): 
                shuffle_word = shuffle(s[len(word):i])              
                word += shuffle_word+s[i]         
            i += 1            
         print(word)
        
    print("") 


args = sys.argv
if (len(args) != 2):
    print("Usage: python readable.py <filename>")
else:
    with open(args[1], 'rt', encoding='UTF8') as f:
        for line in f.readlines():
            reorder_letters(line)

