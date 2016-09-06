print("This program counts the number of words you type")

mystring=input("Type your stupid ass words below\n")
mylist=mystring.split()

length=len(mylist)

word_length=0
for w in mylist:
    word_length=word_length+len(w)
avg_word_length=word_length/length

print(length)
print(avg_word_length)
