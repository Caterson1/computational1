from ball import *

wind_speed = Vec()

class Pumpkin:
    def __init__(self, angle_degrees: float, wind_speed):
        self.initangle = angle_degrees
        initialy = math.sin(math.radians(angle_degrees))*30.48
        print(initialy)
        self.obj = ball_from_angle(Vec(0, initialy), 330, angle_degrees, g, 4.2, 0.125, wind_speed, (235, 235, 80))
        self.obj.drag_override((.125 ** 2) * math.pi, 0.3)
        self.prevy = 0
        self.t = 0
        self.printed = False

    def pumpstep(self, dt):
        self.t += dt
        if self.prevy <= self.obj.pos.y:
            self.prevy = self.obj.pos.y
        if self.obj.pos.y <= 0:
            self.obj.stop()
            if self.printed == False:
                print(f"pumpkin with initial angle: {self.initangle} degrees went {self.obj.pos.x}m after {self.t} seconds."
                      f" \n it reached a maximum height of {self.prevy}m")
                self.printed = True
        self.obj.step(dt)


def multistepper(imput_list):
    for i in imput_list:
        i.step()