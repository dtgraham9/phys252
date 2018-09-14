import math
import numpy
import scipy.integrate as integrate

k = 8.99*(10**9)
cm = 10**-2
micro = 10**-6
electronCharge = 1.602*10**-19
electronMass = 9.11*10**-31
epi = 8.85 * 10**-12

# problem 1
# e = 148 / (.87 * math.cos(math.radians(75)))
# print(e)

# prblem 2
# z = 1.2 -1.2
# y = 5.1 -5.1
# x = -3.5
# m = 36/100
# m = m**2
# print(x*m)

#problem 3
# m = .3/100
# a = m**2
#q = -3.6*micro
#f = q/epi
#f = f * 1/6
#print(f)

# problem 4
#side = 2.5
#def integrand1(x):
#    return 3.43*x + 4.61
#result = integrate.quad(integrand1, 0,side) 
#result1 = (3.43*0 + 4.61 -(3.43*-side+4.61)) * side**2 * epi
#print(result1)

#problem 5
#r = 1.24/2
#q=3.7*micro
#surfaceCharge=q/(4*math.pi*r**2)
#print(surfaceCharge)
#field = surfaceCharge/(epi)
#print(field)

#problem 6
#m = 9.8 * 4.2/1000
#q = 8*10**-8
#hforce= math.tan(math.radians(26))*m
#field = hforce/q
#surfaceCharge = field *2 *epi
#print(surfaceCharge)

#problem 7
#sq = -6*micro
#e = 150 * electronCharge
#d = (e*epi)/(electronCharge*sq)
#print(d)

#problem 8
a = 1.9/1000
r = 1.90/1000
p = 5.1*10**-15
flux = p/(epi) * a
print(flux)


#problem 9
#r = 7.3/100
#a=14.6/100
#q = 5*micro
#field = q/(4*math.pi*epi*a**3)*r
#print(field)
#r=25.6/100
#field = q/(4*math.pi*epi*r**2)
#print(field)

#problem 10
#r = .1
#surfaceflat = math.pi*r**2
#field = 6.5*10**6
#print(-surfaceflat*field)
#surfaceHemi= 2*math.pi*r**2
#print(field*surfaceHemi/2)