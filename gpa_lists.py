from gpa import Student, makeStudent


def readStudents(filename):
    infile=open(filename,'r')
    students=[]
    for line in infile:
        students.append(makeStudent(line))
    infile.close()
    print(students)
    return students

def writeStudents(students, filename):
    outfile=open(filename,'w')
    for s in students:
        print("{0}\t{1}\t{2}".format(s.getName, s.getHours, s.getQPoints), file=outfile)
    outfile.close()

def main():
    filename=input("Name of data file: ")
    data=readStudents(filename)
    data.sort(key=Student.gpa)
    filename=input("Name of output file: ")
    writeStudents(data, filename)

if __name__=='__main__': main()
