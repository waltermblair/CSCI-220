from random import randrange
from random import random
from math import sqrt

def printIntro():
    print("This program uses a simulation to solve an analytic geometry " \
          "problem - if you are standing in the center of a cube, " \
          "each wall would occupy 1/6 of your field of vision. " \
          "If you step halfway toward one wall, what fraction of your " \
          "field of vision is now taken by this closest wall?")

def getInput():
    n=eval(input("How many simulations would you like to run? "))
    return n

#I don't really understand the problem. 
def squares():
    xOuter=10
    AOuter=xOuter**2
    AInner=1/6*AOuter
    xInner=sqrt(AInner)
    return xInner

def look():
    xLook=random()*10
    yLook=random()*10
    return xLook, yLook

def lookHit():
    xInner = squares()
    xLook, yLook = look()
    if xLook<xInner and yLook<xInner:
        return True
    else: False

def simulation(n):
    sumLookHit=0
    for i in range(n):
        if lookHit():
            sumLookHit=sumLookHit+1
    solution=sumLookHit/n
    return solution

def printOutput(solution):
    print("Now 1/{0} of your vision is taken by the closest " \
          "wall.".format(int(1/solution)))

def main():
    printIntro()
    n=getInput()
    solution=simulation(n)
    printOutput(solution)

if __name__=="__main__": main()
