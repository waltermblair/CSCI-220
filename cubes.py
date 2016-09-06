print("This program adds cubes of first n natural numbers")

n=eval(input("How many numbers do you want to input, starting with 0? "))

def sumN(n):
    x=0
    for i in range(n):
        x=x+i
    return x

def sumNCubes(n):
    x=0
    for i in range(n):
        x=x+i**3
    return x

def main():
    print("Sum: {0}, Cubes: {1}".format(sumN(n),sumNCubes(n)))
main()
