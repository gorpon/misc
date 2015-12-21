import random


def input_validate(response):
    try:
        value = int(response)
    except ValueError:
        print("please provide an integer")
        return False
    if value >= 1 and value <= 10:
        return value
    else:
        return False

def provide_secret_num():
    # this time user provides a number between 1 and 10
    secret_num = False
    while secret_num == False:
        response = input("enter a value between 1 and 10: ")
        if input_validate(response):
            secret_num = input_validate(response) 
    return secret_num 

def get_highest_guess(guesses):
    highest = 0
    for num in guesses:
        if num > highest:
            highest = num
    if highest == 0:
        highest = 10
    return highest

def get_lowest_guess(guesses):
    lowest = 10
    for num in guesses:
        if num < lowest:
            lowest = num
    if lowest == 10:
        lowest = 1
    return lowest

def ai_range(guesses, proximity=0):
    # set default range
    # first guess default range
    if proximity == 0 and len(guesses) == 0:
        return range

    last_guess = guesses[-1]
    # last guess too high.
    if proximity == 1:
        range[1] = last_guess - 1
    # last guess too low.
    elif proximity == -1:
        range[0] = last_guess + 1
    else:
        print("proximity error in AI")
        sys.exit(1)
    min, max = range
    # print("min {}   max {}".format(min, max))
    return range
             
def ai_guesser(guesses, proximity = 0):
    # computer needs some logic to try to guess the number quickly
    min, max = ai_range(guesses, proximity)
    if min > max:
        min = max
    return round((max - min) / 2 + min)

def loop_and_guess(secret_num):
    guesses = []
    proximity = 0
    while True:
        # get a number guess from the player
        response = ai_guesser(guesses, proximity)
        print("computer guessed {}".format(response))
        if input_validate(response):
            guess = response
            guesses.append(guess)
        else:
            print("invalid guess.  something is wrong. aborting")
            sys.exit(1)
    
        if guess == secret_num:
            print("computer got it! your number was {}".format(secret_num))
            break
        elif secret_num > guess:
            proximity = -1
            print("computer guessed too low.  trying again")    
        elif secret_num < guess:
            proximity = 1
            print("computer guessed too high. trying again")
        else:
            print("how in the hell did you get here?")
            sys.exit(1)

while True:
    range = [ 2, 9 ]
    loop_and_guess(provide_secret_num())
    if input("Would you like to play again(Yes/No)?: ") == 'Yes':
        continue
    else:
        break
