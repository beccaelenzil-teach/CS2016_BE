import sys

def variation(xList,yList, order):

    directVar = []
    inverseVar = []

    num_points = len(xList)

    for k in range(order+1):
        directVar.append([1]*num_points)
        inverseVar.append([1]*num_points)

    for n in range(1,order+1):
        for i in range(num_points):

            if yList[i]/(xList[i]**n) == yList[i-1]/(xList[i-1]**n):
                directVar[n-1][i] = 0
            elif yList[i]*(xList[i]**n) == yList[i-1]*(xList[i-1]**n):
                inverseVar[n-1][i] = 0

        if sum(directVar[n-1]) == 0:
            print "The data varies directly with an equation of order ", n
            #sys.exit()
        elif sum(inverseVar[n-1]) == 0:
            print "The data varies inversely with an equation of order ", n
            #sys.exit()
        else:
            print "The data varies neither directly or inversely with an equation of order ", n


#variation([2.0,4.0,8.0],[4.0,2.0,1.0],10)


def simpleVar(xList,yList,n):
    """
    :param xList: x values
    :param yList: y values
    :param n: order of equation
    :return:
    """
    if yList[0]/(xList[0]**n) == yList[1]/(xList[1]**n) and yList[1]/(xList[1]**n) == yList[2]/(xList[2]**n) \
      and yList[2]/(xList[2]**n) == yList[3]/(xList[3]**n) and yList[3]/(xList[3]**n) == yList[0]/(xList[0]**n):
        print "The data varies directly with an equation of order ", n
    elif yList[0]*(xList[0]**n) == yList[1]*(xList[1]**n) and yList[1]*(xList[1]**n) == yList[2]*(xList[2]**n) \
      and yList[2]*(xList[2]**n) == yList[3]*(xList[3]**n) and yList[3]*(xList[3]**n) == yList[0]*(xList[0]**n):
        print "The data varies inversely with an equation of order ", n
    else:
        print "The data varies neither directly or inversely with an equation of order ", n

simpleVar([1,2,3,4],[1,4,9,16],2)
print " "
