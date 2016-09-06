# File: chaos.py
# A simple program

def main():
    print("This program illustrates stuff!")
    x = eval(input("Enter a number between 0 and 1: "))
    y = eval(input("Enter another number between 0 and 1: "))
    n = eval(input("Enter number of iterations: "))
    print("{0:8}{1:8}\t{2:8}".format("index", x, y))
    print("-"*40)
    for i in range(n):
        x=3.9*x-3.9*x*x
        y=2*x-2*x*x
        print("{0:>5}\t{1:4.6f}\t{2:8.6f}".format(i, x, y))

main()
