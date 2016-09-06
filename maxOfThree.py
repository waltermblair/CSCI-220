def main():
    x1, x2, x3 = eval(input("Write three numbers: "))

    if x1>x2 and x1>x3:
        max=x1

    elif x2>x1 and x2>x3:
        max=x2

    elif x3>x1 and x3>x2:
        max=x3

    else:
        max="impossible to determine, try again."

    print("The max value is", max)

main()
