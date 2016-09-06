import math
print("This program calculates cost/square inch of your pizza.")
d=eval(input("What is diameter in inches?"))
x=eval(input("What is cost in dollars?"))

def area(d):
    area=math.pi*(d/2)**2
    return area

def cost(d, x):
    cost=x/area(d)
    return cost

def main():
    print("The cost per square inch is $",round(cost(d, x),2))
main()
