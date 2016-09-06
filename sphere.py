print("This program calculates V and SA of a sphere.")
import math

def volume(r):
    Vol=4.0/3.0*math.pi*r**3
    return Vol

def surfaceArea(r):
    SA=4*math.pi*r**2
    return SA

def main():
    r = eval(input("What is the radius?"))
    V = volume(r)
    SA = surfaceArea(r)
    print("Volume: ",V,"\nSurface Area: ",SA)
main()
