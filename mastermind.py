#
# Mastermind game
# 

import random

MAX_NUM_GUESSES = 10
SECRET_LENGTH = 4

# A-F까지에서 (겹치지 않도록) 랜덤하게 4개 고르기
def create_secret(): #ABAB
    c = "ABCDEF"
    secret = ""
    for _ in range(SECRET_LENGTH):
        index = random.randrange(len(c))
        letter = c[index]
        secret = secret + letter
    return secret

# guess가 규칙에 맞는지 확인
# 1. 길이가 4인지 확인. 틀리면 "Your guess must have four letters"
# 2. 글자에 A - F 외의 글자가 있는지 확인. 틀리면 "You can only use letters A, B, C, D, E, and F."
# (3. 중복된 글자가 있는지 확인. 틀리면 "All letters must be distinct.")
# Returns (ok: Boolean, message : String) 
def check_guess(guess):
    if len(guess) != SECRET_LENGTH:
        return False, "Your guess must have " + str(SECRET_LENGTH) + " letters"
    for i, letter in enumerate(guess): # BBCD, ABCD
        if letter not in ['A','B','C','D','E','F']:
            return False, "You can only use letters A, B, C, D, E, and F."
        # for j in range(i):
        #     if letter == guess[j]:
        #         return False, "All letters must be distinct."
    return True, ""

# terminal에서 user input으로 guess 받아서 틀린 입력이면 출력하기
def get_guess():
    while True:
        guess = input("Enter your guess> ")
        guess = guess.strip().upper().replace(" ", "")
        ok, msg = check_guess(guess)
        if ok:
            return guess
        print(msg)


# return (pos, let) pos 는 위치까지 일치하는 글자, let은 secret 포함되지만 위치가 틀린 글자
def evaluate_guess(secret, guess): 
    pos=let=0
    # pos, let = 0,0(숫자가 다를경우 , 로 구분)
    for i in range(SECRET_LENGTH):
        cguess=guess.count(guess[i])
        csecret=secret.count(guess[i])
        if guess[i]==secret[i]:
            pos+=1
            let-=1
    
        elif cguess>csecret:
            let+=csecret
            
        elif cguess<=csecret:
            let+=cguess      

    return pos, let


# 입력한 guess 에 대한 history를 출력하는 함수
def show_history(h, current, secret):
  for count in range(current):
    guess = h[count]
    pos, let = evaluate_guess(secret, guess)
    print("{0:2}: {1} : {2} positions, {3} letters".format(count+1, guess, pos, let))

# main game  
def main():    
    secret = create_secret()
    history = []
    current = 0
    print("Welcome to Mastermind!")
    print("I have created a secret combination:")
    print(str(SECRET_LENGTH)+" distinct letters from A - F.")
    print("You have {0} guesses to find it.".format(MAX_NUM_GUESSES))
    while True:
        show_history(history, current, secret)
        if current == MAX_NUM_GUESSES:
            print("My secret was {0}, you failed to find it in {1} guesses!".format(secret, current))
            return
        guess = get_guess()
        history.append(guess)
        current += 1
        pos, _ = evaluate_guess(secret, guess)
        if pos == SECRET_LENGTH:
            print("My secret was {0}, you guessed correctly in {1} guesses!".format(secret, current))
            return

main()
