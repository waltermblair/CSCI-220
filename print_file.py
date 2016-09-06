print("This program prints contents of a file of your choice")

fname=input("Name of the file: ")
file=open(fname,"r")

#print whole thing
infile=file.read()
print(infile)

#print first 5 lines [:without extra \n]
for i in range(5):
    file_line=file.readline()
    print(file_line[:-1])

#print each line [:without extra \n]
for line in file:
    file_line=file.readline()
    print(file_line[:-1]

#write to a file
fileout=open(fname,"w")
print("This is the text of the file", file=fileout)
