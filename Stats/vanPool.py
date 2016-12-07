import random
import numpy as np
import matplotlib.pyplot as plt

#initialize variables
sample_size = 9
num_sims = 100000
num_items = 3

countList = []
count7 = 0

#run simulation
for i in range(num_sims):
    count = 0
    for i in range(sample_size):
        r = random.randint(0,100)
        if r < 75:
            count +=1
    countList.append(count)
    if count > 7:
        count7 +=1


print "The mean percentage of people that show up is ", np.mean(countList)
print "with a standard deviation of ", np.std(countList)
print " "
print "The percentage of time that more than 7 people show up is ", count7/float(num_sims) * 100, "%"


# histogram of electoral votes from simulations
plt.figure(0)
plt.hist(countList)
plt.xlabel("Number of People")
plt.show()
