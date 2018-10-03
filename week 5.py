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
r = 5
q1 = 4 * micro
q2 = q1 * 5
print("Problem 1 part 1: " + str(q2))

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
print("Problem 4 part1: " + str(C))
d = b-a
a = C *d/epi
print("Problem 4 part2: "+ str(a))

#problem 5
c = 3*21 * micro
v = 3600
q = c*v
print("Problem 5: " + str(q))

#problem 6
c3 = 2.1 * micro
c2 = 4.2 * micro
c1 = 12 * micro
ce = 1/((1/c2)+(1/c1))
ct = ce+c3
print("Problem 6: " + str(ct))

#problem 7
c1 = 2.4 * micro
c2 = 6.7 *micro
ct = c1+c2
v = 290
q1 = v * c1
q2 = v * c2
q = q1+q2
e = q*v
u=.5*ct*v**2
print("Problem 7: "+ str(u))

#problem 8
c = 238*10**-12
a = .035
d = epi*a/c
print("problem 8 part 1: " + str(d))
k = 4.6
c = c * k
print("problem 8 part 2: " + str(c))