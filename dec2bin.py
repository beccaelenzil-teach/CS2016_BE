def isOdd(n):
    if n % 2 == 1:
        return True
    else:
        return False

def numToBinary(N):
  """
  input a decimal number N
  output the binary form
  """
  if N == 0:
    return ''
  elif N%2 == 1:
    return numToBinary(N//2) + '1'
  else:
    return numToBinary(N/2) + '0'


print "numToBinary(0) == '' = ",numToBinary(0)
print "numToBinary(1) == '1' = ",numToBinary(1)
print "numToBinary(4) == '100' = ",numToBinary(4)
print "numToBinary(10) == '1010' = ",numToBinary(10)
print "numToBinary(42) == '101010' = ",numToBinary(42)
print "numToBinary(100) == '1100100' = ",numToBinary(100)

def binaryToNum(S):
  """
  input binary number S
  return decimal
  """
  if S == '':
    return 0
  # if the last digit is a '1'
  elif S[-1] == '1':
    return  2*binaryToNum(S[:-1]) + 1
  else: # last digit must be '0'
    return  2*binaryToNum(S[:-1]) + 0

print "binaryToNum(100) == 4 = ",binaryToNum("100")
print "binaryToNum(1011) == 11 = ",binaryToNum("1011")
print "binaryToNum(00001011) == 11 = ",binaryToNum("00001011")
print "binaryToNum() == 0 = ",binaryToNum("")
print "binaryToNum(0) == 0 = ",binaryToNum("0")
print "binaryToNum(1100100) == 100 = ",binaryToNum("1100100")
print "binaryToNum(101010) == 42 = ",binaryToNum("101010")


def increment(S):
    n = binaryToNum(S)
    x = n+1
    y = numToBinary(x)
    return '0'*(8-len(y)) + y


print increment('00000001')


def count(S,n):
    print S
    for i in range(n):
        S = increment(S)
        print S

count("00000000", 4)

def numToTernary(N):
  """
  input a decimal number N
  output the binary form
  """
  if N == 0:
    return ''
  elif N%3 == 2:
    return numToTernary(N//3) + '2'
  elif N%3 == 1:
    return numToTernary(N//3) + '1'
  else:
    return numToTernary(N/3) + '0'

print numToTernary(42)
print numToTernary(4242)

def ternaryToNum(S):
  """
  input binary number S
  return decimal
  """
  if S == '':
    return 0
  # if the last digit is a '1'
  elif S[-1] == '2':
    return  3*ternaryToNum(S[:-1]) + 2
  elif S[-1] == '1':
    return  3*ternaryToNum(S[:-1]) + 1
  else: # last digit must be '0'
    return  3*ternaryToNum(S[:-1]) + 0


print ternaryToNum('1120')
print ternaryToNum('12211010')
