from random import random
import math
from graphics import *
from time import sleep

def printIntro():
    print("This program draws your random walk of n steps.")

def getInput():
    n=eval(input("How many steps will you take? "))
    return n

def drawGraph():
    win=GraphWin(200,200)
    win.setCoords(0,0,100,100)
    origin=Point(50,50)
    origin.draw(win)
    return win, origin

def simulate(n, win, origin, me):
    x=origin.getX()
    y=origin.getY()
    for i in range(n):
        angle=random()*2*math.pi
        x=x+math.cos(angle)
        y=y+math.sin(angle)
        Point(x,y).draw(win)
        sleep(0.0005)

def main():
    printIntro()
    n=getInput()
    win, origin, me = drawGraph()
    simulate(n, win, origin, me)

if __name__=='__main__': main()
