from graphics import *

win=GraphWin()
win.setCoords(0,0,100,100)

mouth=Oval(Point(25,25),Point(75,30))
nose=Polygon(Point(50,60),Point(45,50),Point(55,50))
eye1=Circle(Point(30,75),15)
pupil1=Circle(Point(35,65),4)
pupil1.setFill("black")
eye2=Circle(Point(70,75),15)
pupil2=Circle(Point(75,65),4)
pupil2.setFill("black")

mouth.draw(win)
nose.draw(win)
eye1.draw(win)
pupil1.draw(win)
eye2.draw(win)
pupil2.draw(win)
