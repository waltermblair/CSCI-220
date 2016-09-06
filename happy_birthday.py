def happy():
    print("Happy birthday to you!")

def sing(person):
    happy()
    happy()
    print("Happy birthday, dear {0}!".format(person))
    happy()
    
def main():
    sing("Walter")
    print()
    sing("Nora")
    print()
main()


