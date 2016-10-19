def isOdd(n):
    if n%2 != 0:
        return True
    else:
        return False

def numToBinaryOrion(N):
    ret = ''
    if N == 0:
        return '0'
    while N > 0:
        if N % 2 == 0:
            ret = ret + '0'
            N = N/2
        else:
            ret = ret + '1'
            N = (N-1)/2
    return ret

print "numToBinaryOrion(21) should be 10101 == ", numToBinaryOrion(10101)

def numToBinary(N):
    """
    convert a base 10 number to binary
    """
    if N == 0:
        return ''
    elif N%2 != 0:
        N = (N-1)/2
        return numToBinary(N) + '1'
    else:
        N = N/2
        return numToBinary(N) +'0'
#print numToBinary(10)

def binaryToNum(S):
    """
    convert a binary number (S) to a base 10 number
    """
    S_list = list(S)
    S_list.reverse()
    S = ''.join(S_list)
    Num = 0
    power = 0
    Num_List = []
    if S == '':
        return 0
    for p in range(len(S)):
        Num_List.append(int(S[p])*2**p)
    return sum(Num_List)

#print binaryToNum('000')

def increment(S):
    n = binaryToNum(S)
    x = n+1
    y = '0'*(len(S)-len(numToBinary(x)))+numToBinary(x)
    return y

#print increment('0000')

def count(S,n):
    if n == 1:
        print S
    else:
        S = increment(S)
        print S
        count(S,n-1)

#count('0000',10)

def numToTernary(N):
    if N == 0:
        return ''
    elif N%3 == 1:
        N = (N-1)/3
        return numToTernary(N) + '1'
    elif N%3 == 2:
        N = (N-2)/3
        return numToTernary(N) + '2'
    else:
        N = N/3
        return numToTernary(N) +'0'

#print numToTernary(42)

def ternaryToNum(S):
    """
    convert a ternary number (S) to a base 10 number
    """
    S_list = list(S)
    S_list.reverse()
    S = ''.join(S_list)
    Num = 0
    power = 0
    Num_List = []
    if S == '':
        return 0
    for p in range(len(S)):
        Num_List.append(int(S[p])*3**p)
    return sum(Num_List)

#print ternaryToNum('1120')

def balancedTernaryToNum(S):
    """
    convert a balanced ternary number (S) to a base 10 number
    """
    S_list = list(S)
    S_list.reverse()
    S = S_list
    #S = ''.join(S_list)
    Num = 0
    power = 0
    count = 0
    Num_List = []
    if S == '':
        return 0
    for p in S:
        sign = 1
        if S[count] != '0':
            S[count] = '1'
        if p == '-':
            sign = -1
        Num_List.append(sign*int(S[count])*3**count)
        count = count+1
    return sum(Num_List)

balancedTer = '-0---+'

print balancedTernaryToNum(balancedTer)

def numToBalancedTernary(N):
    if N == 0:
        return ''
    elif N%3 == 1:
        N = (N-1)/3
        return numToBalancedTernary(N) + '+'
    elif N%3 == 2:
        N = (N+1)/3
        return numToBalancedTernary(N) + '-'
    else:
        N = N/3
        return numToBalancedTernary(N) +'0'


def numToTernary(N):
    if N == 0:
        return ''
    elif N%3 == 1:
        N = (N-1)/3
        return numToTernary(N) + '1'
    elif N%3 == 2:
        N = (N-2)/3
        return numToTernary(N) + '2'
    else:
        N = N/3
        return numToTernary(N) +'0'

print balancedTer
print numToBalancedTernary(balancedTernaryToNum(balancedTer))

def numToBase(N,b):
    """
    :param N: Number
    :param b: base
    :return: Number is base 10 converted to base b
    """
    if N == 0:
        return ''
    for i in range(0,b):
        if N % b == i:
            N = (N-i)/b
            return numToBase(N,b) + str(i)

print "numToBase(21,2) = ", numToBase(21,2)
print "numToBase(21,3) = ", numToBase(21,3)
print "numToBase(101,4) = ", numToBase(102,4)

def baseToNum(S,b):
    """
    :param S: a string in base b
    :param b: the base
    :return: the number in base 10
    """
    S_list = list(S)
    S_list.reverse()
    S = ''.join(S_list)
    Num = 0
    power = 0
    Num_List = []
    if S == '':
        return 0
    for p in range(len(S)):
        Num_List.append(int(S[p])*b**p)
    return sum(Num_List)

print 'baseToNum(\'10101\',3) = ', baseToNum('10101',3)
