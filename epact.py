print("This program calculates the Gregorian epact.")
year=eval(input("What is the year?"))
C=year//100
epact=(8+(C//4)) - C + ((8*C+13)//25 + 11*(year%19))%30
print("The value of the epact is ",epact)
