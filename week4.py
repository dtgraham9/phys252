import math
import numpy
import scipy.integrate as integrate

k = 8.99*(10**9)
cm = 10**-2
micro = 10**-6
electronCharge = 1.602*10**-19
electronMass = 9.11*10**-31
epi = 8.85 * 10**-12

#problem 1
#lam =  5.8*micro
#r=.514
#R=.7
#e = lam/(math.pi*r*2*epi)
#print(e)

#problem 2
#q1 = -7 * 10**-9
#q2 = -5.5 * 10**-12
#r1 = (3.5**2+1**2)**(1/2)
#r2 = (0**2+1**2)**(1/2)
#PEi = k*q1*q2/r1
#PEf = k*q1*q2/r2
#print(PEi)
#print(PEf)
#w = PEf-PEi
#print(w)

#problem 3

#problem 4
q = 3 * micro
d = (5/100)/2
r = (d**2 + d**2) **(1/2)
V = k*q/r + k*q/r
print(V)