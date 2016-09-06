print("This program counts your loose change")
print("Please enter the number of each coin")
quarters=eval(input("Quarters: "))
dimes=eval(input("Dimes: "))
nickels=eval(input("Nickels: "))
pennies=eval(input("Pennies: "))

total = quarters*25+dimes*10+nickels*5+pennies*1

print("You have ${0:0.2f}".format(total/100)+".")
print("More precisely, you have ${0:0}.{1:0>2}"
      .format(total//100,total%100))

#More fun with format specifiers:

print("My name is {0} {1}".format("Walter", "Blair"))
print("My age is {0:>20.5f}".format(29.0))
print("My age is {0:<20.5f}".format(29.0))
print("My age is {0:^20.5f}".format(29.0))
