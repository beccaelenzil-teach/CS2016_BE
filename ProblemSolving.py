# python 2
#
# Homework 5, Problem 1
#
# Name: Becca Elenzil
#

import random
import time

def rs():
    """ rs chooses a random step and returns it
        note that a call to rs() requires parentheses
        inputs: none at all!
    """
    return random.choice([-1,1])

def rwpos( start, nsteps ):
    '''
    an integer start, representing the starting position of our sleepwalker, and
    a nonnegative integer nsteps, representing the number of random steps to take from this starting position.
    :param start:
    :param nsteps:
    :return:random walkers position
    '''
    print "current position is ", start
    for i in range(nsteps):
        start += rs()
        print "current position is ", start

    return start

def rwposPlain( start, nsteps, num_sims):
    '''
    an integer start, representing the starting position of our sleepwalker, and
    a nonnegative integer nsteps, representing the number of random steps to take from this starting position.
    :param start:
    :param nsteps:
    :return:random walkers position
    '''

    signed_displacement = []
    sq_displacement = []

    for i in range(num_sims):
        position = start


        #print "current position is ", start
        for i in range(nsteps):
            position += rs()

        signed_displacement.append(start - position)
        sq_displacement.append((start - position)**2)

    return [sum(signed_displacement)/float(num_sims), sum(sq_displacement)/float(num_sims)]

print rwposPlain( 40, 4, 1000)

def rwsteps( start, low, hi ):
    """
    an integer start, representing the starting position of our sleepwalker,
    an integer low, which will always be nonnegative, representing the smallest value our sleepwalker will be allowed to wander to, and
    an integer hi, representing the highest value our sleepwalker will be allowed to wander to.
    :param start:
    :param low:
    :param hi:
    :return:
    """
    spaces_total = hi - low - 1
    nsteps = 0
    while start > low and start < hi:
        spaces_before = start - low
        spaces_after = spaces_total - spaces_before
        print "|" +" "*spaces_before + "S" +" "*spaces_after+ "|"
        time.sleep(0.1)   #sleep for 0.1 seconds
        start += rs()
        nsteps += 1

    return nsteps



#print rwsteps( 10, 7, 20 )
