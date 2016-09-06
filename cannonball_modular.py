import math
from cannonball_object import Projectile
from cannonball_tracker import Tracker
from graphics import *
from time import *
from button import *

def drawWin():
    win=GraphWin()
    win.setCoords(0,0,100,100)
    target=Rectangle(Point(60,0),Point(70,2))
    target.setFill('red')
    target.draw(win)
    quitButton=Button(win, Point(90,5),15,10,"Quit")
    quitButton.activate()
    return win, quitButton

def getInput():
    angle=eval(input("Launch angle in degrees: "))
    vel=eval(input("Initial velocity in m/s: "))
    h0=eval(input("Initial height in m: "))
    time=eval(input("Time interval between position calculations: "))
    return angle, vel, h0, time

def main():
    win,quitButton=drawWin()
    p=Point(50,50)
    while not quitButton.clicked(p):
        angle, vel, h0, time = getInput()
        cball=Projectile(angle, vel, h0)
        tracker=Tracker(win,cball)
        while cball.getY() >= 0:
            cball.update(time)
            tracker.moveTracker()
            sleep(0.05)
        print("\nDistance traveled: {0:0.1f} meters.".format(cball.getX()))
        if 60 <= cball.getX() <= 70:
            print("You win! Click to fire again.")
        else: print("Miss! Click to fire again.")
        p=win.getMouse()
    win.close()

if __name__=="__main__": main()
