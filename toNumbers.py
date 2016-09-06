print("This program converts a list of strings to a list of numbers")

strList=["3", "5", "7", "9"]

def toNumbers(strList):
    intList=[]
    for i in range(len(strList)):
        intList.append(int(strList[i]))
    return intList

def main():
    intList=toNumbers(strList)
    print(intList[0]+intList[1])
main()
