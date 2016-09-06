print("This program determines how long it will take for your investment to double")

apr=eval(input("Interest rate (e.g. 7% = 7.0): "))

x=100
t=0

while x<200:
    x=x*(1+apr/100)
    t=t+1

print("Your investment will double in {0} years".format(t))
