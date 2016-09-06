from random import random

def printIntro():
    print("This program simulates a rally volleyball game." \
          "Enter the probability of team A and team B winning its serve" \
          "and the number of games you'd like to simulate.")

def getInput():
    probA=eval(input("Probability of team A winning its serve: "))
    probB=eval(input("Probability of team B winning its serve: "))
    n=eval(input("Number of games to simulate: "))
    return probA, probB, n

def gameOver(scoreA, scoreB):
    if scoreA>=15 and scoreA>scoreB+1 or scoreB>=15 and scoreB>scoreA+1:
        return True
    else: False

def simOneGame(probA, probB):
    scoreA=scoreB=0
    while not gameOver(scoreA, scoreB):
        if random()<probA:
            scoreA=scoreA+1
        else: scoreB=scoreB+1
    return scoreA, scoreB

def simulate(probA, probB, n):
    winA=winB=0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA>scoreB:
            winA=winA+1
        else: winB=winB+1
    return winA, winB

def printOutput(winA, winB):
    print("Team A won {0} games.".format(winA))
    print("Team B won {0} games.".format(winB))

def main():
    printIntro()
    probA, probB, n = getInput()
    winA, winB = simulate(probA, probB, n)
    printOutput(winA, winB)

if __name__ == '__main__': main()
