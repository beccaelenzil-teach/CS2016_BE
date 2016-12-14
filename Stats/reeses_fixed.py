import random
import numpy as np
import matplotlib.pyplot as plt

#initialize variables
sample_size = 25
num_sims = 1000

OcountList = []
YcountList = []
BcountList = []

#run simulation
for i in range(num_sims):
    Ocount = 0
    Ycount = 0
    Bcount = 0
    for i in range(sample_size):
        r = random.randint(0,100)
        if r < 45:
            Ocount +=1
        elif r < 66:
            Ycount +=1
        else:
            Bcount +=1
    OcountList.append(Ocount)
    YcountList.append(Ycount)
    BcountList.append(Bcount)

#print out summary statistics
print "The mean percentage of orange reese's is", np.mean(OcountList)/sample_size*100, "%"
print "with a standard deviation of ", np.std(OcountList)/sample_size*100, "%"
#or, if you get an axis error
print "The mean percentage of orange reese's is", sum(OcountList)/float(num_sims)/sample_size*100, "%"

# histogram of electoral votes from simulations
plt.figure(0)
plt.hist(OcountList)
plt.title("Orange")
plt.xlabel("Number of Pieces")
plt.show()








