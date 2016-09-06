l=eval(input("Speed limit (mph): "))
s=eval(input("Your speed: "))

if s<=l:
    print("Speed up next time.")
else:
    if s<=90:
        f=50+5*(s-l)
    else:
        f=50+5*(s-l)+200

print("Your fine is $",f)
