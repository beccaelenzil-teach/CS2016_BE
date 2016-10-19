import random as rand
import matplotlib.pyplot as plt
import csv

def electionSim():

    #load data
    [state_name, elec_votes, dem_perc, rep_perc] = loadData()

    num_states = len(elec_votes)
    num_sims = 1000

    # initialize electoral votes and winner each simulation
    # votes[0] = dem, votes[1] = rep
    votes = [[0]*num_sims,[0]*num_sims]
    winner = [0]*num_sims

    # simulate num_sim times
    for i in range(num_sims):

        # compare random number with probability for each state and return winner
        for state in range(num_states):

            x = rand.randint(1,1000)
            if x < dem_perc[state]*10:
                votes[0][i]+=elec_votes[state]
            elif x < (dem_perc[state]+rep_perc[state])*10:
                votes[1][i]+=elec_votes[state]

        #compare number of votes and assign winner
        if votes[1][i] > votes[0][i]:
            winner[i] = 1

    #print percentage of time dems and reps win
    print "percent dem: ", 1 - sum(winner)/float(num_sims)
    print "percent rep: ", sum(winner)/float(num_sims)

    #return the number of votes each simulation
    return votes


def loadData():
    state_name = []
    elec_votes = []
    dem_perc = []
    rep_perc = []

    with open('electorate2016.csv', 'rb') as pollingInfo:
        reader = csv.reader(pollingInfo)
        #initialize row_num
        row_num = 0
        for row in reader:
            #don't collect the first row of data because this is text
            if row_num > 0:
                # we need data from columns 0, 2, 3, and 4
                for i in [0,2,3,4]:
                    if i == 0:
                        state_name.append(row[i])
                    elif i == 2:
                        elec_votes.append(int(row[i]))
                    elif i == 3:
                        dem_perc.append(float(row[i]))
                    elif i == 4:
                        rep_perc.append(float(row[i]))
            row_num += 1

    return [state_name, elec_votes,dem_perc, rep_perc]

# run simulation
votes = electionSim()

# histogram of electoral votes from simulations
plt.figure(0)
plt.hist(votes[0])
plt.title("Dem")
plt.xlabel("Electoral Votes")
plt.ylabel("Frequency")

plt.figure(1)
plt.hist(votes[1])
plt.title("Rep")
plt.xlabel("Electoral Votes")
plt.ylabel("Frequency")

plt.show()









