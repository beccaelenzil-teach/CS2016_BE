# python 2
#
# Homework 4
#
# Name: Becca Elenzil
#

from random import *
import matplotlib.pyplot



def rs():
    """ rs chooses a random step and returns it
        note that a call to rs() requires parentheses
        inputs: none at all!
    """
    return choice([-1,1])


def rwpos(start,nsteps):
    """
    :param start: starting position of sleepwalker
    :param nsteps: number of random steps
    :return:
    """
    current_pos = start
    for i in range(nsteps):
        print 'current pos is', current_pos
        current_pos += rs()
    print 'current pos is', current_pos
    #return current_pos

#rwpos(40,10)

def rwposPlain(start,nsteps):
    """
    :param start: starting position of sleepwalker
    :param nsteps: number of random steps
    :return:
    """
    current_pos = start
    for i in range(nsteps):
        #print 'current pos is', current_pos
        current_pos += rs()
    #print 'current pos is', current_pos
    return current_pos

#rwposPlain(40,100)

def rwsteps( start, low, hi ):
    """
    :param start: starting position for sleep walker
    :param low: smallest integer sleepwalker is allowed to wander
    :param hi: largest position sleepwalker is allowed to wander
    :return: nsteps until reaching bound
    """
    nsteps = 0 # initialize number of steps to 0
    current_pos = start # initialize current position to start position
    while current_pos > low and current_pos < hi:
        #print str(current_pos)+(4-len(str(current_pos)))*' '+'|' + ' '*(current_pos-1-low) + 'S' + ' '*(hi-current_pos-1) + '|'
        print  ' '*(current_pos-1-low) + 'S' + ' '*(hi-current_pos-1)

        #time.sleep(0.5)

        current_pos += rs()
        nsteps += 1
    return nsteps

#rwsteps(5, 0, 10 )

def ave_signed_displacement(N,nsteps):
    """
    :param N: number of trials
    :return: the average signed displacement
    """
    #LC = [rwposPlain(0,100) for x in range(N)]
    LC = []
    for x in range(N):
        end_pos = rwposPlain(0,nsteps)
        LC.append(end_pos)

    return [LC, float(sum(LC))/N]

[list, ave] = ave_signed_displacement(1000,100)

#print 'The average signed displacement for 1000 trials with 1000 steps is '\
#    ,ave_signed_displacement(1000,1000)

matplotlib.pyplot.figure(0)
matplotlib.pyplot.hist(list)




def ave_squared_displacement(N,nsteps):
    """
    :param N: number of trials
    :return: the average squared displacement
    """
    #LC = [rwposPlain(0,nsteps) for x in range(N)]
    LC = []
    for x in range(N):
        end_pos = rwposPlain(0,nsteps)
        LC.append(end_pos)

    square_list = []
    for i in range(N):
        square_list.append(LC[i]**2)
    return float(sum(square_list))/N

#print 'The average squared displacement for 1000 trials with 1000 steps is ',ave_squared_displacement(1000,1000)
