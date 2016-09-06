from random import randrange

def printIntro():
    print("This program calculates your random walk of n steps.")

def getInput():
    n=eval(input("How many steps will you take? "))
    return n

def simulate(n):
    x=0
    y=0
    for i in range(n):
        direction=randrange(1,5)
        if direction==1:
            y=y+1
        elif direction==2:
            x=x+1
        elif direction==3:
            y=y-1
        else: x=x-1
    return x, y

def printOutput(distance, n):
    print("You will be {0} steps away from origin after {1} steps" \
          .format(distance, n))

def main():
    printIntro()
    n=getInput()
    x, y =simulate(n)
    printOutput(abs(x)+abs(y), n)

if __name__=='__main__': main()
