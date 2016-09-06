x=eval(input("What is the test score? "))

if x>=90:
    g="A"
elif x>=80 and x<90:
    g="B"
elif x>=70 and x<80:
    g="C"
elif x>=60 and x<70:
    g="D"
else:
    g="F"

print("Your grade is ",g)
