def printRect(width, height, symbol ):
    for h in range(height):
        print width * symbol

printRect( 4, 6, '%' )


def printTriangle(width, symbol, rightSideUp):
    if rightSideUp == True:
        for w in range(1,width+1):
            print w*symbol
    else:
        for w in range(width,0,-1):
            print w*symbol



printTriangle( 3, '@', True )
printTriangle( 3, '@', False)
