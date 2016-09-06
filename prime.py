import math

##print("This program determines if your value is prime")
##x=eval(input("Enter a value: "))
##
##for i in range(2,x):
##    if x%i==0:
##        print("{0} is a factor".format(i))
##        break
    
##print("This program finds all prime numbers between 1 and your value")
##n=eval(input("Enter a value: "))
##
###For each value between 1 and the value entered:
##for i in range(n+1):
##    #For each number between 2 and number:
##    for j in range(2,i+1):
##        if j==i:
##            print(i)
##        if i%j==0: break

print("This program finds two prime numbers that add to equal you even value")

#Check that value is even
n=1
while n%2 != 0:
    n=eval(input("Enter an even integer: "))

#For each value between 1 and the value entered:
for i in range(n+1):
    #For each number between 2 and number:
    for j in range(2,i+1):
        if j==i:
            #j is a prime number. Subtract from n and see if that is prime:
            x=n-j
            for k in range(2,x+1):
                if k==x:
                    print(k,"+",j,"=",n)
                if x%k==0: break                    
        if i%j==0: break
