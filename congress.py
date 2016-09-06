age=eval(input("Age: "))
n=eval(input("Years as citizen: "))

if age>=25:
    if age >=30:
        if n>=9:
            S="Eligible"
            H="Eligible"
        else:
            S="Not Eligible"
    elif n>=7:
        H="Eligible"
        S="Not Eligible"
    else:
        H="Not Eligible"
        S="Not Eligible"
else:
    H="Not Eligible"
    S="Not Eligible"

print("Senate: ",S,"\nHouse: ",H)

    
