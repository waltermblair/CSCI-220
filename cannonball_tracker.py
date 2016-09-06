#cannonball_tracker.py

from graphics import *
from cannonball_object import *

class Tracker:

    def __init__(self, window, objToTrack):
        self.win=window
        self.obj=objToTrack
        x=objToTrack.getX()
        y=objToTrack.getY()
        self.circ=Circle(Point(x,y),5)
        self.circ.setFill("black")
        self.circ.draw(window)

    def moveTracker(self):
        point=self.circ.getCenter()
        x=point.getX()
        y=point.getY()
        self.circ.move((self.obj.getX()-x),(self.obj.getY()-y))
        Point(self.obj.getX(),self.obj.getY()).draw(self.win)
