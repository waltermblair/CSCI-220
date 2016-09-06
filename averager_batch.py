fileName=input("What is the name of the file? ")
file=open(fileName,"r")

##Using Python's special "for line in file" mechanism
##count=0
##mysum=0
##x=0
##
##for line in file:
##    x=eval(line)
##    mysum=mysum+x
##    count=count+1
##
##print(round((mysum/count),2))

##Typical for other programs without built-in "line" semantics
##count=0
##mysum=0
##line=file.readline()
##
##while line != "":
##    mysum=mysum+eval(line)
##    count=count+1
##    line=file.readline()
##
##print(round((mysum/count),2))

##Using Python and no longer assuming one number per line in file
count=0
mysum=0
line=file.readline()

while line != "":
    strList=line.split(',')
    intList=[]
    for i in range(len(strList)):
        intList.append(eval(strList[i]))
        mysum=mysum+intList[i]
        count=count+1
    line=file.readline()

print(round((mysum/count),2))
