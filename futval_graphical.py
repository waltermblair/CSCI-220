from graphics import *

win=GraphWin("Your investment over 10 years (<$500)",320,240)
win.setCoords(-1,-50.0,10,1000)
Text(Point(5,900),"Your initial investment: ").draw(win)
Text(Point(5,800),"Your APR(e.g. 7% = '7'): ").draw(win)
xinput=Entry(Point(8,900),5)
xinput.draw(win)
pinput=Entry(Point(8,800),5)
pinput.draw(win)
button=Text(Point(5,650),"Crunch the Numbers")
button.draw(win)
Rectangle(Point(2,600),Point(8,700)).draw(win)

win.getMouse()

xaxis=Line(Point(0,0),Point(0,10))
yaxis=Line(Point(0,0),Point(0,1000))
xaxis.draw(win)
yaxis.draw(win)

x=eval(xinput.getText())
p=eval(pinput.getText())


for i in range(0,x*5,x):
    label=Text(Point(-0.5,i),i)
    label.draw(win)

for i in range(10):
    x=x*(1+p/100)
    bar=Rectangle(Point(0+1*i,0),Point(0+1*(i+1),x))
    bar.setFill('grey')
    bar.draw(win)
    print("Year ",i+1,": $",round(x))

