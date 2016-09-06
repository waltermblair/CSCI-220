from random import random
from random import randrange

def printIntro():
    print("This program runs a racquetball simulation!" \
          "Enter a number between 0 and 1 to indicate probability" \
          "of a player winning his serve. In this simulation, " \
          "player A always serves first.")

def getInput():
    probA=eval(input("What is prob. that player A wins a serve? "))
    probB=eval(input("What is prob. that player B wins a serve? "))
    nGames=eval(input("How many games are in each match? "))
    n=eval(input("How many matches to simulate? "))
    return probA, probB, nGames, n

def simOneGame(probA,probB):
    scoreA=scoreB=0
    serving="A"
    while scoreA<15 and scoreB<15:
        if serving=="A":
            if random()<probA:
                scoreA=scoreA+1
            else: serving="B"
        if serving=="B":
            if random()<probB:
                scoreB=scoreB+1
            else: serving="A"
    return scoreA, scoreB

def simOneMatch(probA, probB, nGames):
    winGamesA=winGamesB=0
    serving="A"
    for i in range(nGames):
        scoreA, scoreB = simOneGame(probA,probB)
        if scoreA>scoreB:
            winGamesA=winGamesA+1
        else: winGamesB=winGamesB+1
        if i%2==0:
            serving="B"
        else: serving="A"
    return winGamesA, winGamesB

def simulate(probA,probB,nGames,n):
    winMatchA=0
    winMatchB=0
    shutOutA=0
    shutOutB=0
    for i in range(n):
        winGamesA,winGamesB = simOneMatch(probA,probB,nGames)
        if winGamesA>winGamesB:
            winMatchA=winMatchA+1
        else: winMatchB=winMatchB+1
        if winGamesB==0:
            shutOutA=shutOutA+1
        if winGamesA==0:
            shutOutB=shutOutB+1
    return winMatchA, winMatchB, shutOutA, shutOutB

def printOutput(winMatchA, winMatchB, shutOutA, shutOutB):
    print("Player A won {0} games. {1} wins were shutouts.".format(winMatchA, shutOutA))
    print("Player B won {0} games. {1} wins were shutouts.".format(winMatchB, shutOutB))

def main():
    printIntro()
    probA, probB, nGames, n = getInput()
    winMatchA, winMatchB, shutOutA, shutOutB = simulate(probA,probB,nGames,n)
    printOutput(winMatchA, winMatchB, shutOutA, shutOutB)

if __name__ == '__main__': main()
