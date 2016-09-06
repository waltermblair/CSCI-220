#face.py
from graphics import *
from time import sleep
from math import sqrt

class Face:

    def __init__(self, window, center, size):
        eyeSize = 0.15*size
        eyeOff=size/3.0
        mouthSize=0.8*size
        mouthOff=size/2.0
        self.head=Circle(center,size)
        self.head.draw(window)
        self.leftEye=Circle(center,eyeSize)
        self.leftEye.move(-eyeOff,eyeOff)
        self.rightEye=Circle(center,eyeSize)
        self.rightEye.move(eyeOff,eyeOff)
        self.leftEye.draw(window)
        self.rightEye.draw(window)
        p1=center.clone()
        p1.move(-mouthSize/2,-mouthOff)
        p2=center.clone()
        p2.move(mouthSize/2,-mouthOff)
        self.mouth=Line(p1,p2)
        self.mouth.draw(window)
        #doSmile
        p1Smile=p1.clone()
        p1Smile.move(0,1)
        p2Smile=p2.clone()
        p2Smile.move(0,1)
        p3=p1Smile.clone()
        p3.move(mouthSize/4,-mouthSize/4)
        p4=p2Smile.clone()
        p4.move(-mouthSize/4,-mouthSize/4)
        self.smile=Polygon(p1Smile,p2Smile,p4,p3)
        self.smile.setOutline("white")
        self.smile.draw(window)
        #doWink
        self.wink=Line(Point(center.getX()+eyeOff-eyeSize, \
                             center.getY()+eyeOff), \
                       Point(center.getX()+eyeOff+eyeSize, \
                             center.getY()+eyeOff))
        self.wink.setOutline("white")
        self.wink.draw(window)
        #doSurprise
        self.leftEyeBig=Circle(center,eyeSize*2)
        self.leftEyeBig.move(-eyeOff,eyeOff)
        self.leftEyeBig.setOutline("white")
        self.leftEyeBig.draw(window)
        self.rightEyeBig=Circle(center,eyeSize*2)
        self.rightEyeBig.move(eyeOff,eyeOff)
        self.rightEyeBig.setOutline("white")
        self.rightEyeBig.draw(window)

    def doSmile(self, window):
        self.mouth.setOutline("white")
        self.smile.setOutline("black")

    def doWink(self, window):
        self.rightEye.setOutline("white")
        self.rightEyeBig.setOutline("white")
        self.wink.setOutline("black")

    def doSurprise(self, window):
        self.leftEye.setOutline("white")
        self.rightEye.setOutline("white")
        self.wink.setOutline("white")
        self.leftEyeBig.setOutline("black")
        self.rightEyeBig.setOutline("black")

    def reset(self):
        self.leftEyeBig.setOutline("white")
        self.rightEyeBig.setOutline("white")
        self.wink.setOutline("white")
        self.smile.setOutline("white")
        self.leftEye.setOutline("black")
        self.rightEye.setOutline("black")
        self.mouth.setOutline("black")
        
    def move(self, x, y):
        self.head.move(x,y)
        self.leftEye.move(x,y)
        self.rightEye.move(x,y)
        self.leftEyeBig.move(x,y)
        self.rightEyeBig.move(x,y)
        self.wink.move(x,y)
        self.mouth.move(x,y)
        self.smile.move(x,y)

    def getCenter(self):
        return self.head.getCenter()
