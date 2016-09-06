print("This program sums a series of numbers")
n=eval(input("How many numbers do you want to add?"))
x=0
for i in range(n):
    x=x+eval(input("Type a number: "))
print("Sum: ",x)
