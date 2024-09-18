from vectors import *

A = Vec(3, 4, -2)

B = Vec(-2, 5, 0)

C = Vec(-4, 0, 7)

D = Vec(0, 0, 0)


print(3*A - 2*B)

print(mag(3*A - 2*B))

print(3.24*B -1.86*A)

print(mag(3.24*B -1.86*A))

print(A + B + C + D)

print(mag(A + B + C + D))

print(dot(A,(2.5*B - 3*C)))


print((2*C + 3*D).cross(-1*A + B))

print(mag((2*C + 3*D).cross(-1*A + B)))


A = A + B
print(A)

C = 1.5*C
print(C)

A = Vec(3, 4, -2)

B = Vec(-2, 5, 0)

C = Vec(-4, 0, 7)

D = Vec(0, 0, 0)


for x in range(1000):
    D = D + 0.001*A
    x += 1
print(D)

A = (3, 4, -2)

B = Vec(-2, 5, 0)

C = Vec(-4, 0, 7)

D = Vec(0, 0, 0)

for x in range(1000):
    B = B + 0.001*C
    x+=1
print(B)

A = Vec(3, 4, -2)

B = Vec(-2, 5, 0)

C = Vec(-4, 0, 7)

D = Vec(0, 0, 0)


# Add to Vector “B” a vector in the direction of “A” that has a magnitude of ten.
print(B+(10*A.norm()))

# Add to Vector “C” a vector in the direction of “A” that has a magnitude of 6.
print(C+(6*A.norm()))
