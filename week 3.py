import math
import numpy

k = 8.99*(10**9)
cm = 10**-2
micro = 10**-6
electronCharge = 1.602*10**-19
electronMass = 9.11*10**-31

# problem 1
# e = 148 / (.87 * math.cos(math.radians(75)))
# print(e)

# problem 2
# z = 1.2 -1.2
# y = 5.1 -5.1
# x = -3.5
# m = 36/100
# m = m**2
# print(x*m)

#problem 3
m = .3/100
a = m**2
q = -6.1*micro
r = (m/2)**2
e = k*q/r
f=e*a
print(f)