#three_button_monte.py
"Guess the right door, win a prize!"

from button import Button
from graphics import *
from random import randrange

def drawWin():
    win=GraphWin(320,240)
    win.setCoords(0,0,10,10)
    door1=Button(win, Point(2.5,6),2,3.5,"Door 1")
    door2=Button(win, Point(5,6),2,3.5,"Door 2")
    door3=Button(win, Point(7.5,6),2,3.5,"Door 3")
    playButton=Button(win, Point(5,3),4,1,"Play")
    playButton.activate()
    message=Text(Point(5,1),"Guess if you dare!")
    message.draw(win)
    score=Text(Point(5,2),"")
    score.draw(win)
    quitButton=Button(win, Point(8,9),2,1,"Quit")
    quitButton.activate()
    return win, door1, door2, door3, playButton, message, score, quitButton

def randDoor():
    door=randrange(1,4)
    return door

def main():
    win, door1, door2, door3, playButton, message, score, quitButton=drawWin()
    door=randDoor()
    p = win.getMouse()
    if playButton.clicked(p):
        door1.activate()
        door2.activate()
        door3.activate()
        p=win.getMouse()
        wins=losses=0
        while not quitButton.clicked(p):
            if door1.clicked(p) and door==1 or \
               door2.clicked(p) and door==2 or \
               door3.clicked(p) and door==3:
               message.setText("Congrats, you win! Choose again.")
               wins=wins+1
            else:
               message.setText("No, Door #{0} was correct! " \
                               "Choose again.".format(door))
               losses=losses+1
            score.setText("Wins: {0}, Losses: {1}".format(wins, losses))
            door=randDoor()
            p=win.getMouse()
    win.close()
    
if __name__=='__main__': main()
