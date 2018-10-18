import math
from numpy import *
from numpy.linalg import *
import scipy.integrate as integrate


k = 8.99*(10**9)
cm = 10**-2
micro = 10**-6
electronCharge = 1.602*10**-19
electronMass = 9.11*10**-31
epi = 8.85 * 10**-12


#problem 1
R1 = 500
R2 = 1000
V1 = .1519
V2 = .2216
Rs = (R1*R2*(V2-V1))/(V1*R2-V2*R1)
print("Problem 1 part 1: " + str(Rs))
V = (V2*(R2+Rs)/R2)
print("Problem 1 part 2: " + str(V)) 
i = 2
c = 5
p = c*i
p2 = V2**2/R2 * 10**3
eff = p2/p * 100
print("Problem 1 part 3: " + str(eff))

#problem 2
R1 = 10
R2 = 10
R3 = 5
V1 = 6.1
V2 = 1
a = array([[R1+R3,-R3],
    [-R3, R2+R3]])
b = array([[-V1],
    [V2]])
i = inv(matrix(a)) * b
i1 = i.item(0,0)
i2 = i.item(1,0)
i3 = i1-i2
V3 = -i2*R2
print("Problem 2: " + str(V3))

#problem 3
R1 = 6
R2 = 12
V1 = 5
V2 = 10
V3 = 10
a = array([[2*R1+R2,-R2],
        [-R2, 2*R1+R2]])
b = array([[V2-V1],
        [V3-V2]])
i = inv(matrix(a)) * b
i1 = i.item(0,0)
i2 = i.item(1,0)
i1= i1
i3 = i1-i2
V = V2 - R2*i2
print("Problem 3 part 1: " + str(-i1))
print("Problem 3 part 2: " + str(i2))
print("Problem 3 part 3: " + str(i3))
print("Problem 3 part 4: " + str(V))

#problem 4
Vi = 11.7
Ai = 10.1
Rl = Vi/Ai
Af = 7
Vf = Af * Rl
Rb= .044
V = Vi*(Rl+Rb)/Rl
print("Problem 4 part 1: " + str(V))
V2 = Rl * Af
Vsp = Af*Vi/Ai 
I = (V-Vsp)/Rb - Af
print("Problem 4 part 2: " + str(I))

#problem 5
Rs = 19.6
R2 = 26
R1 = 10
Rx = (Rs*R2)/R1
print("Problem 5: " + str(Rx))

#problem 6 
t1 = .5
V = 95
VL = 73
t = t1/math.log(1/(1-VL/V),math.e)
F = .19 * 10**-6
R6 = t/F

print("problem 6: " + str(R6))


#problem 8
V = 110
I = 20
P = V *I
W = 300
L = P/W

print("Problem 8: " + str(L))

#problem 9
R = 494.5
C = 4*10**-6
Vb = 2.05
t = 2/1000
T = R * C
Vc = Vb*math.e**(-t/T)
print("Problem 9 part 2: "+ str(Vc))
Q = Vb * C
Edis = Vb*(Q/2)
print("Problem 9 part 3: "+ str(Edis)) 
Vc = Vb * (1-math.e**(-t/T))
print("Problem 9 part 4: "+str(Vc))

#problem 10
R = 935
C = 81*10**-6
T = R *C
V = 27
print("problem 10 part 1: " +str(T))
t = 1.11*10**-1
q = C * V* (1-math.e**(-t/T))
print("problem 10 part 2: " + str(q))
I = V/R * (math.e**(-t/T))
print("Problem 10 part 3: "+ str(I))
Vf = V*(1-math.e**(-t/T))
print("problem 10 part 4: " + str(Vf))

#problem 11
V = 12
R = 1.36 * 10**6
C = 1.89*10**-6
T = R *C
print("Problem 11 part 1: " + str(T))
Q = C * V
print("Problem 11 part 2: "+ str(Q)) 
Q = 16.9*10**-6
t = T* math.log(1/(1-Q/(C*V)),math.e)
print("Problme 11 part 3: " + str(t))

#problem 12
R1 = 10.1*10**3
R2 = 16.9*10**3
C = .42*10**-6
V = 19
t = 4.3/1000
R = R1+R2
T = R2*C
i =V/R
i2 = i*math.e**(-t/T)
print("Problem 12: " + str(i2))