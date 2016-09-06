from graphics import *

print("This program graphs value of investment over ten years")
x=eval(input("Your initial investment "))
p=eval(input("Your APR (e.g. 7% = '7'): "))
win=GraphWin("Your investment",320,240)
win.setCoords(-1,-50.0,12,x*5)
xaxis=Line(Point(0,0),Point(0,10))
yaxis=Line(Point(0,0),Point(0,x*5))
xaxis.draw(win)
yaxis.draw(win)
bar=Rectangle(Point(0,0),Point(1,x))
bar.setFill('grey')
bar.draw(win)
print("Year ",0,": $",round(x))

for i in range(0,x*5,x):
    label=Text(Point(-0.5,i),i)
    label.draw(win)

for i in range(10):
    x=x*(1+p/100)
    year=1+i
    bar=Rectangle(Point(year,0),Point(year+1,x))
    bar.setFill('grey')
    bar.draw(win)
    print("Year ",i+1,": $",round(x))

