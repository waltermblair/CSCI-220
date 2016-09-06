print("This program is the master acronymer")

mystring=input("Type the phrase you'd like to acronym\n")

def acronym(mystring):
    mylist=mystring.split()
    for i in mylist:
        print(i[0].upper(),end="")

def main():
    acronym(mystring)
main()
    
