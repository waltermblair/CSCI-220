from graphics import *

print("This program calculates linear regression from several data points.")

class Regression:

    def __init__(self):
        self.count=0
        self.xsum=0
        self.ysum=0
        self.xysum=0
        self.xsqsum=0

    def addPoint(self, win):
        while True:
            p=win.getMouse()
            p.draw(win)
            x=p.getX()
            y=p.getY()
            self.xsum=self.xsum+x
            self.ysum=self.ysum+y
            self.xysum=self.xysum+x*y
            self.xsqsum=self.xsqsum+x**2
            self.count=self.count+1
            if x>0.25 and x<1.75 and y>0.5 and y<1.5: break

    def bestFit(self, win):
        self.m = (self.xysum-self.count*(self.xsum/self.count)* \
            (self.ysum/self.count))/(self.xsqsum-self.count* \
            (self.xsum/self.count)**2)
        p1y = self.ysum/self.count+self.m*(10-self.xsum/self.count)
        self.p2y = self.ysum/self.count+self.m*(0-self.xsum/self.count)
        p1 = Point(10,p1y)
        p2 = Point(0,self.p2y)
        line = Line(p1,p2)
        line.draw(win)
        print("y-intercept = ",self.p2y)

    def predict(self, x):
        y=self.m*x+self.p2y
        print("y-value: ",y)

#Make window with done button
def drawWindow():
    win=GraphWin(640,480)
    win.setCoords(0,0,10,10)
    xaxis=Line(Point(0,5),Point(10,5))
    yaxis=Line(Point(5,0),Point(5,10))
    xaxis.draw(win)
    yaxis.draw(win)
    Text(Point(5,9),"Click several data points and then click 'Done'" \
         "to compute regression").draw(win)
    Text(Point(1,1),"Done").draw(win)
    Rectangle(Point(0.25,0.5),Point(1.75,1.5)).draw(win)
    return win

def main():
    win=drawWindow()
    lsr = Regression()
    lsr.addPoint(win)
    lsr.bestFit(win)
    lsr.predict(eval(input("x-value: ")))
    win.getMouse()
    win.close()

main()
