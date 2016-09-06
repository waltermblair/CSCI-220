#APR

print("This program calculates the future value")
print("of a n-year investment...")

x=eval(input("Enter value of your annual investment: "))
apr=eval(input("Enter your annual percentage rate, e.g. 0.07: "))
n=eval(input("How many years do you want to forecast?"))

print("{0:4}{1:>8}".format("Year","Value"))
print("-"*16)
for i in range(1,n+1):
    x = x*(1+apr)
    print("{0:>4}  ${1:>8.2f}".format(i,x))

