def eiigh():
    print("Ee-igh, Ei-igh, Oh!")

def oldMacDonald():
    print("Old MacDonald had a farm, {0}!".format(eiigh()))

def sing(animal, sound):
    oldMacDonald()
    print("And on that farm he had a {0}, {1}!".format(animal,eiigh()))
    print("With a {0}, {0} here and a {0}, {0} there.".format(sound))
    print("Here a {0}, there a {0}, everywhere a {0}, {0}.".format(sound))
    oldMacDonald()

def main():
    sing("cow", "moo")
    print()
    sing("dog", "bark")
    print()
    sing("hen", "cluck")
    print()
    sing("pig", "oink")
    print()
    sing("dinosaur", "RAWWWR!!!")
main()
