from random import random
import graphics

def printIntro():
    print("This program estimates the value of pi by throwing darts " \
          "randomly at a target inscribed in a square cabinet.")

def getInput():
    n=eval(input("How many darts do you want to throw? "))
    return n

def throw():
    x=2*random()-1
    y=2*random()-1
    return x,y

def estimation(n):
    h=0
    for i in range(n):
        x, y = throw()
        if x**2+y**2<=1:
            h=h+1
    pi = 4 * (h / n)
    return pi

def printOutput(pi):
    print("Pi is estimated to be {0}".format(pi))

def main():
    printIntro()
    n=getInput()
    pi=estimation(n)
    printOutput(pi)

if __name__=='__main__': main()
    
