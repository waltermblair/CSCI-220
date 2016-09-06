print("This program pretends like scores.txt are daily temperatures and" \
      "computes the number of heating days and cooling days.")

fileName=input("Name of file: ")
file=open(fileName,"r")

line=file.readline()

strList=[]
intList=[]
countH=0
countC=0

while line != "":
    strList=line.split(",")
    for i in range(len(strList)):
        intList.append(int(strList[i]))
    line=file.readline()

for i in range(len(intList)):
    if intList[i]<6:
        countH=countH+1
    if intList[i]>8:
        countC=countC+1

print("Heating days: {0}. Cooling days: {1}".format(countH, countC))
