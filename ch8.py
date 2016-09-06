#3a
i=1
sum=0
n=eval(input("Add to what value?"))
while i<=n:
    sum=sum+i
    i=i+1
print(sum)

#3b
i=1
sum=0
n=eval(input("Add odd numbers to what value?"))
while i<=n:
    sum=sum+i
    i=i+2
print(sum)
    
#3c
sum=0
x=eval(input("Enter first value to add: "))
while x!=999:
    sum=sum+x
    x=eval(input("Next value (Enter 999 to exit): "))
print(sum)

#3d
import math
n=eval(input("Enter a number"))
count=0
while math.log(n,2)>1:
    n=n//2
    count=count+1
print(count)
