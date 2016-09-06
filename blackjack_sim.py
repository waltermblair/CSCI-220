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

def game():
    dealerPoints=0
    while dealerPoints < 17:
        card=draw()
        print(card)
        if hasAce(card):
            if dealerPoints+10<21:
                dealerPoints=dealerPoints+10+card
            else: dealerPoints=dealerPoints+card
        else: dealerPoints=dealerPoints+card
        
    print("Dealer score is: ",dealerPoints)
    print("--"*20)
    if dealerPoints>21: 
        return "dealerBusts"

def simulation(n):
    dealerBusts=0
    for i in range(n):
        if game()=="dealerBusts":
            dealerBusts=dealerBusts+1
    return dealerBusts

def printOutput(dealerBusts):
    print("The dealer has a {0} probability of bust.".format(dealerBusts))

def main():
    printIntro()
    n = getInput()
    dealerBusts = simulation(n)
    printOutput(dealerBusts/n)

if __name__=='__main__': main()
