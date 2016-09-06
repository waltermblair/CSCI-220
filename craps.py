from random import randrange

def printIntro():
    print("This program runs a craps simulation of n games.")

def getInput():
    n = eval(input("How many games do you want to simulate? "))
    return n

def roll():
    d1 = randrange(1,6)
    d2 = randrange(1,6)
    return d1+d2

def game():
    firstRoll=roll()
    if firstRoll in {2, 3, 12}:
        return "loss"
    elif firstRoll in {7, 11}:
        return "win"
    else:
        nextRoll=roll()
        if nextRoll==firstRoll:
            return "win"
        elif nextRoll==7:
            return "loss"
        else:
            while nextRoll!=7 and nextRoll!=firstRoll:
                nextRoll=roll()
                if nextRoll==7:
                    return "loss"
                elif nextRoll==firstRoll:
                    return "win"
                else: nextRoll=roll()
            

def simulate(n):
    win=loss=0
    for i in range(n):
        if game() == "win":
            win=win+1
        else:
            loss=loss+1
    return win, loss

def printOutput(win,loss, n):
    print("You won {0} games and lost {1} games.".format(win, loss))
    print("the probability of winning is {0}".format(win/n))

def main():
    printIntro()
    n = getInput()
    win, loss = simulate(n)
    printOutput(win, loss, n)

if __name__=='__main__': main()
