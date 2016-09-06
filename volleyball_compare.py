from random import random
import volleyball
import volleyball_rally

def printIntro():
    print("This program compares normal v. rally volleyball match." \
              "Enter the probability of team A and team B winning its serve" \
              "and the number of games you'd like to simulate.")

def printOutput(winANormal, winBNormal, winARally, winBRally):
    print("Team A wins {0} games in normal match v. {1} games in rally " \
          "match".format(winANormal, winARally))
    print("Team B wins {0} games in normal match v. {1} games in rally " \
          "match".format(winBNormal, winBRally))

def main():
    printIntro()
    probA, probB, n = volleyball.getInput()
    winANormal, winBNormal = volleyball.simulate(probA, probB, n)
    winARally, winBRally = volleyball_rally.simulate(probA, probB, n)
    printOutput(winANormal, winBNormal, winARally, winBRally)

if __name__=='__main__': main()
