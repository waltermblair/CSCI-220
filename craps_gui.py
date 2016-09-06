from random import randrange
from dieview import DieView
from button import *
from graphics import *
from time import sleep

def printIntro():
    print("This program plays craps.")

def drawWin():
    win=GraphWin()
    win.setCoords(0,0,100,100)
    #Draw play button
    playButton=CButton(win, Point(50,20), 20, "Click to Play")
    playButton.activate()
    #Draw 2 DieView objects
    die1=DieView(win, Point(25, 70), 20)
    die2=DieView(win, Point(75, 70), 20)
    #Draw output label
    outputLabel=Text(Point(50,50),"Ready to Go")
    outputLabel.draw(win)
    #Draw a quit button
    quitButton=Button(win, Point(85,90), 15, 10, "Quit")
    quitButton.activate()
    return win, playButton, die1, die2, outputLabel, quitButton

def roll():
    d1 = randrange(1,6)
    d2 = randrange(1,6)
    return d1,d2

def game(die1, die2, outputLabel):
    #sends "win" or "loss" to output label
    d1, d2 = roll()
    firstRoll=d1+d2
    #takes value from each roll to die1 and die2
    die1.setValue(d1)
    die2.setValue(d2)
    die1.setColor()
    die2.setColor()
    outputLabel.setText("First Roll: {0}".format(d1+d2))
    sleep(0.05)
    if firstRoll in {2, 3, 12}:
        return "loss"
    elif firstRoll in {7, 11}:
        return "win"
    else:
        d1, d2 = roll()
        nextRoll=d1+d2
        die1.setValue(d1)
        die2.setValue(d2)
        die1.setColor()
        die2.setColor()
        if nextRoll==firstRoll:
            return "win"
        elif nextRoll==7:
            return "loss"
        else:
            while nextRoll!=7 and nextRoll!=firstRoll:
                d1, d2 = roll()
                nextRoll=d1+d2
                die1.setValue(d1)
                die2.setValue(d2)
                die1.setColor()
                die2.setColor()
                if nextRoll==7:
                    return "loss"
                elif nextRoll==firstRoll:
                    return "win"
                else:
                    sleep(0.05)
                    nextRoll=roll()

def main():
    printIntro()
    win, playButton, die1, die2, outputLabel, quitButton = drawWin()
    p=win.getMouse()
    while not quitButton.clicked(p):
        if playButton.clicked(p):
            if game(die1, die2, outputLabel)=="win":
                outputLabel.setText("You win!")
                playButton.activate()
            else:
                outputLabel.setText("You lose!")
                playButton.activate()
        p=win.getMouse()
    win.close()

if __name__=='__main__': main()
