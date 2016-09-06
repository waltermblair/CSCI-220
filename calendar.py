print("This program tells you if your calendar date is valid.")

strdate=input("Type your date like 05/01/1965\n")

strList=strdate.split("/")

intList=[]
for i in range(len(strList)):
    intList.append(int(strList[i]))
    
def leapYear(year):
    if year%4==0:
        if year%400!=0:
            return False
        else:
            return True
    else:
        return False

def validate(intList):
    if intList[0] in {1, 3, 5, 7, 8, 10, 12}:
        if intList[1]<=31:
            print("Date is valid")
            return True
        else:
            print("Date is invalid")
            return False

    if intList[0] in {4,6,9,11}:
        if intList[1]<=30:
            print("Date is valid")
            return True
        else:
            print("Date is invalid")
            return False

    if intList[0] == 2:
        if leapYear(intList[2]):
            if intList[1]<=29:
                print("Date is valid")
                return True
            else:
                print("Date is invalid")
                return False
        else:
            if intList[1]<=28:
                print("Date is valid")
                return True
            else:
                print("Date is invalid")
                return False
    
def main():
    if validate(intList):
        dayNum=31*(intList[0]-1)+intList[1]
        if intList[0] in {3, 4, 5, 6, 7, 8, 9, 10, 11, 12}:
            if leapYear(intList[2]):
                dayNum=dayNum+1        
        else:
            dayNum=dayNum-(4*intList[0]+23)//10
        print("Day: ",dayNum)
main()
