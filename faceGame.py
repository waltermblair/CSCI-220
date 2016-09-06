#faceTime.py

from face import Face
from graphics import *
from button import *

def drawWin():
    win=GraphWin()
    win.setCoords(-50,-50,50,50)
    center=Point(0,0)
    smileButton=CButton(win, Point(-30,35), 12, "Smile")
    smileButton.activate()
    winkButton=CButton(win, Point(0,35), 12, "Wink")
    winkButton.activate()
    surpriseButton=CButton(win, Point(30,35), 12, "Surprise")
    surpriseButton.activate()
    resetButton=CButton(win, Point(0,-35), 10, "Reset")
    resetButton.activate()
    quitButton=Button(win, Point(35,-40), 15, 10, "Quit")
    return win, center, smileButton,winkButton,surpriseButton, \
           resetButton, quitButton
    

def main():
    win,center,smileButton,winkButton,surpriseButton, \
        resetButton,quitButton=drawWin()
    myFace=Face(win, center, 20)
    p=center
    while not quitButton.clicked(p):
        p=win.getMouse()
        quitButton.activate()
        if smileButton.clicked(p):
            myFace.doSmile(win)
        elif surpriseButton.clicked(p):
            myFace.doSurprise(win)
        elif winkButton.clicked(p):
            myFace.doWink(win)
        elif resetButton.clicked(p):
            myFace.reset()
        else: p=win.getMouse()
    win.close()
    
if __name__=="__main__": main()
