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
    
    def addLetterGrade(self, letterGrade, creds):
        self.hours=self.hours+float(creds)
        if letterGrade=="A":
            gradePoints=4.0
        elif letterGrade=="A-":
            gradePoints=3.7
        elif letterGrade=="B+":
            gradePoints=3.3
        elif letterGrade=="B":
            gradePoints=3.0
        elif letterGrade=="B-":
            gradePoints=2.7
        elif letterGrade=="C+":
            gradePoints=2.3
        elif letterGrade=="C":
            gradePoints=2.0
        elif letterGrade=="C-":
            gradePoints=1.7
        elif letterGrade=="D+":
            gradePoints=1.3
        elif letterGrade=="D":
            gradePoints=1.0
        elif letterGrade=="D-":
            gradePoints=0.7
        else: gradePoints=0.0
        self.qpoints=self.qpoints+gradePoints*creds

    def addGrade(self, gradePoint, creds):
        self.hours=self.hours+float(creds)
        self.qpoints=self.qpoints+gradePoints*creds

def main():
    name=input("Name of new student (e.g. Blair, Walter): ")
    name=Student(name, 0, 0)
    n=eval(input("How many courses would you like to add for {0}? " \
                 .format(name.getName())))
    for i in range(n):
        creds=eval(input("Credits for class (e.g. 3): "))
        grade=input("Grade earned (e.g. B+): ")
        name.addLetterGrade(grade, creds)
    print(name.gpa())

main()
