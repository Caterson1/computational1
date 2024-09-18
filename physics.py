from vectors import *
g = Vec(0, -9.81, 0)

class Air_density:
    def __init__(self, air_density):
        self.d = air_density

    def set(self, new_density):
        self.d = new_density

def drag(c, a, p, v):
    # print(f"{c}, {a}, {p}, {v}, drag force = {(c*a*p*mag(v)**2)*norm(v)}")
    return (c*a*p*mag(v)**2) * -norm(v)


def force_adder(forces):
    total_force = Vec()
    for force in forces:
        total_force += force
    return total_force