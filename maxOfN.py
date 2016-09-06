print("This program finds the max of any series of numbers you enter.")

n=eval(input("How many numbers are there to test? "))

max=eval(input("What is the first number you'd like to test? "))

for i in range(n-1):
    x=eval(input("Enter the next number: "))
    if max < x:
        max=x

print("The maximum value you entered is: ",max)
