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
lam =  5.8*micro
r=.514
R=.7
e = lam/(math.pi*r*2*epi)
print(e)