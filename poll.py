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
'''

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


