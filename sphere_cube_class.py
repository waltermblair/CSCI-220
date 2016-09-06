#sphere_class.py
"This is a solid sphere class"

import math

class Sphere:

    def __init__(self, radius):
        self.r=radius
        self.SA=4*math.pi*radius**2
        self.V=4/3*math.pi*radius**3

    def getRadius(self):
        return self.r

    def surfaceArea(self):
        return self.SA

    def volume(self):
        return self.V

class Cube:

    def __init__(self, l):
        self.l=l
        self.SA=l**2*6
        self.V=l**3

    def surfaceArea(self):
        return self.SA

    def volume(self):
        return self.V

def main():
    t=input("Analyze a cube or a sphere? ")
    if t == "sphere":
        r=eval(input("What is radius of your sphere? "))
        mysphere=Sphere(r)
        print("Radius = ",mysphere.getRadius())
        print("Surface Area = ",mysphere.surfaceArea())
        print("Volume = ",mysphere.volume())
    else:
        l=eval(input("What is length of your cube? "))
        mycube=Cube(l)
        print("Surface Area = ",mycube.surfaceArea())
        print("Volume = ",mycube.volume())

main()
