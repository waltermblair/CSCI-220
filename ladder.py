import math
print("This program calculates required ladder length")
x=eval(input("Provide the height of roof: "))
theta=eval(input("Provide the ladder angle in degrees: "))
theta=math.pi/180*theta
l=x/math.sin(theta)
print("You need a ladder of length ",l)
