# Welcome to The Electric Fursuits RGB Deep Dive handout!

This is a supplimental document to the panel, but please do use for reference and share where you fancy!
No copyright or any of that nonsense, copy and paste away!

## LED Types

Highbeam used Lilypad LEDs as at the time, the "Seed" style leds were not commercially avaliable 

| Image                           | Type         | £/LED                                                                                       | Pros                                                                                              | Cons                                                    |
|---------------------------------|--------------|---------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| ![](media%2Fseed_style_leds.jpg)  | "Seed" style | [£0.05](aliexpress.com/item/1005004633923201.html)                     | - Flexible<br/>- Lightweight<br/>- Waterproof                                                     | - Not as bright as the other types<br/>- Hard to solder |
| ![](media%2Fstrip_style_leds.jpg) | Strip        | [£0.05](aliexpress.com/item/32852794406.html) | - Very bright<br/>- Adhesive backing<br/>- Lots of densities & sizes <br/>- Waterproofing options | - Cannot be bent<br/>- Gets hot                         |
| ![](media%2Flillypad_leds.png)    | Lilypad      | [£0.13](aliexpress.com/item/32633490802.html)                                               | - Very bright<br/>- Flexible                                                                      | - No waterproofing<br/>- Expensive<br/>- Also gets hot  |

> [!WARNING]
> NEVER USE 12v WS2815 LEDS for heavy color. At their worst, they are 3x less efficient than WS2812b

## Common Mapping

## Types of Microcontroller

| Image                 | Name            | £                                                                               | Pros                                                                                                                | Cons                                                                                                               |
|-----------------------|-----------------|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| ![](media%2Fplasma.png) | Pimoroni Plasma | [£14.10](https://shop.pimoroni.com/products/plasma-2040) | - Has built in USB-C power management<br/>- Supports MicroPython, CircuitPython and C++<br/>- No soldering required | - Weak processor, can only do about 100 leds worth of heavy processing<br/>- Realistically only supports 1 channel |
| ![](media%2Fteensy.png) | Teensy 4.1      | [£29.70](https://thepihut.com/products/teensy-4-1)                              | - Absolute unit of a processor<br/>- I've driven 10k LEDs with one of these<br/>- Great as a driver board over USB  | - Expensive<br/>- Only supports C style programming<br/>- Expensive                                                |

> [!TIP]
> If you're gonna use the Teensy 4.1, checkout my [FC-Mega](https://github.com/TheMariday/FC-Mega) library. It allows you to plug in your Teensy to your PC and send it LED data over USB. Super simple!


## Suppliers

- The Pi Hut
- Pimoroni
- Ebay
- Amazon
- AliExpress
  - BTF Lighting

## Tools

One thing I didn't cover in the talk is tools!

I'm a big fan of Adam Savages approach to tools, buy the cheapest you can find, then when you're sick of it, you'll know how much you want to spend on it.
For instance, my pliers cost me £3 from Maplins 10 years ago, but my wire cutters cost around £80.
Once you know what you'll use the most, you'll know what to spend.

The below are just my suggestions and there are lots of alternatives depending on what you're using them for!
For instance, I wouldn't use my TS80P soldering iron for big battery wires

### A basic list of Electronic Fursuit tools in order of importance:


| Image of mine                   | Name           | Cheap                                                                                               | Expensive (mine)                                                                                                                              | Notes |
|---------------------------------|----------------|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|-------|
| ![](media%2Fsoldering_iron.png) | Soldering Iron | [£30 Antex XS25](https://thepihut.com/products/antex-xs25-soldering-iron-uk-plug)                   | [£75 TS80P](https://thepihut.com/products/ts80p-usb-c-smart-soldering-iron)                                                                   |       |
| ![](media%2Fglue_gun.jpg)       | Glue gun       | [£17 Einhell](https://www.amazon.co.uk/Einhell-Mechanical-Viewing-Standard-Extension/dp/B01MQQVK0F) | [£36 Einhell Cordless](https://www.screwfix.com/p/einhell-te-cg-18-li-solo-18v-li-ion-power-x-change-cordless-hot-glue-gun-bare/256TJ?tc=CB9) |       |
| ![](media%2Fwire_strippers.jpg) | Wire Strippers | [£12 No Brand](https://thepihut.com/products/automatic-self-adjusting-wire-strippers-and-cutter)    | [£50 RS Components Automatic Strippers](https://uk.rs-online.com/web/p/wire-strippers/3822847)                                                |       |

### Here are some extras that will seriously help when things go wrong


| Image                            | Name                   | Price (mine)                                                                                        | Notes                                                                                                                                                                             |
|----------------------------------|------------------------|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](media%2Fmeter.png)           | Multimeter             | [£17 and up](https://thepihut.com/products/digital-multimeter-model-9205b)                          | You can get really expensive multimeters, however I've never needed that level of precision or reliability personally                                                             |
| ![](media%2Fcrocodile_clips.png) | Crocodile clips        | [£3 for 12](https://thepihut.com/products/short-wire-alligator-clip-test-lead-set-of-12)            | Side note, don't use these for anything more than like 1 amp, I've had some serious issues where the problem turned out to be my crocodile clips getting //rather// toasty!       |
| ![](media%2Fpower_supply.jpg)    | Bench top power supply | [£80 at least](https://uk.rs-online.com/web/p/bench-power-supplies/1757368)                         | Get a decent one of these! This is a good model and I would recommend checking out RS components for the "right" price for these. There are a lot of shite ones on Ebay / Amazon! |
| ![](media%2Fscope.jpg)           | Oscilloscope           | [£65 at least](https://www.amazon.co.uk/Hantek-Digital-Storage-Oscilloscope-PC-Based/dp/B015XTOOKY) | Mine is the cheapest, nastiest one you can get. But you know what? I haven't needed more from it! But a decent one will probably set you back £500 or more                        |

## Batteries

## General Advice

## LED Square Tutorial


## Tools
