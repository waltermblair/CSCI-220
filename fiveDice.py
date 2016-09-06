from random import randrange

def printIntro():
    print("This program estimates probability of rolling five-of-a-kind with" \
          "all 5 dice in a single roll")

def getInput():
    n=eval(input("How many rolls do you want to simulate? "))
    return n

def roll():
    rollList=[]
    for i in range(6):
        rollList.append(randrange(1,5))
    if rollList[1]==rollList[2]==rollList[3]==rollList[4]==rollList[5]:
        return "match"

def simulate(n):
    matches=0
    for i in range(n):
        if roll()=="match":
            matches=matches+1
    return matches

def printOutput(matches, n):
    print("The probability of a five-of-a-kind in one roll is {0}" \
          .format(matches/n))

def main():
    printIntro()
    n=getInput()
    matches=simulate(n)
    printOutput(matches, n)

if __name__=='__main__':main()
