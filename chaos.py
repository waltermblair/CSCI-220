# File: chaos.py
# A simple program

def main():
    print("This program illustrates stuff!")
    x = eval(input("Enter a number between 0 and 1: "))
    y = eval(input("Enter another number between 0 and 1: "))
    for i in range(10):
        x=3.9*x-3.9*x*x
        y=2*x-2*x*x
        print("Your answers are",x,"and",y)

main()
