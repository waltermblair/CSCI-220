from random import randrange

def printIntro():
    print("This program simulates n games of blackjack and calculates" \
          "the probability that the dealer will bust.")

def getInput():
    n = eval(input("How many games do you want to simulate? "))
    print("--"*20)
    return n

def draw():
    card=randrange(1,13)
    if card>10:
        card=10
    return card

def hasAce(card):
    if card==1:
        return True

def game(i):
    dealerPoints=i
    while dealerPoints < 17:
        card=draw()
        if hasAce(card):
            if dealerPoints+10<21:
                dealerPoints=dealerPoints+10+card
            else: dealerPoints=dealerPoints+card
        else: dealerPoints=dealerPoints+card
    if dealerPoints>21: 
        return "dealerBusts"

def simulation(n):
    for i in range(1,11):
        dealerBusts=0
        for j in range(n):
            if game(i)=="dealerBusts":
                dealerBusts=dealerBusts+1
##            print("Dealer busts with starting value of {0} is: {1}" \
##                .format(i, dealerBusts))
##        print("--"*20)
        print("With first card of {0}, dealer has {1:0.2f} probability " \
              "of busting".format(i,dealerBusts/n))

##def printOutput(dealerBusts):
##    print("The dealer has a {0} probability of bust.".format(dealerBusts))

def main():
    printIntro()
    n = getInput()
    dealerBusts = simulation(n)
##    printOutput(dealerBusts/n)

if __name__=='__main__': main()
