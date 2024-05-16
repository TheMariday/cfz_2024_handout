from plasma import plasma2040, WS2812
from pimoroni import Button
from random import random
import math

NUM_LEDS = 400
WIDTH = 20


def mapping(index):
    y = int(index / WIDTH)
    x = index % WIDTH
    if y % 2 == 1:
        x = WIDTH - 1 - x
    return x, y


def rainbow_x(frame_number, x, y):
    h = (x * 0.5 + frame_number / 20) / WIDTH
    s = 1.0
    v = 1.0
    return h, s, v


def rainbow_y(frame_number, x, y):
    h = (y * 0.5 + frame_number / 20) / WIDTH
    s = 1.0
    v = 1.0
    return h, s, v


def rainbow_xy(frame_number, x, y):
    h = ((x + y) * 0.5 + frame_number / 20) / WIDTH
    s = 1.0
    v = 1.0
    return h, s, v


def rainbow_y_short(frame_number, x, y):
    h = (y * 2 + frame_number) / WIDTH
    s = 1.0
    v = 1.0
    return h, s, v


def fire(frame_number, x, y):
    return (1, 1, 1) if random() < 0.5 else (0.1, 1, 1)


def droplet(frame_number, x, y):
    dist = math.sqrt(pow(x - 10, 2) + pow(y - 10, 2))
    return ((dist - frame_number / 4) / 20.0) % 1.0, 1.0, 1.0


def swirl(frame_number, x, y):
    x -= 10
    y -= 10
    dist = math.sqrt(pow(x, 2) + pow(y, 2))

    angle = (frame_number / 20.0) - dist / 3

    s = math.sin(angle)
    c = math.cos(angle)

    xs = x * c - y * s
    ys = x * s + y * c

    r = abs(xs + ys)

    return r / 50, 1.0, 1 - r / 10


def police(frame_number, x, y):

    red = [1, 1, 1]
    blue = [0.7, 1, 1]
    black = [0, 0, 0]

    left = [red, black, red, black] + [black] * 2 + [black, black, black, black] + [black] * 2
    right = [black, black, black, black] + [black] * 2 + [blue, black, blue, black] + [black] * 2

    i = int(frame_number) % len(left)
    return left[i] if y < 10 else right[i]


button_a = Button(plasma2040.BUTTON_A)
button_b = Button(plasma2040.BUTTON_B)

leds = WS2812(NUM_LEDS, 0, 0, plasma2040.DAT)
leds.start()

frame = 0

effect_index = 0

effects = [
    rainbow_y,
    rainbow_xy,
    rainbow_x,
    fire,
    droplet,
    police,
    rainbow_y_short,
    swirl,
]

while True:

    if button_a.read():
        effect_index = (effect_index + 1) % len(effects)
    if button_b.read():
        effect_index = (effect_index - 1) % len(effects)

    for led_index in range(0, NUM_LEDS, 2):
        x, y = mapping(led_index)
        h, s, v = effects[effect_index](frame, x, y)
        leds.set_hsv(led_index, h, s, v)
        leds.set_hsv(led_index + 1, h, s, v)

    frame += 1
