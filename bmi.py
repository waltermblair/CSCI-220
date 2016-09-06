w=eval(input("Weight: "))
h=eval(input("Height: "))

bmi=w*720/h**2

if bmi<=25 and bmi>=19:
    r="healthy"
elif bmi > 25:
    r="overweight"
else:
    r="underweight"

print("You are ",r)
