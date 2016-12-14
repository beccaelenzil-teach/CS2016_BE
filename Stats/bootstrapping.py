import csv
import random
import numpy as np
import matplotlib.pyplot as plt

def loadData():
    times = []
    with open('heroin.csv', 'rb') as heroinData:
        reader = csv.reader(heroinData)
        #initialize row_num
        row_num = 0
        for row in reader:
            #don't collect the first row of data because this is text
            if row_num > 0:
                # we need data from columns 0, 2, 3, and 4
                for i in [0,1,2,3,4,5]:
                    if i == 3:
                        times.append(int(row[i]))
            row_num += 1

    return [times]

def bootstrap():
    [times] = loadData()

    num_samples =  len(times)
    num_sims = 1000

    samples = [[0]*num_samples]*num_sims
    medians = []

    for n in range(num_sims):
        for i in range (num_samples):
            r = random.randrange(num_samples)
            samples[n][i] = times[r]
        medians.append(np.median(samples[n]))

    return medians

medians = bootstrap()
print np.std(medians)

plt.figure(0)
plt.hist(medians)
plt.show()



