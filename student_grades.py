from graphics import *

print("This program will graph students scores from a file")
grade_fileName=input("Enter the name of the grade file: ")

grade_file=open(grade_fileName,"r")
n=eval(grade_file.readline())

win=GraphWin(320,240)
win.setCoords(-50,-5,100,120)
x=0
y=100
dy=10
width=7
xaxis=Line(Point(0,0),Point(100,0))
yaxis=Line(Point(0,0),Point(0,100))
xaxis.draw(win)
yaxis.draw(win)

grade_data=[]
i=0

for i in range(10) :
    grade_string=grade_file.readline()
    grade_data.append(grade_string.split())
    dx=eval(grade_data[i][1])
    grade_bar=Rectangle(Point(0,90-dy*i),Point(0+dx,(90-dy*i)+width))
    grade_bar.setFill("grey")
    grade_bar.draw(win)
    name=grade_data[i][0]
    Text(Point(-20,95-dy*i),name).draw(win)

grade_file.close()
