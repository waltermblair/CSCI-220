#This program takes a file of names and outputs a file of generated usernames

def main():
    #open the name file for reading and open a new username file for writing
    input_file=input("What is the name of the file? ")
    names_file=open(input_file,"r")
    output_file=input("What is the name of your new username file? ")
    username_file=open(output_file,"w")

    #grab each name, generate username, and write username for each line
    for line in names_file:
        first, last = names_file.split()
        uname=(first[0].last[0:7]).lower()
        print(uname, file=username_file)

    names_file.close()
    username_file.close()

    print("Usernames have been written to",output_file)

main()
