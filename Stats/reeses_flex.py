import random
import matplotlib.pyplot as plt

#initialize variables
sample_size = 10
num_sims = 10000
num_items = 3

countList = []
for i in range(num_items):
    countList.append([])

#run simulations
for i in range(num_sims):
    count = [0,0,0]
    for i in range(sample_size):
        r = random.randint(0,100)
        if r < 10:
            count[0] += 1
        elif r < 50:
            count[1] += 1
        else:
            count[2] += 1

    for i in range(num_items):
        countList[i].append(count[i])

# average percentage of each type
for i in range(num_items):
    print(sum(countList[i])/float(len(countList[i]))/sample_size)

# histogram of electoral votes from simulations
for i in range(num_items):
    plt.figure(i)
    plt.hist(countList[i],bins = sample_size)
    plt.title("Item Type " + str(i))
    plt.xlabel("Number of Pieces")
    plt.show()
