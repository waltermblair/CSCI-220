from graphics import *

print("This program generates a histogram from a file of quiz scores 1-10")
scores_fileName=input("What is the name of the file? ")
scores_file=open(scores_fileName,"r")
scores_string=scores_file.read()
scores_data=scores_string.split()

n=len(scores_data)

scores=[]
i=0

win=GraphWin(320,240)
win.setCoords(-10,-10,120,40)
xaxis=Line(Point(0,0),Point(120,0))
xaxis.setWidth(3)
xaxis.draw(win)
dx=10
width=7

#count each score in this list
for i in range(11):
    scores.append(scores_data.count(str(i)))
    dy=scores[i]
    bar=Rectangle(Point(0+dx*i,0),Point(width+dx*i,dy))
    bar.setFill("grey")
    bar.draw(win)
    Text(Point(5+dx*i,-5),i).draw(win)

scores_file.close()
