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
#lam =  -5.8*micro
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
#a = 1/100 * 1/100
#q1 = 2.2*micro
#q2 = q1
#surf1 = q1
#surf2 = -q2
#E1 = surf1/(a*epi)
#print(E1)

#problem 4
#q = 3 * micro
#d = (5/100)/2
#r = (d**2 + d**2) **(1/2)
#V = k*q/r + k*q/r
#print(V)
#U = V*q
#print(U)
#PE = k*q*q/r + k*q*q/r + k*q*q/(d*2)
#print(PE)

#problem 5
#surf = 2 * 10**-7
#v = 50
#x = v*2*epi/surf
#print(x)

#problem 6
#d1 = 2.16
#d2 = 1.2
#q = 5 *micro
#V1 = k*q/d1
#V2 = k*q/d2
#V = V1-V2
#print(V)

#problem 7
#debyte = 3.34*10**-30
#dipole = 1.47*debyte
#d = 46 * 10**-9
#v = k*dipole*d/d**3
#print(v)

#problem 8
#xi= 0
#xf = 5.8
#def integrand(x):
#    return 2.3*x**2
#V = integrate.quad(integrand,xi, xf)
#print(V)

#problem 9
#dg = .88
#Lh = 1
#lam = 6*10**-3
#Q = lam/(2*Lh)
#r = (dg**2+Lh**2)**(1/2)
#ang = math.atan(dg/Lh)
#V = 2*k*lam * math.log((Lh+ r)/dg)
#print(V)
#print(V-V)

#problem 10
#V = 1300
#x = 9.9/100
#E = -1300*2*x
#print(E)
