import random

def guessMyNumber():
    """ guess my number game """
    hiddenNum = random.choice(range(100))
    numguesses = 1    # we just made one, above
    guess = raw_input("Guess a number between 1 and 100: ")
    guess = int(guess)
    while guess != hiddenNum:
        if guess > hiddenNum:
            guess = raw_input("Too high! Guess again: ")
            guess = int(guess)
        else:
            guess = raw_input("Too low! Guess again: ")
            guess = int(guess)
        numguesses += 1  # add one to our number of guesses

    print "That's right! The number is ", guess

guessMyNumber()


