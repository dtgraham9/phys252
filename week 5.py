import math
import numpy
import scipy.integrate as integrate

k = 8.99*(10**9)
cm = 10**-2
micro = 10**-6
electronCharge = 1.602*10**-19
electronMass = 9.11*10**-31
epi = 8.85 * 10**-12

#problem 2
f = 30*micro
v =90
q = f*v
print("problem 2: " +str(q))

#problem 3
r=9/100
s = 1.3/1000
a = math.pi*r**2
C = epi * a/s
print("problem 3 part1: " + str(C))
v =66
q = v*C
print("problem 3 part2: "+ str(q))

#problem 4
a = 26/1000
b = 28/1000
C = 4*math.pi*epi*(a*b)/(b-a)
print("Problem 4 part1: " str(C))