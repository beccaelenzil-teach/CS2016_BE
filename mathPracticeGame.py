# initial program
'''
import random

factor1 = random.randint(2,10)
factor2 = random.randint(2,10)

correctAnswer = factor1*factor2
userAnswer = raw_input("Please enter the product of "+str(factor1)+" and "+str(factor2)+" : ")
userAnswer = int(userAnswer)
if userAnswer == correctAnswer:
    print "Correct!"
else:
    print "Incorrect!"

# with try again

import random

factor1 = random.randint(2,10)
factor2 = random.randint(2,10)

correctAnswer = factor1*factor2
#userAnswer = raw_input("Please enter the product of "+str(factor1)+" and "+str(factor2)+" : ")
#userAnswer = int(userAnswer)
userAnswer = 1
while userAnswer != correctAnswer:
    userAnswer = raw_input("Please enter the product of "+str(factor1)+" and "+str(factor2)+" : ")
    userAnswer = int(userAnswer)

    if userAnswer == correctAnswer:
        print "Correct!"
    else:
        print "Incorrect!"


'''
# with try again and play 5 times

import random

def play():
    for i in range(5):

        factor1 = random.randint(2,10)
        factor2 = random.randint(2,10)

        correctAnswer = factor1*factor2
        #userAnswer = raw_input("Please enter the product of "+str(factor1)+" and "+str(factor2)+" : ")
        #userAnswer = int(userAnswer)
        userAnswer = 1
        while userAnswer != correctAnswer:
            userAnswer = raw_input("Please enter the product of "+str(factor1)+" and "+str(factor2)+" : ")
            userAnswer = int(userAnswer)

            if userAnswer == correctAnswer:
                print "Correct!"
            else:
                print "Incorrect!"



# Gamify
def instructions():
    print "Hello! I am a computer!"
    name = raw_input("What is your name?")
    print "Welcome, "+name + "!"
    print "Let's practice multiplication"
    print "I'll give you two factors, and you enter their product"


def main():
    instructions()
    play()

main()
