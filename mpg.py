print("This program calculates the fuel efficiency for a trip")

n=eval(input("Starting odometer reading: "))
entryStr="{0}, {1}".format(n, 0)
intList=[]
mileList=[]
gasList=[]

while entryStr != "":
    entryList=entryStr.split(",")
    for i in range(len(entryList)):
        intList.append(int(entryList[i]))
    entryStr=input("New odometer reading, " \
                   "Gallons of gas used (Press Enter when done): ")

for j in range(len(intList)):
    if j%2==0:
        mileList.append(intList[j])
    else:
        gasList.append(intList[j])

for i in range(len(mileList)):
    mpgLeg=(mileList[i]-n)/(gasList[i]-gasList[i-1])
    print("Leg {0}: {1}mpg".format(i,mpgLeg))

mpgTotal=(mileList[-1]-n)/gasList[-1]
print("Your total efficiency was {0}mpg".format(mpgTotal))
              
        
              
