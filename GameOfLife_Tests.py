print 'Total Score: '
print 'Notes: '
print "------------------------------------- "
print ' '
print 'diagonalize()'
print "------------------------------------- "
A = diagonalize(5,5)
printBoard(A)
print 'innerReverse()'
print "------------------------------------- "
Areverse = innerReverse(A)
printBoard(Areverse)
print ' '
print 'innerCells()'
print "------------------------------------- "
A = innerCells(5,5)
printBoard(A)
print ' '
print 'randomCells()'
print "------------------------------------- "
A = randomCells(5,5)
printBoard(A)
print ' '
print 'countNeighbors()'
print "------------------------------------- "
A = [ [0,0,0,0,0],
      [0,0,1,0,0],
      [0,0,1,0,0],
      [0,0,1,0,0],
      [0,0,0,0,0]]
print 'A = '
printBoard(A)
print 'countNeighbors(2,2,A) = 2:',countNeighboroughs(2,2,A), 2 == countNeighboroughs(2,2,A)
print ' '
print 'next_life_generation()'
print "------------------------------------- "
A = [ [0,0,0,0,0],
      [0,0,1,0,0],
      [0,0,1,0,0],
      [0,0,1,0,0],
      [0,0,0,0,0]]
print 'A = '
printBoard(A)
A2 = next_life_generation(A)
print "A2 = next_life_generation(A) --> printBoard(A2) should look like"
print '00000'
print '00000'
print '01110'
print '00000'
print '00000'
print 'and it looks like'
printBoard(A2)
