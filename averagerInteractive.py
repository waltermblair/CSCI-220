print("This program averages any number of values entered by user.")

x=input("Enter a value: ")
count=0
mysum=0.0

while x != "":
    mysum=mysum+eval(x)
    count=count+1
    x=input("Enter next value (Press Enter to quit): ")
print(mysum/(count))
