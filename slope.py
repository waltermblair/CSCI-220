import math
print("This program calculates slope in x,y plane and distance between two points")

try:
    x1, y1, x2, y2 = eval(input("Please enter the two points like x1,y1,x2,y2\n"))
    slope=(y2-y1)/(x2-x1)
    distance=math.sqrt((x2-x1)**2 + (y2-y1)**2)
    print("The slope is ",slope," and the distance is ",distance)
except:
    print("Vertical line, fool!")
