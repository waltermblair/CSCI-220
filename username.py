print("This program generates a username for you!")

first=input("Enter your first name: ")
last=input("Enter your last name: ")

username=first[0]+last[0:7]

print("Your username is: ",username)
