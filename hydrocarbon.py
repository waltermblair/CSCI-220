print("This program calculates the molecular weight of a hydrocarbon")
h=eval(input("How many hydrogen atoms?"))
c=eval(input("How many carbon atoms?"))
o=eval(input("How many oxygen atoms?"))
w=h*1.0079+c*12.011+o*15.9994
print("The weight is ",w," grams/mole")
