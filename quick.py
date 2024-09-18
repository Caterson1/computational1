total = 0
rate = 0
t = 0
dt = .0000001

while t < 100:
    total += rate*dt
    t += dt
    rate+=dt
    print(t, "%")
print("$", total)