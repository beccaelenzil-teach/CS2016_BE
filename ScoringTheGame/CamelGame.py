import random

print "Welcome to Camel!"
print " "
print "You have stolen a camel to make your way across the great Mobi desert.\
The natives want their camel back and are chasing you down! Survive your\
desert trek and outrun the natives."


done = False
miles_traveled = 0
thirst = 0
tired = 0
natives_traveled = -20
drinks = 5

while not done:
    print " "
    print "A. Drink from your canteen."
    print "B. Ahead moderate speed."
    print "C. Ahead full speed."
    print "D. Stop and rest."
    print "E. Status check."
    print "Q. Quit."
    print " "

    choice = raw_input("Your choice? ")
    print " "

    choice = choice.upper()

    if choice == 'Q':
        done = True
    elif choice == 'E':
        print "Miles traveled: ", miles_traveled
        print "Drinks in canteen: ", drinks
        print "The natives are ", miles_traveled - natives_traveled, " behind you."
    elif choice == 'D':
        tired = 0
        print "The camel is happy"
        natives_traveled += random.randint(7,15)
    elif choice == 'C':
        m = random.randint(10,21)
        print "You traveled ",m, " miles."
        miles_traveled += m
        thirst += 1
        tired += random.randint(1,4)
        natives_traveled += random.randint(7,15)
    elif choice == 'B':
        m = random.randint(5,13)
        print "You traveled ",m, " miles."
        miles_traveled += m
        thirst += 1
        tired += 1
        natives_traveled += random.randint(7,15)
    elif choice == 'A':
        if drinks > 0:
            drinks -= 1
            thirst = 0
        else:
            print "You don't have any water left."

    r = random.randint(0,20)
    if r == 0:
        print "You found an Oasis!"
        drinks = 5
        thirst = 0
        tired = 0


    if thirst > 4:
        print "You are thirsty!"
    elif thirst > 6:
        print "You died of thirst!"
        done = True

    if tired > 5 and done == False:
        print "Your camel is getting tired."
    elif tired > 8 and done == False:
        print "Your camel is dead."
        done = True

    if miles_traveled - natives_traveled <= 0 and done == False:
        print "The natives caught up."
        done = True
    elif miles_traveled - natives_traveled <= 15 and done == False:
        print "The natives are getting close."

    if miles_traveled >= 200 and done == False:
        print "You won!"
        done = True








