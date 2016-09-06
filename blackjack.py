from random import randrange
import graphics
from cardDeck import *
from button import *

def printIntro():
    print("""This program watches a dealer play blackjack. It uses
    the cardDeck and button modules.""")

def drawWin():
    win=GraphWin(320,240)
    win.setCoords(-1,-1,11,11)
    playButton=CButton(win, Point(5,1.95), 1.75, "Play")
    quitButton=Button(win, Point(9,9.5), 2, 1, "Quit")
    message=Text(Point(5,-.5),"Let's do this.")
    message.draw(win)
    slot1=Rectangle(Point(0,4.5),Point(2,8))
    slot1.setWidth(1.95)
    slot1.draw(win)
    slot2=slot1.clone()
    slot2.draw(win)
    slot2.move(2,0)
    slot3=slot2.clone()
    slot3.draw(win)
    slot3.move(2,0)
    slot4=slot3.clone()
    slot4.draw(win)
    slot4.move(2,0)
    slot5=slot4.clone()
    slot5.draw(win)
    slot5.move(2,0)
    playButton.activate()
    return win, playButton, quitButton, message, slot1, slot2, \
           slot3, slot4, slot5

def hasAce(cardValue):
    if cardValue==1:
        return True

def main():
    printIntro()
    win, playButton, quitButton, message, slot1, slot2, \
           slot3, slot4, slot5 = drawWin()
    p=win.getMouse()
    if playButton.clicked(p):
        quitButton.activate()
        while not quitButton.clicked(p):
            dealerPoints=0
            i=1
            while dealerPoints < 17:
                card=playingCard(randrange(1,13),randrange(1,5))
                cardValue=card.drawBlackjack(card.getValue())
                print(cardValue)
                card.draw(win, Point(i,6.25), card.getRank(), card.getSuit())
                if hasAce(cardValue):
                    if dealerPoints+10<21:
                        dealerPoints=dealerPoints+10+cardValue
                    else: dealerPoints=dealerPoints+cardValue
                else: dealerPoints=dealerPoints+cardValue
                i=i+2
            print("Dealer score is: ",dealerPoints)
            print("--"*20)
            if dealerPoints>21: 
                print("Dealer busts")
            p=win.getMouse()
        win.close()

if __name__=='__main__': main()
