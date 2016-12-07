import random
import matplotlib.pyplot as plt

sample_size = 10
num_sims = 10000
num_items = 3


countList = []
for i in range(num_items):
    countList.append([])

OcountList = []
YcountList = []
BcountList = []
for i in range(num_sims):
    count = [0,0,0]
    Ocount = 0
    Ycount = 0
    Bcount = 0
    for i in range(sample_size):
        r = random.randint(0,100)
        if r < 10:
            Ocount +=1
            count[0] += 1
        elif r < 50:
            Ycount +=1
            count[1] += 1
        else:
            Bcount +=1
            count[2] += 1
    OcountList.append(Ocount)
    YcountList.append(Ycount)
    BcountList.append(Bcount)

    #for an arbitrary item types
    for i in range(num_items):
        countList[i].append(count[i])

for i in range(num_items):
    print sum(countList[i])/float(len(countList[i]))/sample_size

print sum(OcountList)/float(len(OcountList))/sample_size
print sum(YcountList)/float(len(YcountList))/sample_size
print sum(BcountList)/float(len(BcountList))/sample_size


# histogram of electoral votes from simulations

for i in range(num_items):
    plt.figure(i)
    plt.hist(countList[i])
    plt.title("Item Type " + str(i))
    plt.xlabel("Number of Pieces")

'''
plt.figure(0)
plt.hist(OcountList)
plt.title("Orange")
plt.xlabel("Number of Pieces")

plt.figure(1)
plt.hist(YcountList)
plt.title("Yellow")
plt.xlabel("Number of Pieces")


plt.figure(2)
plt.hist(BcountList)
plt.title("Brown")
plt.xlabel("Number of Pieces")

plt.show()
'''




