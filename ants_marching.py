def ants(n):
    print("The ants go marching {0} by {0}, hurrah! hurrah!".format(n))

def marching(stops_to, n):
    print("The ants go marching {0} by {0},".format(n))
    print("The little one stops to {0},".format(stops_to))
    print("And they all go marching down...")
    print("In the ground...\nTo get out...\nOf the rain.\nBoom! Boom! Boom!")
    print()

def verse(stops_to, n):
    ants(n)
    ants(n)
    marching(stops_to, n)

def main():
    verse("suck his thumb", "one")
    verse("tie his shoe", "two")
    verse("take a pee", "three")
    verse("hit the floor", "four")
    verse("do the jive", "five")
    verse("get her kicks", "six")
    verse("talk to the dev", "sev")
    verse("fill his plate", "eight")
    verse("drink some wine", "nine")
    verse("drink all the gin", "ten")
main()
