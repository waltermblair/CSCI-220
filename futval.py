#APR

print("This program calculates the future value")
print("of a n-year investment...")

x=eval(input("Enter value of your annual investment: "))
apr=eval(input("Enter your annual percentage rate, e.g. 0.07: "))
n=eval(input("How many times is interest compounded each year? "))

for i in range(10*n):
    x = x*(1+apr/n)

print("In 10 years, you will have",x)
