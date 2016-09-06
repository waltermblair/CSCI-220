print("This program calculates the nth term of a Fibonacci sequence")
a=1
b=1
n=eval(input("Which term do you want to compute? "))

for i in range(n):
    a,b=a+b,a

print(b)
    
