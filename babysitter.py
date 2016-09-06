print("This program calculates the charge for the babysitter")
start=input("Start time (e.g. 21:45): ")
end=input("End time (e.g. 23:43): ")

startList=start.split(":")
endList=end.split(":")

startHour=int(startList[0])
startMin=int(startList[1])
endHour=int(endList[0])
endMin=int(endList[1])

s=startHour*60+startMin
e=endHour*60+endMin
dt=e-s

#9:00pm = 21:00*60 = 1260
#If ended before 9pm, cost=hours*$2.50
#if ended after 9pm, cost=hours before 9pm*$2.50 and hours after*$1.75

if e<1260:
    c=dt/60*2.5
else:
    c=(1260-s)/60*2.5+(e-1260)/60*1.75

print("You owe $",c)

