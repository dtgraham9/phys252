import math
import numpy

from scipy.integrate import quad
k = 8.99*(10**9)
cm = 10**-2
micro = 10**-6
electronCharge = 1.602*10**-19
electronMass = 9.11*10**-31

# charge2 *=micro;
# length = math.cos((math.asin(2.1/110)))*110
# difference = 110-length
# forcePotential = difference*cm * 9.8 * (10/1000)
# q = ((forcePotential*(4.2*cm)**2)/k)**(1/2)
# print(q)
# print(((((10/1000)*9.8*(4.2/100)**3)/(k*2*1.1))**(1/2)))

# q12 = 5.90*electronCharge
# q3 = 2.90*electronCharge
# q4 = -11.6*electronCharge
# distance = 4.8 * micro
# electric1 = k*q3/distance**2
# electric2 = k*q4/(2*distance)**2
# print(electric1 + electric2)

# q = 7*micro
# distance = .1
# field = 2*k*q/(math.pi*distance**2)
# print(2*field)

# q = 3*micro
# lamda = q/.42
# angle = math.atan(.21/.336)
# e = ((k*lamda) / .336) * abs(math.sin(angle)-math.sin(-angle))
# print(e)

# p = 2*electronCharge * 0.671 * 10**-9
# t = p*3.77*10**6
# print(t)

# ef = 442
# volume = math.pi * 4/3 * (1.4/2*micro)**3
# force = volume * 1000 * 9.8
# q = force/ef
# electrons = q/electronCharge
# print(electrons)
plate = 3.5*10**3
length = .04
apart = .02
velocity = 6.5*10**6 * math.sin(math.pi/4)
accel = plate*electronCharge/electronMass
coeffx = [velocity, -length]
coeffy = [-.5*accel, velocity, -apart]
y = (numpy.roots(coeffy))
x = (numpy.roots(coeffx))
print(x > y)
print(y)
print(x)
print(y[0])
print(y*velocity)
print(velocity*x - .5*accel*(x**2))

# y= 2.208*10**-8
# x = 1.3437*10**-8
# distance = 50 * cm
# force1 = 1.0098
# force2 = .0979
# diagonal = (distance**2 + distance**2);
# force1 = ((k*charge1 * charge1)/(distance**2));
# forcex = force1 * cos(radians(30));
# forcey = force1 * sin(radians(30));
# forcey += force1;
# netforce = (forcex**2 + forcey**2)**(1/2);
# force2 = (k*charge1 * charge2)/(distance**2);
# netforce = force1 - force2;
# distance = (k*(abs(charge1)*abs(charge2))/force)**(1/2);
# product = -((force1*(distance**2))/k)
# print(product)
# q2=product/q1
# sum = q1+q2
# sum = q1+product/q1
# sum*q1=q1^2+product
# 0=q1^2-sum*q1+product
# sum = ((force2*4*(distance**2))/k)**(1/2)
# coeff = [1, -sum, product]
# q1 = (np.roots(coeff))
# print(np.roots(coeff))
# q2 = product/q1[0]
# print(str(q1[0])+"\n"+str(q2))
# print(q1[0] > abs(q2))
