print("This program gives you abbreviation of chosen month")

n=eval(input("Select a month, from 1-12: "))

#months=("JanFebMarAprMayJunJulAugSepOctNovDec")

#print("You have selected ",months[(n-1)*3:(n-1)*3+3])

months=["January", "February", "March", "April", "May", "June", "July",
        "August", "September", "October", "November", "December"]

print("You have selected ",months[n-1])

n2=eval(input("Which month would you like to rename? "))
name=input("What is the new name?")

months[n2-1]=name

print(months)
