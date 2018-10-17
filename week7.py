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

print("Problem 4 part 2: " + str(Am))

#problem 5
print("Problem 5: " + str())

#problem 6 
print("problem 6: " + str())

#problem 7 
print("Problem 7: " + str())

#problem 8
print("Problem 8: " + str())

#problem 9
print("Problem 9 part 1: "+str())
print("Problem 9 part 2: "+ str())
print("Problem 9 part 3: "+ str()) 
print("Problem 9 part 4: "+str())

#problem 10
print("problem 10 part 1: " +str())
print("problem 10 part 2: " + str())
print("Problem 10 part 3: "+ str())
print("problem 10 part 4: " + str())

#problem 11
print("Problem 11 part 1: " + str())
print("Problem 11 part 2: "+ str()) 
print("Problme 11 part 3: " + str())

#problem 12
print("Problem 12: " + str())