print("This program computes the sum of squares of numbers read from a file of your choice")

fileName=input("What is the name of your file?\n")
file=open(fileName,"r")

def toNumbers(file):
    #Read file to a list of strings
    strList=file.readlines()

    #Truncate strList by removing all the \n's (including blank last line)!
    #convert strList to intList using int()
    intList=[]
    for i in range(len(strList)-1):
        intList.append(int(strList[i][:-1]))
    return intList

def squareEach(nums):
    for i in range(len(nums)):
        nums[i]=nums[i]**2
    return nums

def sumList(nums):
    mysum=0
    for i in range(len(nums)):
        mysum=mysum+nums[i]
    return mysum

def main():
    intList=toNumbers(file)
    print(intList)
    mysum=sumList(squareEach(intList))
    print("Sum = {0}".format(mysum))
main()
