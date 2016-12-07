from gameOfLifeFunctions import *
from visual import *

def constants():
    width = 40
    height = 40
    cell_size = 18
    spacing = 2
    return [width,height,cell_size,spacing]

def drawBoard(A):
    [width,height,cell_size,spacing] = constants()
    for row in range(height):
        x_pos = row*(cell_size+spacing)
        for col in range(width):
            y_pos = col*(cell_size+spacing)
            if A[row][col] == 1:
                box(pos=(x_pos,y_pos,0), size=(cell_size,cell_size,0), color=color.white)
            elif A[row][col] == 0:
                box(pos=(x_pos,y_pos,0), size=(cell_size,cell_size,0), color=color.black)


[w,h,cell_size,spacing] = constants()

w_window = w*(cell_size+spacing)
h_window = h*(cell_size+spacing)

gameOfLife = display(title='Game Of Life',
     x=0, y=0, width=w_window, height=h_window,
     center=(w_window/2,h_window/2,0), background=(1,1,1))

gameOfLife.exit = True

A = randomCells(w,h)
drawBoard(A)

while True:
    A = next_life_generation(A)
    drawBoard(A)
    rate(60)




