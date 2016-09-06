from graphics import *
import math

print("This program will help you save face.")

def drawWindow():
    fileName=input("What is the name of the image file?\n")
    myImage=Image(Point(50,50),fileName)
    #Load image file to window
    win=GraphWin(myImage.getWidth(),myImage.getHeight())
    myImage.draw(win)
    win.setCoords(0,0,100,100)
    Text(Point(50,90),
         "Step 1: Click on center of your face.\n" \
         "Step 2: Click on opposite sides of face to set size").draw(win)
    print("Size of window: ",win.getHeight())
    return win

def drawFace(center, size, win):
    circ=Circle(center, size/2)
    mouth=Oval(Point(center.getX()-size/4,center.getY()-size/3),
               Point(center.getX()+size/4,center.getY()-size/4))
    nose=Polygon(center, Point(center.getX()-size/8,center.getY()-size/5),
                 Point(center.getX()+size/8,center.getY()-size/5))
    leye=Circle(Point(center.getX()-size/4,center.getY()+size/4),size/8)
    reye=leye.clone()
    reye.move(size/2,0)
    circ.draw(win)
    mouth.draw(win)
    nose.draw(win)
    leye.draw(win)
    reye.draw(win)

def getSize(p1,p2):
    dx=p2.getX()-p1.getX()
    dy=p2.getY()-p1.getY()
    size=math.sqrt(dx**2+dy**2)
    return size

def main():
    n=eval(input("How many faces do you want to save? "))
    win=drawWindow()
    for i in range(n):
        center=win.getMouse()
        p1=win.getMouse()
        p2=win.getMouse()
        size=getSize(p1,p2)
        drawFace(center, size, win)
main()
    
