#cardDeck.py
"This module contains a deck of cards."

from random import randrange
from graphics import *

class playingCard:

    def __init__(self, rank, suit):
        self.rank=rank
        if suit==1:
            self.suit="d"
        elif suit==2:
            self.suit="c"
        elif suit==3:
            self.suit="h"
        else: self.suit="s"

    def drawBlackjack(self, cardValue):
        if cardValue>10:
            cardValue=10
        return cardValue

    def getValue(self):
        return self.rank

    def getRank(self):
        if self.rank==1:
            return "ace"
        elif self.rank==11:
            return "jack"
        elif self.rank==12:
            return "queen"
        elif self.rank==13:
            return "king"
        else: return self.rank

    def getSuit(self):
        return self.suit

    def __str__(self):
        return "{0} of {1}".format(self.getRank(), self.getSuit())

    def draw(self, win, center, rank, suit):
        if suit=="d":
            suit="diamonds"
        if suit=="c":
            suit="clubs"
        if suit=="h":
            suit="hearts"
        if suit=="s":
            suit="spades"
        gif=Image(center, "cards/{0}_of_{1}.gif".format(rank,suit))
        gif.draw(win)

def main():
    n=eval(input("How many cards? "))
    for i in range(n):
        card=playingCard(randrange(1,13),randrange(1,5))
        print(card)
        
if __name__=='__main__': main()
