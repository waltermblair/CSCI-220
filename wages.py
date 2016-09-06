print("This program calculates weekly wages")

x=eval(input("Hourly wage: "))
n=eval(input("# of hours worked: "))

if n-40>0:
    wages=40*x+(n-40)*1.5*x
else:
    wages=n*x

print("Your wages are $",wages)
