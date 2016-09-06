import math
print("This function calculates area of triangle")
x,y,z=eval(input("Provide the three sides of the triangle like 'x,y,z'\n"))
s=(x+y+z)/2.0
area=math.sqrt(s*(s-x)*(s-y)*(s-z))
print("Area: ",area)
