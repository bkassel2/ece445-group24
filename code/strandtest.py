#!/usr/bin/env python3
# rpi_ws281x library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.

import time
from rpi_ws281x import *
import argparse
import board
import busio
import adafruit_mpr121
import numpy as np
import adafruit_mpr121
import random
# Create I2C bus.
i2c = busio.I2C(board.SCL, board.SDA)

# Create MPR121 object.
mpr121 = adafruit_mpr121.MPR121(i2c , address = 0x5a)
#mpr1212 = adafruit_mpr121.MPR121(i2c , address = 0x5b)
#mpr1213 = adafruit_mpr121.MPR121(i2c , address = 0x5c)
#mpr1214 = adafruit_mpr121.MPR121(i2c , address = 0x5d)


# Import MPR121 module.
# LED strip configuration:
LED_SEPERATION = 37     #Seperation in  4 pixel per inch 
LED_COUNT      = 144 + LED_SEPERATION      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 150     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

LED_PIN2       = 13
LED_CHANNEL2   = 1
PIXEL_WIDTH    = 3
SPEED          = 1000.0
# 1000  ~ 144/14 = 10 pixels / second
# 5000  ~ 144/6 = 24 pixels / second
# 10000 ~ 144/5 = 28 pixels/second

# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/10000.0)



def quantumlights(strip1, strip2 , color1_1 , color1_2 , color2_1 , color2_2,s1p , s2p, wait_ms = 50):
    # Clears the first pulse of lights
    if s1p != LED_COUNT - 1:
        strip1.setPixelColor(s1p+1, Color(0,0,0))
    if s2p != LED_COUNT - 1:
        strip2.setPixelColor(s2p+1, Color(0,0,0))
    if s1p == LED_COUNT - 1:
        strip1.setPixelColor(0, Color(0,0,0))
    if s2p == LED_COUNT - 1:
        strip2.setPixelColor(0, Color(0,0,0))

    # Clears the second pulse of lights
    if (s1p + LED_SEPERATION + 1 + 1)% LED_COUNT < LED_COUNT:
        strip1.setPixelColor((s1p + LED_SEPERATION + 1)%LED_COUNT, Color(0,0,0))
    if (s2p + LED_SEPERATION + 1 + 1)% LED_COUNT < LED_COUNT:
        strip2.setPixelColor((s2p + LED_SEPERATION + 1)%LED_COUNT, Color(0,0,0))
    for x in range(PIXEL_WIDTH):
        strip1.setPixelColor((s1p + LED_SEPERATION - x)%LED_COUNT, color1_2)
        strip2.setPixelColor((s2p + LED_SEPERATION - x)%LED_COUNT, color2_2)
        # for j in range(12):
        # # Call is_touched and pass it then number of the input.  If it's touched
        # # it will return True, otherwise it will return False.
        #    if mpr121[j].value:
        #        print("Input {} touched!".format(j))
        #time.sleep(0.25)  # Small delay to keep from spamming output messages.
        strip1.setPixelColor((s1p - x)% LED_COUNT, color1_1)
        strip2.setPixelColor((s2p - x) % LED_COUNT, color2_1)

    strip1.show()
    strip2.show()
    time.sleep(wait_ms/SPEED)
# 
# 
# 

touch_array = np.zeros(24)
s1touch = np.zeros(12)
def s1touch(s1):
    pos = (s1 + 8)%144 // 8
    pos1measurement = 0
    color1measurement = 0
    s1touch = np.zeros(12)
    for i in range(12):
        # Call is_touched and pass it then number of the input.  If it's touched
        # it will return True, otherwise it will return False.
           if mpr121[i].value:
               s1touch[i] = 1
    if s1touch[(pos - 1)%12] == 1 and s1touch[(pos + LED_SEPERATION//8)%12] == 1 :
        pos1measurement = 1
    print("S1")
    print(s1touch)
    print(s1touch[0])
    print(pos)
    for i in range(LED_SEPERATION // 8 //2):
        if pos + i < 12:
            if (s1touch[(pos+ i)]):
                color1measurement = 1
    # print (pos , (pos + LED_SEPERATION // 8)%24)
    return pos1measurement , color1measurement

# s2touch = np.zeros(12)
# def s2touch(s1):
#     pos = (s1 + 8) // 8
#     pos1measurement = 0
#     color1measurement = 0
#     s1touch = np.zeros(12)
#     for i in range(12):
#         # Call is_touched and pass it then number of the input.  If it's touched
#         # it will return True, otherwise it will return False.
#            if mpr1212[i].value:
#                s1touch[i] = 1
#     if s1touch[(pos - 1)%12] == 1 and s1touch[(pos + 2)%12] == 1 :
#         pos1measurement = 1
#     if (s1touch[(pos + 1)%12]) or (s1touch[(pos + 2)% 12]):
#         color1measurement = 1
#     # print (pos , (pos + LED_SEPERATION // 8)%24)
#     return pos1measurement , color1measurement

    


def testlight():
    for i in range(0 , 255 , 10):
        for j in range (0, 255 , 10):
            for k in range(0, 255, 10):
                for x in range(3):
                    # print(i , j , k)
                    strip2.setPixelColor(50 - x, Color(i , j , k))
                # strip2.setPixelColor((s2p - x) % LED_COUNT, color2_1)
                strip2.show()
    # strip2.show()
        time.sleep(50/100)


def test2():
    for x in range(3):
        strip2.setPixelColor(50-x, red)
        strip2.setPixelColor(50 - x  + LED_SEPERATION, blue)

    strip2.show()
    time.sleep(1/20)


def theaterChaseRainbow(strip, wait_ms=50):
    """Rainbow movie theater light style chaser animation."""
    for j in range(256):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, wheel((i+j) % 255))
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip1 = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip2 = Adafruit_NeoPixel(LED_COUNT, LED_PIN2, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL2)
    # Intialize the library (must be called once before other functions).
    strip1.begin()
    strip2.begin()

    print ('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')
    # color1 = Color(255,0,0) #red
    # color2 = Color(255,0,0) #red
    # color3 = Color(0,0,255) #blue
    # color4 = Color(0,0,255) #blue
    purple = Color(128,0,128)
    red = Color(255,0,0)
    blue = Color(0,0,255)
    black = Color(0,0,0)
    color1 = color2 = color3 = color4 = purple
    s1flag = 0
    s2flag = 0
    touch = 0
    times = 0
    p1 = -1
    p2 = -1
    p1f = -1
    p2f = -1
    c1f = -1
    c2f = -1
    firstmeasurent = 1
    firsttype = -1
    try:
        s1p = LED_COUNT - LED_SEPERATION - 1
        s2p = LED_COUNT - LED_SEPERATION - 1
        while True:
            # Reset
            if (times % 100 == 0 or s2p == LED_COUNT or s1p == LED_COUNT)and s1flag == 1 :
                print("reached")
                s1flag = 0
                s1p = LED_COUNT - LED_SEPERATION - 1
                s2p = LED_COUNT - LED_SEPERATION - 1
                color1 = color2 = color3 = color4 = purple
                colorWipe(strip1, Color(0,0,0), 0.1)
                colorWipe(strip2, Color(0,0,0), 0.1)
                p1 = -1
                p2 = -1
                p1f = -1
                p2f = -1
                c1f = -1
                c2f = -1
                firstmeasurent = 1
                firsttype = -1



            if s1p == -1:
                s1p = LED_COUNT - 1
            if s2p == -1:
                s2p = LED_COUNT - 1
            # print("Loop")
            # testlight()
            if s1flag:
                s1p = p1
            if s2flag:
                s2p = p2
            quantumlights(strip1 , strip2, color1 , color2 ,color3 , color4, s1p, s2p)
            pos1f , color1f = s1touch(s1p)
            if color1f:
                if firstmeasurent:
                    x = random.randint(0,10000) % 2
                    firstmeasurent = 0
                    firsttype = 0
                    if x:
                        color1 = red
                        color2 = blue
                        c1f = 0
                    else:
                        color1 = blue
                        color2 = red
                        c1f = 1
                elif firsttype == 0:
                    if c2f:
                        color1 = red
                        color2 = blue
                    else:
                        color1 = blue
                        color2 = red
                else:
                    x = random.randint(0,10000) % 2
                    if x:
                        color1 = red
                        color2 = blue
                    else:
                        color1 = blue
                        color2 = red
                p1 = s1p
                s1flag = 1
                times = 1
            if pos1f:
                if firstmeasurent:
                    x = random.randint(0,10000) % 2
                    firstmeasurent = 0
                    firsttype = 1
                    if x:
                        color1 = black
                        p1f = 0
                    else:
                        color2 = black
                        p1f = 1
                elif firsttype == 1:
                    if p2f:
                        color1 = black
                    else:
                        color2 = black
                else:
                    x = random.randint(0,10000) % 2
                    if x:
                        color1 = black
                    else:
                        color2 = black
                p1 = s1p
                s1flag = 1
                times = 1
            # pos2f , color2f = s2touch(s2p) 
            # if color2f:
            #     color1 = red
            #     color2 = blue
            #     p2 = s2p
            #     s2flag = 1
            #     times = 1   
            # if pos2f:
            #     if firstmeasurent:
            #         x = random.randint(0,10000) % 2
            #         if x:
            #             color3 = black
            #             p2f = 0
            #         else:
            #             color4 = black
            #             p2f = 1
            #     else:
            #         if p1f:
            #             color3 = black
            #         else:
            #             color4 = black
            #     p2 = s2p
            #     s1flag = 1
            #     times = 1 
            # print(pos1flag , color1f)

            if s1flag == 0:
                s1p -= 1
            if s2flag == 0:
                s2p -= 1
            times += 1

    except KeyboardInterrupt:
        if args.clear:
            colorWipe(strip1, Color(0,0,0), 1)
            colorWipe(strip2, Color(0,0,0), 1)