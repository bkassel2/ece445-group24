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

# Create I2C bus.
i2c = busio.I2C(board.SCL, board.SDA)

# Create MPR121 object.
mpr121 = adafruit_mpr121.MPR121(i2c)
#mpr1212 = adafruit_mpr121.MPR121(i2c , address = 0x5b)
#mpr1213 = adafruit_mpr121.MPR121(i2c , address = 0x5c)
#mpr1214 = adafruit_mpr121.MPR121(i2c , address = 0x5d)


# Import MPR121 module.
import adafruit_mpr121
# LED strip configuration:
LED_SEPERATION = 20



LED_COUNT      = 144 + LED_SEPERATION      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).    
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

LED_PIN2       = 13
LED_CHANNEL2   = 1


# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels(), -1 , -1):
        if i != LED_COUNT - 1:
            strip.setPixelColor(i+1, Color(0,0,0))
        if i == LED_COUNT - 1:
            strip.setPixelColor(0, Color(0,0,0))
        if (i - LED_SEPERATION) % LED_COUNT < LED_COUNT:
            strip.setPixelColor((i + LED_SEPERATION)%LED_COUNT, color)
            if (i + LED_SEPERATION + 1)% LED_COUNT < LED_COUNT:
                strip.setPixelColor((i + LED_SEPERATION + 1)%LED_COUNT, Color(0,0,0))

        #time.sleep(0.25)  # Small delay to keep from spamming output messages.
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/3000.0)



def quantumlights(strip1, strip2 , color1 , color2,s1p , s2p, wait_ms = 50):
   
    if s1p != LED_COUNT - 1:
        strip1.setPixelColor(s1p+1, Color(0,0,0))
    if s2p != LED_COUNT - 1: 
        strip2.setPixelColor(s2p+1, Color(0,0,0))
    if s1p == LED_COUNT - 1:
        strip1.setPixelColor(0, Color(0,0,0))
    if s2p == LED_COUNT - 1:
        strip2.setPixelColor(0, Color(0,0,0))

    if (s1p - LED_SEPERATION) % LED_COUNT < LED_COUNT:
        strip1.setPixelColor((s1p + LED_SEPERATION)%LED_COUNT, color1)
        if (s1p + LED_SEPERATION + 1)% LED_COUNT < LED_COUNT:
            strip1.setPixelColor((s1p + LED_SEPERATION + 1)%LED_COUNT, Color(0,0,0))
            
    if (s2p - LED_SEPERATION) % LED_COUNT < LED_COUNT:
        strip2.setPixelColor((s2p + LED_SEPERATION)%LED_COUNT, color2)
        if (s2p + LED_SEPERATION + 1)% LED_COUNT < LED_COUNT:
            strip2.setPixelColor((s2p + LED_SEPERATION + 1)%LED_COUNT, Color(0,0,0))

    for j in range(12):
    # Call is_touched and pass it then number of the input.  If it's touched
    # it will return True, otherwise it will return False.
       if mpr121[j].value:
           print("Input {} touched!".format(j))
    #time.sleep(0.25)  # Small delay to keep from spamming output messages.
    strip1.setPixelColor(s1p, color1)
    strip2.setPixelColor(s2p, color2)

    strip1.show()
    strip2.show()
    time.sleep(wait_ms/3000.0)



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
    color1 = Color(255,0,0) #red
    color2 = Color(0,0,255) #blue
    s1flag = 0
    s2flag = 0
    times = 0
    try:
        s1p = strip1.numPixels() - 1
        s2p = strip2.numPixels() - 1
        while True:
            #print ('Color wipe animations.')
            if times % 100 == 0 and s1flag == 1:
                s1flag = 0
                s1p = strip1.numPixels() - 1
                s2p = strip2.numPixels() - 1 
                colorWipe(strip1, Color(0,0,0), 10)
                colorWipe(strip2, Color(0,0,0), 10)
            if s1p == -1:
                s1p = LED_COUNT - 1
            if s2p == -1:
                s2p = LED_COUNT - 1 
            quantumlights(strip1 , strip2, color1 , color2 , s1p, s2p)
            for j in range(12):
            # Call is_touched and pass it then number of the input.  If it's touched
            # it will return True, otherwise it will return False.
                if mpr121[j].value:
                   print("Input {} touched!".format(j))
                   s1flag = 1
                   times = 0
            
            if s1flag == 0:
                s1p -= 1
            if s2flag == 0:
                s2p -= 1
            times += 1
            #colorWipe(strip1, Color(255, 0, 0))  # Red wipe
            #colorWipe(strip, Color(0, 255, 0))  # Blue wipe
            #colorWipe(strip, Color(0, 0, 255))  # Green wipe
   

    except KeyboardInterrupt:
        if args.clear:
            colorWipe(strip1, Color(0,0,0), 10)
            colorWipe(strip2, Color(0,0,0), 10)
