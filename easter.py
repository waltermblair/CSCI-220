print("This program gives you the date of Easter between 1900-2099")

year=eval(input("Year: "))

if year<1900 or year>2099:
    print("Year out of range")

else:
    a=year%19
    b=year%4
    c=year%7
    d=(19*a+24)%30
    e=(2*b+4*c+6*d+5)%7
    if year==1954 or year==1981 or year==2049 or year==2076:
        day=22+d+e-7
    else:
        day=22+d+e
    if day>31:
        dayApr=day%31
        print("Easter will be on April {0}, {1}.".format(dayApr,year))
    else:
        print("Easter will be on March {0}, {1}.".format(day,year))
    
