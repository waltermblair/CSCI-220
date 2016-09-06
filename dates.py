print("This program converts a 5/5/1955 date to a nicer format")

#Collect a string of format MO/DY/YEAR
date_in=input("Write your date here in the format shown above\n")

#Split string to list
date_list=date_in.split("/")

#Convert month string in list to int (doesn't work if starts with 0, like 05)
x=eval(date_list[0])

#months list to index
months=["January", "February", "March", "April", "May", "June", "July",
        "August", "September", "October", "November", "December"]

#Select correct month and print date in format Month DY, YEAR
print(months[x-1],date_list[1]+",",date_list[2])
print("{0} {1}, {2}".format(months[x-1],date_list[1],date_list[2]))

month=str(months[x-1])
day=str(date_list[1])
year=str(date_list[2])

print(month, day+",", year)
print(month[0:4],day,year[-2:])

