from graphics import *

def createLabeledWindow(x):
    win=GraphWin("Your investment",320,240)
    win.setCoords(-1,-50.0,12,x*5)
    xaxis=Line(Point(0,0),Point(0,10))
    yaxis=Line(Point(0,0),Point(0,x*5))
    xaxis.draw(win)
    yaxis.draw(win)
    for i in range(0,x*5,x):
        label=Text(Point(-0.5,i),i)
        label.draw(win)
    return win

def drawBar(window, year, height):
    bar=Rectangle(Point(year,0),Point(year+1,height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(window)

def main():
    print("This program graphs value of investment over ten years")
    x=eval(input("Your initial investment "))
    p=eval(input("Your APR (e.g. 7% = '7'): "))

    print("Year ",0,": $",round(x))

    win=createLabeledWindow(x)  
    drawBar(win,0,x)

    for i in range(10):
        x=x*(1+p/100)
        year=1+i
        drawBar(win,year,x)
        print("Year ",i+1,": $",round(x))

main()
