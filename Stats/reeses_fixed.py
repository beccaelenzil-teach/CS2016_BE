import random
import numpy as np
import matplotlib.pyplot as plt

#initialize variables
sample_size = 10
num_sims = 100000
num_items = 3

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
        if r < 10:
            Ocount +=1
        elif r < 50:
            Ycount +=1
        else:
            Bcount +=1
    OcountList.append(Ocount)
    YcountList.append(Ycount)
    BcountList.append(Bcount)


print "The mean percentage of orange reese's is", np.mean(OcountList)/sample_size*100, "%"
print "with a standard deviation of ", np.std(OcountList)/sample_size*100, "%"
print " "
print "The mean percentage of yellow reese's is", np.mean(YcountList)/sample_size*100, "%"
print "with a standard deviation of ", np.std(YcountList)/sample_size*100, "%"
print " "
print "The mean percentage of brown reese's is", np.mean(BcountList)/sample_size*100, "%"
print "with a standard deviation of ", np.std(BcountList)/sample_size*100, "%"



# histogram of electoral votes from simulations
plt.figure(0)
plt.hist(OcountList)
plt.title("Orange")
plt.xlabel("Number of Pieces")
plt.show()
'''
plt.figure(1)
plt.hist(YcountList)
plt.title("Yellow")
plt.xlabel("Number of Pieces")

plt.figure(2)
plt.hist(BcountList)
plt.title("Brown")
plt.xlabel("Number of Pieces")
'''







