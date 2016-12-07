# python 2
#
# Game of Life
#
# Name:
#

import random

def createOneRow(width):
    """ returns one row of zeros of width "width"...
         You should use this in your
         createBoard(width, height) function """
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width, height):
    """ returns a 2d array with "height" rows and "width" cols """
    A = []
    for row in range(height):
        A += [createOneRow(width)]    # What do you need to add a whole row here?
    return A

def printBoard(A):
    for row in A:
        line = ''
        for col in row:
            line += str(col)
        print line

def diagonalize(width, height):
    """ creates an empty board and then modifies it
        so that it has a diagonal strip of "on" cells.
    """
    A = createBoard(width, height)

    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0

    return A

def innerCells(width, height):
    """ creates an empty board and then modifies it
        so that it has a diagonal strip of "on" cells.
    """
    A = createBoard(width, height)

    for row in range(1,height-1):
        for col in range(1,width-1):
            A[row][col] = 1

    return A

def randomCells(width, height):
    """ creates an empty board and then modifies it
        so that it has a diagonal strip of "on" cells.
    """
    A = createBoard(width, height)

    for row in range(1,height-1):
        for col in range(1,width-1):
            A[row][col] = random.choice([0,1])

    return A

def copy(A):
    height = len(A)
    width = len(A[0])
    newA = createBoard(width,height)
    for row in range(height):
        for col in range(width):
            newA[row][col] = A[row][col]

    return newA


def innerReverse(A):
    newA = copy(A)
    height = len(A)
    width = len(A[0])
    for row in range(height):
        for col in range(width):
            if A[row][col] == 0:
                newA[row][col] = 1
            else:
                newA[row][col] = 0
    return newA

def countNeighbors(row,col,A):
    count = 0
    for r in range(row-1,row+2):
        for c in range(col-1,col+2):
            count += A[r][c]
    count -= A[row][col]
    return count


def next_life_generation(A):
    """ makes a copy of A and then advances one
        generation of Conway's game of life within
        the *inner cells* of that copy.
        The outer edge always stays at 0.
    """
    height = len(A)
    width = len(A[0])
    newA = copy(A)
    for row in range(1,height-1):
        for col in range(1,width-1):
            count = countNeighbors(row,col,A)
            if count < 2:
                newA[row][col] = 0
            elif count > 3:
                newA[row][col] = 0
            elif count == 3:# and A[row][col] == 0:
                newA[row][col] = 1
    #static = (newA == A)
    #return [static,newA]
    return newA

A = [ [0,0,0,0,0],
      [0,0,1,0,0],
      [0,0,1,0,0],
      [0,0,1,0,0],
      [0,0,0,0,0]]

print countNeighbors(2,2,A)
