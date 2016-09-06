import math

def getInput():
    angle=eval(input("Launch angle in degrees: "))
    vel=eval(input("Initial velocity in m/s: "))
    h0=eval(input("Initial height in m: "))
    time=eval(input("Time interval between position calculations: "))
    return angle, vel, h0, time

def getXYComponents(vel, angle):
    theta=math.radians(angle)
    xvel=vel*math.cos(theta)
    yvel=vel*math.sin(theta)
    return xvel, yvel

def updateCannonball(time, xpos, ypos, xvel, yvel):
    ymax=0
    while ypos>=0:
        xpos=xpos+time*xvel
        yvel1=yvel-time*9.8
        ypos=ypos+time*(yvel+yvel1)/2.0
        yvel=yvel1
        if ypos>ymax:
            ymax=ypos
    return xpos, ypos, xvel, ymax

def main():
    angle, vel, h0, time = getInput()
    xpos, ypos = 0.0, h0
    xvel, yvel = getXYComponents(vel, angle)
    xpos, ypos, xvel, ymax = updateCannonball(time, xpos, ypos, xvel, yvel)
    print("\nDistance traveled: {0:0.1f} meters.".format(xpos))
    print("Height reached: {0:0.1f} meters.".format(ymax))

if __name__=="__main__": main()
