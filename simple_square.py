from plasma import plasma2040, WS2812

NUM_LEDS = 400
WIDTH = 20

def mapping(index):
    y = int(index / WIDTH)
    x = index % WIDTH
    if y % 2 == 1:
        x = WIDTH - 1 - x
    return x, y

def rainbow(frame_number, x, y):
    h = (x*0.5 + frame_number/10)/WIDTH
    s = 1.0
    v = 1.0
    return h, s, v


leds = WS2812(NUM_LEDS, 0, 0, plasma2040.DAT)

leds.start()

frame = 0

while True:
    for led_index in range(NUM_LEDS):
        x, y = mapping(led_index)
        h, s, v = rainbow(frame, x, y)
        leds.set_hsv(led_index, h, s, v)
    frame += 1
