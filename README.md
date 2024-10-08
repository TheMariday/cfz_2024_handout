# Welcome to The Electric Fursuits RGB Deep Dive handout!

This is a supplimental document to the panel, but please do use for reference and share where you fancy!
No copyright or any of that nonsense, copy and paste away!
> [!CAUTION]
> This is Mariday's simplified opinion, there are many things omitted here and complexities that have been breezed over

## LED Types

What we're looking for here is 5v "addressable" leds, these can be APA102, WS2812b,SK98 or even have no chip name like the "seed" style!

> [!WARNING]
> DO NOT USE 12v WS2815 LEDS for pretty much anything. At their worst, they are 3x less efficient than WS2812b

| Image                             | Type         | £/LED                                               | Pros                                                                                              | Cons                                                    |
|-----------------------------------|--------------|-----------------------------------------------------|---------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| ![](media%2Fseed_style_leds.jpg)  | "Seed" style | [£0.05](https://www.aliexpress.com/item/1005004633923201.html)  | - Flexible<br/>- Lightweight<br/>- Waterproof                                                     | - Not as bright as the other types<br/>- Hard to solder |
| ![](media%2Fstrip_style_leds.jpg) | Strip        | [£0.05](https://www.aliexpress.com/item/32852794406.html)       | - Very bright<br/>- Adhesive backing<br/>- Lots of densities & sizes <br/>- Waterproofing options | - Cannot be bent<br/>- Gets hot                         |
| ![](media%2Flillypad_leds.png)    | Lilypad      | [£0.13](https://www.aliexpress.com/item/32633490802.html)       | - Very bright<br/>- Flexible                                                                      | - No waterproofing<br/>- Expensive<br/>- Also gets hot  |

> [!NOTE]
> Highbeam used Lilypad LEDs as at the time, the "Seed" style leds were not commercially available!

## Microcontrollers

| Image                              | Name            | £                                                        | Pros                                                                                                               | Cons                                                                                                               |
|------------------------------------|-----------------|----------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| ![](media%2Fplasma.png)            | Pimoroni Plasma | [£14.10](https://shop.pimoroni.com/products/plasma-2040) | - Has built in USB-C power management<br/>- Supports Micro/CircuitPython and C++<br/>- No soldering required       | - Weak processor, can only do about 100 leds worth of heavy processing<br/>- Realistically only supports 1 channel |
| ![](media%2Fteensy.png)            | Teensy 4.1      | [£29.70](https://thepihut.com/products/teensy-4-1)       | - Absolute unit of a processor<br/>- I've driven 10k LEDs with one of these<br/>- Great as a driver board over USB | - Expensive<br/>- Only supports C style programming<br/>- Requires soldering & external power management           |
|TODO|Arduino nano|£10|TODO|TODO|
> [!TIP]
> If you're gonna use the Teensy 4.1, checkout my [FC-Mega](https://github.com/TheMariday/FC-Mega) library. It allows you to plug in your Teensy to your PC and send it LED data over USB. Super simple!


## Suppliers

- **Pimoroni** - Fantastic supplier of electronics stuff, lots of cool custom boards
- **The Pi Hut** - Sells a lot of Pimoroni stuff plus some nice off the shelf electronics components and tools
- **Ebay** - Good if you want something cheap and dirty
- **Amazon** - Good if you want something cheap and dirty and with next day delivery
- **AliExpress** - Your go-to place for bulk buying LEDs and other components. As you're buying directly from China, the cost can be up to 10x less! And usually free shipping! Takes a few weeks though. Some sellers can be dodgy so best bet is to always buy a small amount first to see if it's up to scratch! BTF or Rita lighting are good and will often make you custom orders if you need something custom! Rita made Highbeams LED strings! 

## Tools

One thing I didn't cover in the talk is tools!

I'm a big fan of Adam Savages approach to tools, buy the cheapest you can find, 
then when you're sick of it, you'll know how much you want to spend on it.

For instance, my pliers cost me £3 from Maplins 10 years ago, but my wire cutters cost around £80.

Once you know what you'll use the most, you'll know what to spend.

The below are just my suggestions and there are lots of alternatives depending on what you're using them for!

For instance, I wouldn't use my TS80P soldering iron for big battery wires

### A list of some electronic fursuit tools:


| Image of mine                         | Name            | Cheap                                                                                                | Expensive (mine)                                                                                                                              | Notes                                                                                                                                                                    |
|---------------------------------------|-----------------|------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](media%2Fsoldering_iron_image.png) | Soldering Iron  | [£30 Antex XS25](https://thepihut.com/products/antex-xs25-soldering-iron-uk-plug)                    | [£75 TS80P](https://thepihut.com/products/ts80p-usb-c-smart-soldering-iron)                                                                   | I like mine cause it's USB-c. Loads available but even the cheapest will probably get the job done! Try and get one with a nice flat tip.                                |
| ![](media%2Fglue_gun.jpg)             | Glue gun        | [£17 Einhell](https://www.amazon.co.uk/Einhell-Mechanical-Viewing-Standard-Extension/dp/B01MQQVK0F)  | [£36 Einhell Cordless](https://www.screwfix.com/p/einhell-te-cg-18-li-solo-18v-li-ion-power-x-change-cordless-hot-glue-gun-bare/256TJ?tc=CB9) | I like mine cause it's wireless! I move around a lot so it makes sense for me, but a decent mains powered one will heat up quicker and of course not run out of battery! |
| ![](media%2Fwire_strippers.jpg)       | Wire Strippers  | [£6 No Brand](https://thepihut.com/products/wire-strippers)                                          | [£50 RS Components Automatic Strippers](https://uk.rs-online.com/web/p/wire-strippers/3822847)                                                | Oh gods, if you can afford expensive ones, get them! They make such a difference                                                                                         |
| ![](media%2Fwire_cutters.jpg)         | Wire Cutters    | [£3.50 No Brand](https://thepihut.com/products/diagonal-cutters)                                     | [£100 Lindstrom RX8151 side cutters](https://uk.rs-online.com/web/p/cutters/1906703/)                                                         | I wouldn't spend the money on these unless you're using them daily. But if you are, you absolutely need to spend at least £50 on some decent ones!                       |


### Some optional extras that will help when things go wrong


| Image                            | Name                   | Price (mine)                                                                                        | Notes                                                                                                                                                                             |
|----------------------------------|------------------------|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](media%2Fmeter.png)           | Multimeter             | [£17 and up](https://thepihut.com/products/digital-multimeter-model-9205b)                          | You can get really expensive multimeters, however I've never needed that level of precision or reliability personally                                                             |
| ![](media%2Fcrocodile_clips.png) | Crocodile clips        | [£3 for 12](https://thepihut.com/products/short-wire-alligator-clip-test-lead-set-of-12)            | Side note, don't use these for anything more than like 1 amp, I've had some serious issues where the problem turned out to be my crocodile clips getting //rather// toasty!       |
| ![](media%2Fpower_supply.jpg)    | Bench top power supply | [£80 at least](https://uk.rs-online.com/web/p/bench-power-supplies/1757368)                         | Get a decent one of these! This is a good model and I would recommend checking out RS components for the "right" price for these. There are a lot of shite ones on Ebay / Amazon! |

## Batteries

There are 3 main things to look for in a battery:

### Voltage

Make sure your battery can output the voltage you need for your system!

All USB battery banks will output 5v, but some that support USB-C can go as high as 28v! Great if you want to power your... Minifridge?

### Output Current

This is the most energy a battery can dump through its connectors. 
For USB, this usually maxes out at 3 amps as the cables would need to be much thicker to handle more!

However, you can increase the voltage **if** your system can handle that!

### Capacity

So lots of manufacturers measure capacity in milli-amp hours or mAh, which in most cases is completely useless.

It's much useful to know the **watt-hours / Wh** of the battery! This can usually be found by multiplying the batteries **amp-hours** by **3.6**

To find how long your battery will last, 
divide your battery capacity in **watt-hours** by the amount of current you're intending to draw in **amps** 
then times by 0.8 for good measure.

For example:

- My LEDs draw **2 amps** at **5 volts**
- This is equal to **10 watts** (`2 amps * 5 volts`)
- I'm using the Anker Nano which has **36 watt-hours**
- So my total run-tim is about **3 hours** (`(10 watts / 36 watt-hours)*0.8`)

### A table of a few battery suggestions


| Image                  | Price                                                                                        | Output                                                 | Notes                                                                                                                         |
|------------------------|----------------------------------------------------------------------------------------------|--------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| ![](media%2Fnano.png)  | [£39 Anker Nano](https://www.anker.com/uk/products/a1259-built-in-cable-power-bank-10000mah) | 1x3A or 2x2A output<br>USBC & USBA<br>5v - 20v<br>36Wh | My personal fave for anything up to 400 seed style leds or 100 strip style                                                    |
| ![](media%2Fprime.png) | [£180 Anker Prime](https://www.anker.com/uk/products/a1340-250w-power-bank)                  | 3x3A +<br>2XUSBC & USBA<br>5v-28v<br>100Wh             | Power everything forever                                                                                                      |
| ![](media%2Flipo.jpg)  | [LiPo](https://www.youtube.com/watch?v=Dcu1z8vAgkQ&ab_channel=TeamFortress2-AllSounds)       | Nope<br>Do not<br>Just why                             | The Anker Prime has enough power to run an 82 Inch LED TV.<br>WHAT THE HELL DO YOU NEED MORE FOR?<br> Also LiFe exists y'know |


## Code

All the code I used during the presentation can be found in the [led square](led_square) folder of this readme!

Here's a nice generic template for how I usually do things:

```python
def some_kind_of_mapping(led_index):
    # Do some kind of mapping here that turns your led index into an x y coordinate
    return x, y


def some_kind_of_effect(frame_number, x, y):
    # Do some kind of cool thing that takes the frame number, x and y and produce an HSV value
    return h, s, v


my_strip = some_led_driver_library()

frame_number = 0

while True:
    for led_index in range(NUM_LEDS):
        x, y = some_kind_of_mapping(led_index)
        h, s, v = some_kind_of_effect(frame_number, x, y)
        my_strip.set_hsv(led_index, h, s, v)
    frame_number += 1
```

## Mapping

Mapping is the way we turn 1D led indexes into 2D positions

Here's the one used in my demo square where `WIDTH` is set to 20 for my example:

Nothing here should be surprising, perhaps except the `%` which just means "remainder"

```python
def mapping(index):
    
    y = int(index / WIDTH)
    x = index % WIDTH
    
    if y % 2 == 1:
        x = WIDTH - 1 - x
        
    return x, y
```

## Effects

Effects in short take a 2D position along with the current time and produce an RGB or HSV value

Here's a super simple effect for making an animated rainbow that moves the rainbow along the x axis

```python
def rainbow_x(frame_number, x, y):
    
    h = (x * RAINBOW_SIZE + frame_number / RAINBOW_SPEED) / WIDTH
    s = 1.0
    v = 1.0
    
    return h, s, v
```


## Closing Advice

- Make mistakes early!
- Be safe!
- Enjoy yourself!
- Get Mariday some coffee, they are a very eepy bean as they write this

# Well done!

You've made it to the bottom of the handout! Have a picture of my cat for all your hard work
![](media%2Fcat.png)

Massive thanks to Max, Reiu and Pixelsuchter for feedback on this document along with Tux for their wonderful co-hosting and Lutis for the design of the EF coin.

If you want to reach out you can find me on [Telegram](https://www.t.me/themariday) or [Twitter](https://www.twitter.com/themariday)! Love love!
