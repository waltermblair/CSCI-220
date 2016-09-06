print("This program tells you if your year is a leap year.")

year=eval(input("Year: "))

if year%4==0:
    if year%400!=0:
        print("Nope!")
    else:
        print("Leap Year!")
else:
    print("Nope!")
