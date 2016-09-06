print("This program counts the number of words in your file")

myfileName=input("Type your stupid ass file name below\n")
myfile=open(myfileName,"r")

mystring=myfile.read()

mylist=mystring.split()

word_count=len(mylist)
char_count=len(mystring)
line_count=mystring.count("\n")


print("Words: {0}".format(word_count))
print("Characters: {0}".format(char_count))
print("Lines: {0}".format(line_count))
