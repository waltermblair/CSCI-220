import math

class Projectile:
    def __init__(self, angle, velocity, height):
        self.xpos = 0.0
        self.ypos = height
        theta=math.radians(angle)
        self.xvel=velocity*math.cos(theta)
        self.yvel=velocity*math.sin(theta)

    def getX(self):
        return self.xpos

    def getY(self):
        return self.ypos

    def getMax(self, time):
        maxX=1
        maxY=1
        timeElapsed=0
        while self.ypos>=0:
            self.xpos=self.xpos+time*self.xvel
            yvel1=self.yvel-time*9.8
            self.ypos=self.ypos+time*(self.yvel+yvel1)/2.0
            self.yvel=yvel1
            timeElapsed=timeElapsed+time
            if self.xpos>maxX:
                maxX=self.xpos
            if self.ypos>maxY:
                maxY=self.ypos
        return maxX,maxY

    def update(self, time):
        self.xpos=self.xpos+time*self.xvel
        yvel1=self.yvel-time*9.8
        self.ypos=self.ypos+time*(self.yvel+yvel1)/2.0
        self.yvel=yvel1
        return self.xpos, self.ypos


