def main():

    x1, x2, x3, x4=eval(input("Please enter four values: "))
    if x1>x2:
        if x1>x3:
            if x1>x4:
                max=x1
            else:
                max=x4
        else:
            if x3>x4:
                max=x3
            else:
                max=x4
    else:
        if x2>x3:
            if x2>x4:
                max=x2
            else:
                max=x4
        else:
            if x3>x4:
                max=x3
            else:
                max=x4
 
    print("The max is ",max)

main()
