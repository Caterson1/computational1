import random

import pygame as p
import sys  # most commonly used to turn the interpreter off (shut down your game)
from pumkin_class import *

# Constants - sets the size of the window
window_bounds = WIDTH, HEIGHT, scale = 600, 600, .5
origin = x0, y0 = WIDTH/2, HEIGHT-HEIGHT/2  # This is the new origin
dt = 0.001
oldv = 0
oldpos = 0
printed = False
printed2 = False
printed3 = False
printed4 = False
terminalprint = 0
timer = 0
otherBool = False
object_list = []
CURRENTMODE = "null"


pumpkin_windspeeds = {1 : Vec(), 2 : Vec(), 3 : Vec(10), 4 : Vec(-15), 5 : Vec(-12, 1), 6 : Vec(15, 1)}
pumpkin_angles = {1 : 10, 2 : 30, 3 : 60, 4: 80}


def ball_xy(ball):
    return origin[0] + ball.pos.x*scale, origin[1] - ball.pos.y*scale - 10


screen = p.display.set_mode((WIDTH, HEIGHT))


def pygame_init():
    # Screen or whatever you want to call it is your best friend - it's a canvas
    # or surface where you can draw - generally you'll have one large canvas and
    # additional surfaces on top - effectively breaking things up and giving
    # you the ability to have multiples scenes in one window
    p.init()
    screen.fill((180, 210, 255))
    p.display.set_caption('Fireworks')


def drawer(object_list, place_to_draw_stuff=screen):
    for i in object_list:
        p.draw.circle(place_to_draw_stuff, i.color, ball_xy(i), 10)


def skydive_checks(baller):
    global printed
    global printed2
    global oldv
    global oldpos
    if baller.pos.y <= 1000 and printed is False:
        print(f"PARACHUTE DEPLOYED AT: {baller.pos.y} meters up and {timer} seconds")
        baller.drag_override(math.pi * 9, 1.6)
        terminalprint = 0
        printed = True
    if baller.pos.y <= baller.floor and printed2 is False:
        printed2 = True
        print(
            f"yo the ball hit the floor after like {timer} seconds or somethin, "
            f"if you catch my drift dude. \n it hit the floor at {baller.pos}")
    if round(mag(baller.v), 7) == round(oldv, 7) and baller.pos is not oldpos and terminalprint < 10:
        print(f"current speed: {mag(baller.v)}, is terminal = {mag(baller.v) == oldv}")
        terminalprint += 1
    oldv = baller.v.x
    oldpos = baller.pos


def car_checks(balln):
    global printed
    global printed2
    global printed3
    global printed4
    global terminalprint
    global running
    global oldv
    global oldpos
    if balln.v.x >= 62 / 2.23694 and printed == False:
        print(f"the car reached {balln.v.x * 2.23694} mph after {timer} seconds")
        printed = True

    if balln.v.x >= 124 / 2.23694 and printed2 == False:
        print(f"the car reached {balln.v.x * 2.23594} mph after {timer} seconds")
        printed2 = True

    if balln.pos.x >= 1609.34*.25 and printed3 == False:
        print(f"reached .25 miles after {timer} seconds")
        printed3 = True

    if balln.pos.x >= 1609.34 and printed4 == False:
        print(f"reached one mile after {timer} seconds")
        printed4 = True

    oldv = balln.v.x
    oldpos = balln.pos


def checks(input, ball):
    if input == "skydiver":
        skydive_checks(ball)
    if input == "racecar":
        skydive_checks(ball)


def setter_upper(name, mode: int = 0, wind_mode = 0):
    global otherBool
    global object_list
    global scale
    global origin
    if name == "skydiver":
        object_list = [Ball(Vec(0, 3700, 0))]
        scale = 0.05
        if mode == 0:
            object_list[0].drag_override(0.23, 1.0)
        elif mode == 1:
            object_list[0].drag_override(0.45, 1.4)
        else:
            raise OverflowError("mode must be in range [0,1]")
    elif name == "racecar":
        object_list = [Ball(Vec(), Vec(), Vec(), 1435, (10, 1.98, 0.33), Vec(), (0, 0, 0), [Vec(0, 1435*9.81)])]
        scale = .5
        if mode > 0:
            otherBool = True
    elif name == "pumkin chunkin":
        if mode == 0:
            object_list = []





# tester variables
height = 0
speed = 0
angle = 180
wind_speed = Vec()


inputs = [input("INPUT TEST TYPE: "), float(input("INPUT MODE: "))]
# ball order: Position, Speed, Angle, Acceleration, Mass, Radius (meters), Wind Speed
setter_upper(inputs[0], inputs[1])
pumkin = [Pumpkin(pumpkin_angles[1], pumpkin_windspeeds[1]), Pumpkin(pumpkin_angles[2], pumpkin_windspeeds[2]), Pumpkin(pumpkin_angles[3], pumpkin_windspeeds[3]), Pumpkin(pumpkin_angles[4], pumpkin_windspeeds[4])]
# ball = ball_from_angle(Vec(0, math.sin(math.radians(10))*30.48), 330, 10, g, 4.2, 0.125, Vec(), (235, 235, 80))

running = False
while True:
    screen.fill((150, 210, 255))
    #keystroke example
    for event in p.event.get():

        if event.type == p.QUIT:  # this refers to clicking on the "x"-close
            p.quit()
            sys.exit()

        elif event.type == p.KEYDOWN:  # there's a separate system built in
            # for multiple key presses or presses
            # that result in changes of state - tba
            if event.key == p.K_g:
                print("n")

            if event.key == p.K_a:
                print("goodbye")

            if event.key == p.K_SPACE:
                if running is False:
                    running = True
                    print("START")
                elif running is True:
                    running = False
                    print("PAUSE")

    if running:
        #background

        for z in range(100):

            timer += dt

            for o in object_list:
                o.step(dt, inputs[0])

        #     for pump in pumkin:
        #         pump.pumpstep(dt)
        # for pumpkin in pumkin:
        #     drawer([pumpkin.obj])
        # drawer([ball])
        checks(inputs[0], object_list[0])
        drawer(object_list)
        # I used this to increase wind speed until the top speed of the car is 250 mph
        # if object_list[0].v.x < 250/2.23694:
        #     ball.wind((ball.wind_speed + Vec(0.5)))
        #     print(ball.wind_speed)
        p.draw.rect(screen, (50, 200, 100), (x0 / 2, y0, WIDTH, HEIGHT))
        p.display.flip()

    # This sets an upper limit on the frame rate (here 100 frames per second)
    # often you won't be able
    p.time.Clock().tick(100)
