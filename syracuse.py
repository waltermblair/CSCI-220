print("This program prints the Syracuse sequence from a starting value")

x=eval(input("Starting value: "))

while x > 1:
    if x%2==0: x=x/2
    else: x=3*x+1
    print(x)

