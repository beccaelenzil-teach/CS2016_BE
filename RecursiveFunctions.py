def listReverse(L):
    """
    input: list L
    output: reverse of list L
    """
    K = []
    if len(L) == 1:
        return L
    else:
        return [L[-1]] + listReverse(L[:-1])

def listReverseIter(L):
    """
    input: list L
    output: reverse of list L
    """
    K = []
    for i in range(len(L)-1,-1,-1):
        K.append(L[i])
    return K

print listReverse([1,2,3,4])
print listReverseIter([1,2,3,4])

def fibIter(n):
    L = [0,1]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(1,n):
            L.append(L[i-1] + L[i])
        print L
        return L[n]

def fib(n):
    L = [0,1]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

n = 11
print fibIter(n)
print fib(n)

