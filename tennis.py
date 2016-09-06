from random import random

def printIntro():
    print("This program simulates tennis games between Player A and Player B" \
          "given a probability of each player winning his serve.")

def getInput():
    probA=eval(input("Probability of Player A winning serve: "))
    probB=eval(input("Probability of Player B winning serve: "))
    nGames=eval(input("Best of 'n' games per match (3 or 5): "))
    n=eval(input("Number of games to simulate: "))
    return probA, probB, nGames, n

def setOver(scoreSetA, scoreSetB):
    if scoreSetA > 3 and scoreSetA > scoreSetB+1 or \
       scoreSetB > 3 and scoreSetB > scoreSetA+1:     
        return True
    else: return False

def simOneSet(probA, probB):
    scoreSetA=scoreSetB=0
    serving="A"
    while not setOver(scoreSetA, scoreSetB):
        if serving=="A":
            if random() < probA:
                scoreSetA=scoreSetA+1
            else: serving="B"
        else:
            if random() < probB:
                scoreSetB=scoreSetB+1
            else: serving="A"
    return scoreSetA, scoreSetB       

def simOneGame(probA, probB):
    winSetsA=winSetsB=0
    for i in range(6):
        scoreSetA, scoreSetB = simOneSet(probA, probB)
        if scoreSetA>scoreSetB:
            winSetsA=winSetsA+1
        else: winSetsB=winSetsB+1
    return winSetsA, winSetsB

def simOneMatch(probA, probB, nGames):
    winGamesA=winGamesB=0
    for i in range(nGames):
        winSetsA, winSetsB = simOneGame(probA, probB)
        if winSetsA>winSetsB:
            winGamesA=winGamesA+1
        else: winGamesB=winGamesB+1
    return winGamesA, winGamesB

def simulate(probA, probB, nGames, n):
    winMatchesA=winMatchesB=0
    for i in range(n):
        winGamesA, winGamesB = simOneMatch(probA, probB, nGames)
        if winGamesA>winGamesB:
            winMatchesA=winMatchesA+1
        else: winMatchesB=winMatchesB+1
    return winMatchesA, winMatchesB

def printOutput(winMatchesA, winMatchesB):
    print("Player A won {0} matches.".format(winMatchesA))
    print("Player B won {0} matches.".format(winMatchesB))

def main():
    printIntro()
    probA, probB, nGames, n = getInput()
    winMatchesA, winMatchesB = simulate(probA, probB, nGames, n)
    printOutput(winMatchesA, winMatchesB)

if __name__=='__main__': main()
