# Welcome to The Electric Fursuits RGB Deep Dive handout!

## LED Square Tutorial

## LED Types

Highbeam used Lilypad LEDs as at the time, the "Seed" style leds were not commercially avaliable 

| Image                           | Type         | £/LED                                                                                       | Pros                                                                                              | Cons                                                    |
|---------------------------------|--------------|---------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| ![](media\seed_style_leds.jpg)  | "Seed" style | [£0.05](aliexpress.com/item/1005004633923201.html?gatewayAdapt=glo2deu)                     | - Flexible<br/>- Lightweight<br/>- Waterproof                                                     | - Not as bright as the other types<br/>- Hard to solder |
| ![](media\strip_style_leds.jpg) | Strip        | [£0.05](aliexpress.com/item/32852794406.html) | - Very bright<br/>- Adhesive backing<br/>- Lots of densities & sizes <br/>- Waterproofing options | - Cannot be bent<br/>- Gets hot                         |
| ![](media\lillypad_leds.png)    | Lilypad      | [£0.13](aliexpress.com/item/32633490802.html)                                               | - Very bright<br/>- Flexible                                                                      | - No waterproofing<br/>- Expensive<br/>- Also gets hot  |

> [!WARNING]
> NEVER USE 12v WS2815 LEDS for heavy color. At their worst, they are 3x less efficient than WS2812b

## Common Mapping

## Types of Microcontroller

| Image                 | Name            | £                                                                               | Pros                                                                                                                | Cons                                                                                                               |
|-----------------------|-----------------|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| ![](media\plasma.png) | Pimoroni Plasma | [£14.10](https://shop.pimoroni.com/products/plasma-2040?variant=39410354847827) | - Has built in USB-C power management<br/>- Supports MicroPython, CircuitPython and C++<br/>- No soldering required | - Weak processor, can only do about 100 leds worth of heavy processing<br/>- Realistically only supports 1 channel |
| ![](media\teensy.png) | Teensy 4.1      | [£29.70](https://thepihut.com/products/teensy-4-1)                              | - Absolute unit of a processor<br/>- I've driven 10k LEDs with one of these<br/>- Great as a driver board over USB  | - Expensive<br/>- Only supports C style programming<br/>- Expensive                                                |

> [!TIP]
> If you're gonna use the Teensy 4.1, checkout my [FC-Mega](https://github.com/TheMariday/FC-Mega) library. It allows you to plug in your Teensy to your PC and send it LED data over USB. Super simple!

### [Pimoroni Plasma](https://shop.pimoroni.com/products/plasma-2040?variant=39410354847827)
- 
### [Teensy 4.1](https://thepihut.com/products/teensy-4-1)
- £29.70


## Batteries

## General Advice



## Tools
