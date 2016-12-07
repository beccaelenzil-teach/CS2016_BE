# python 2
#
# Homework 3, Problem 1
#
# name: Becca

from turtle import *
import time

def poly( n, N ):
    """ draws n sides of an N-sided regular polygon """
    if n == 0:
        return
    else:
        forward( 50 )   # 50 is hard-coded at the moment...
        left( 360.0/N )
        poly( n-1, N )

poly(7,7)

def spiral(initialLength, angle, multiplier):
  """draws a spiral with initialLength, that changes at angle, where the
  length of each segment changes by a factor multiplie"""
  if initialLength < 1 or initialLength > 500:
    return
  else:
    forward(initialLength)
    left(angle)
    spiral(initialLength*multiplier,angle,multiplier)

#spiral(100,90,0.9)

def chai(size):
  """our chai function"""
  if (size<9):
        return
  else:
        forward(size)
        left(90)
        forward(size/2.0)
        right(90)
        chai(size/2.0)
        right(90)
        forward(size)
        left(90)
        chai(size/2.0)
        left(90)
        forward(size/2.0)
        right(90)
        backward(size)
        return

#chai(100)

def svtree(trunklength, level):
  ang = 30
  div = 1.5
  if level == 0:
    return
  forward(trunklength)
  left(ang)
  svtree(trunklength/div,level-1)
  right(2*ang)
  svtree(trunklength/div,level-1)
  left(ang)
  backward(trunklength)

#penup();
#backward(150);
#pendown();
#svtree(100,7)

def flakeside(sidelength, levels):
  div = 3
  if levels == 0:
     return forward(sidelength)
  else:
    forward(sidelength/div)
    right(60)
    forward(sidelength/div)
    left(60)
    left(60)
    forward(sidelength/div)
    right(60)
    forward(sidelength/div)
    right(60)
    flakeside(sidelength, levels - 1)
    left(60)
    flakeside(sidelength, levels - 1)

#flakeside(100,3)

def snowflake(sidelength, levels):
    """ fractal snowflake function
    sidelength: pixels in the largest-scale triangle side
    levels: the number of recursive levels in each side
    """
    flakeside( sidelength, levels )
    left(120)
    flakeside( sidelength, levels )
    left(120)
    flakeside( sidelength, levels )
    left(120)

#snowflake(50,1)
