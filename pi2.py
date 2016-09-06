import math
print("This program approximates the value of pi")
n=eval(input("How many terms in the infinite series do you want to sum?"))
x=0
for i in range(n):
   x=x+4/(1+4*i)-4/(3+4*i)
   a=math.pi-x
print(a)
print(x)
