print("This program adds up the first n natural numbers starting from 0.")
n=eval(input("How many numbers would you like to add, starting with 0?\n"))
x = 0
for i in range(n):
    x=x+i
print("Sum: ",x)
