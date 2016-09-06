print("This program calculates the factorial of your input.")
n=eval(input("Give me a number: "))
x=1
for i in range(n,1,-1):
    x=x*i
print("Your number is ",x)
