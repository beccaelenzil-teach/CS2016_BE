import random as rand
import numpy as np
'''
#simulations
winner = [0,0]
states = ['nj', 'fl', 'mi']
elec_votes = [14, 29, 16]

for j in range(len(states)):
for i in range(10000):
    fl = rand.randint(1,1000)
    if fl < 563:
        winner[0]+=1
    else:
        winner[1]+=1

    winner*

print(winner)


#weighted average

weights = [1.76, 1.49, 1.42, 1.22, 1.13, 1.07, .96, .91, .84, .81]
c_perc = [.41, .44, .44, .43, .43, .46, .46, .42, .41, .44]

weighted_average = 0
for i in range(len(weights)):
    weighted_average += weights[i]*c_perc[i]

weighted_average /= (sum(weights))
print(weighted_average)


a = []
b = []
for j in range(10000):
    for i in range(6):
        a.append(rand.randint(0,1));
    b.append(sum(a))
    a = []
print b
hist = np.histogram(b,[0,1,2,3,4,5,6,7])
print hist
'''

import random as rand

num_states = 3
elec_votes = [14, 14, 14]
c_perc = [.6, .6, .6]
num_sims = 100
votes = [[0]*num_sims,[0]*num_sims]
winner = [0]*num_sims

for i in range(num_sims):
    for state in range(num_states):

        x = rand.randint(1,1000)
        if x < c_perc[state]*1000:
            votes[0][i]+=elec_votes[state]
        else:
            votes[1][i]+=elec_votes[state]

    if votes[1][i] > votes[0][i]:
        winner[i] = 1




print "clinton: ",  votes[0]
#print "trump  : ",  votes[1]

#print "winner: ", winner
print "percent trump: ", sum(winner)/float(num_sims)

#histogram with number of electoral votes on x-axis






