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

#problem 2
i = 320
a = .22/10000
J = i/a
carr = 8.49*10**28
V = J/(carr*electronCharge)
l = .77
t = l / V
print("Problem 2: " + str(t))

#problem 3
i = 55/1000
r = 2175
v = i * r
print("Problem 3: " + str(v))

#problem 4
v = 27
r = 6.2753/1000
i = v/r
print("Problem 4 part 1: " + str(i))
a = math.pi*(7/2/1000)**2
J=i/a
print("Problem 4 part 2: " + str(J))
l = 4.6
p = v * a/l
print("Problem 4 part 3: " + str(p))

#problem 5
v = 120
r = 9
p = v**2/r
print("Problem 5 part 1: " + str(p))
total = p*15/1000
cost = .0460
final = total * cost
print("Problem 5 part 2: " + str(final))

#problem 6
w = 100
v =120 
cost = .06
hr = 31 * 24 
total = w * hr/1000
price = total * cost
print("Problem 6 part 1: "+str(price))
i = w/v
r = v/i
print("Problem 6 part 2: " + str(r))
print("Problem 6 part 3: " + str(i))

#problem 7
w1 = 80/(1000*35*2)
w2 = 80/(1000*35*4)
w = 2*(w1+w2)
print("Problem 7: " + str(w))