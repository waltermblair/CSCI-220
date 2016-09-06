print("This program calculates the fuel efficiency for a trip")

fileName=input("Name of file: ")
file=open(fileName,"r")

intList=[]
mileList=[]
gasList=[]

line=file.readline()

while line != "":
    entryList=line.split(",")
    for i in range(len(entryList)):
        intList.append(int(entryList[i]))
    line=file.readline()

for j in range(len(intList)):
    if j%2==0:
        mileList.append(intList[j])
    else:
        gasList.append(intList[j])

for i in range(len(mileList)):
    mpgLeg=(mileList[i]-mileList[i-1])/(gasList[i]-gasList[i-1])
    print("Leg {0}: {1}mpg".format(i,mpgLeg))

mpgTotal=(mileList[-1]-mileList[0])/gasList[-1]
print("Your total efficiency was {0}mpg".format(mpgTotal))
              
        
              
