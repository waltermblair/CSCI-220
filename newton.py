import math
print("This program implements Newton's method to approximate a square root")
x=eval(input("For what number do you want to approximate the square root: "))

def newton(x):   
    g=x/2
    n=eval(input("How many times do you want to iterate: "))
    for i in range(n):
        g=(g+x/g)/2
    return g

def main():
    print(newton(x))
main()
