#Exercise 06 - Vinh Nguyen - vinhhnguyen313@gmail.com
#April 25, 2020.
#This program involves calculating trajectories for different starting
#conditions of a projectile

from numpy import arange


def dropit(A,vx0):
    x0 = 0
    t = 0.0
    dt = .1
    x,y=0,0
    g=32.17

    t = abs((2*A/g)**(1/2)) if abs((2*A/g)**(1/2))<=30 else 30
    x = vx0*t
    y = A - 1/2*(32.17)*t**2
    return [t,x,y]

print("Exercise 06 - Vinh Nguyen - vinhhnguyen313@gmail.com\n\
April 25, 2020.")
print("This program simulates a falling object released from \
an airplane over and over again with many different starting conditions.")
print("-------------")

A, vx0 = map(float,input("Please enter the altitude (in feet) and the airspeed \
of the aircraft when the object is dropped, in knots (nautical miles per hour): ").split(","))


print("")
print("Your altitude is "+ str(A))
print("Your aircraft's airspeed is "+ str(vx0)+"\n")

print("TABLE OF RESULTS:")
print("%-15s %-18s %-15s %-15s" % ("Altitude (ft)","Airspeed (knots)","Time (s)","Position (ft,ft)"))

altrange = arange(A+100,A-100-200/8, -200/8) if A>100 else arange(A+100,-(A+100)/8, -(A+100)/8)

for i in altrange:
    for j in arange(vx0-10, vx0+15, 20/4):
        result = dropit(i,j*6076/60/60)
        print("%-15.2f %-18.2f %-15.2f (%3.2f, %3.2f)" % (i, j, result[0],result[1],result[2]))

