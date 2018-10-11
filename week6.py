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
i = 4.5*10**-12
a = math.pi*(2.9/1000/2)**2
J = i/a
carr = 8.49*10**28
V = J/(carr*electronCharge)
print("Problem 1 part 1: " + str(J))
print("Problem 1 part 2: " + str(V))