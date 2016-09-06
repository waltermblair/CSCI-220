"""Program to find the student(s) with highest GPA from a tab-delimited
file of Name Hours QPoints."""

class Student:
    "Creates a student with given name, hours, qpoints from file"
    def __init__(self, name, hours, qpoints):
        self.name=name
        self.hours=float(hours)
        self.qpoints=float(qpoints)

    def getName(self):
        return self.name

    def getHours(self):
        return self.hours

    def getQPoints(self):
        return self.qpoints

    def gpa(self):
        return self.qpoints/self.hours

def makeStudent(infoStr):
    "Returns each student string as a list"
    name, hours, qpoints = infoStr.split("\t")
    return Student(name, hours, qpoints)

def main():

    "Asks for filename, opens file, and checks for highest gpa line by line."
    fileName=input("Name of tab-separated grade file: ")
    infile=open(fileName,"r")

    best=makeStudent(infile.readline())
    bestList=[best]

    for line in infile:
        s=makeStudent(line)
        if s.gpa() > best.gpa():
            best=s
            bestList[0]=best
        if s.gpa() == best.gpa() and s.getName() != best.getName():
            bestList.append(s)

    infile.close()

    for obj in bestList:
        print("The best student(s):", obj.getName())
        print("hours:",best.getHours())
        print("GPA:",best.gpa())
        print()

if __name__=="__main__": main()
