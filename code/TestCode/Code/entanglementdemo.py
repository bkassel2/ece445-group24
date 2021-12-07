import socket
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

import time
from rpi_ws281x import *
import argparse
import board
import busio
import adafruit_mpr121
import numpy as np
import random
# Create I2C bus.
i2c = busio.I2C(board.SCL, board.SDA)

# Create MPR121 object.
mpr121 = 0
mpr1212 = 0
mpr121 = adafruit_mpr121.MPR121(i2c , address = 0x5b)
mpr1212 = adafruit_mpr121.MPR121(i2c , address = 0x5a)

LED_SEPERATION = 20     #Seperation in  4 pixel per inch 
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
SPEED          = 2000.0


COLOR0 = "colormeasurment0".encode()
COLOR1 = "colormeasurment1".encode()
POS0 = "positionmeasurement0".encode()
POS1 = "positionmeasurement1".encode()
RESET = "rest".encode()


# activate the pygame library
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()
 
# define the RGB value for white,
#  green, blue colour .
out = ['   ', '0' , '1']
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 128, 128)
red = (255,0,0)
purple = (128,0,128)
black = (0,0,0)
# assigning values to X and Y variable
X = 500
Y = 500

# create the display surface object
# of specific dimension..e(X, Y).
display_surface = pygame.display.set_mode((X, Y))
 
# set the pygame window name
# pygame.display.set_caption('Show Text')
 
# create a font object.
# 1st parameter is the font file
# which is present in pygame.
# 2nd parameter is size of the font
font = pygame.font.Font('freesansbold.ttf', 128)
 
# create a text surface object,
# on which text is drawn on it.
text = font.render(out[0], True, purple, black)
 
# create a rectangular object for the
# text surface object
textRect = text.get_rect()
 
# set the center of the rectangular object.
textRect.center = (X // 2, Y // 2)
 
# infinite loop
def showscreen(texts):
    # completely fill the surface object
    # with white color
    # display_surface.fill(black)
    # copying the text surface object
    # to the display surface object
    # at the center coordinate.
    # print("Hi")
    display_surface.blit(texts, textRect)
    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get():
        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.QUIT:
            # deactivates the pygame library
            pygame.quit()
            # quit the program.
            quit()
        # Draws the surface object to the screen.
        pygame.display.update()



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
if mpr121:    
    def s1touch(s1):
        pos = -1
        if s1 >= 8 and s1 <= 144+8:
            pos = (s1 - 8) // 8
        pos1measurement = 0
        color1measurement = 0
        s1touch = np.zeros(12)
        for i in range(12):
            # Call is_touched and pass it then number of the input.  If it's touched
            # it will return True, otherwise it will return False.
            if mpr121[i].value:
                s1touch[i] = 1
        # print(pos , (pos + LED_SEPERATION//8))
        for i in range(LED_SEPERATION//8//2):
            for j in range(LED_SEPERATION//8 // 2):
                if s1touch[(pos + i)%12] == 1 and s1touch[(pos + j + LED_SEPERATION//8)%12] == 1 and pos!= -1:
                    pos1measurement = 1
        print(s1touch)
        # print(sum(s1touch))
        # print(s1touch[0])
        for i in range(LED_SEPERATION // 8 //2):
            if pos + i + 2 < 12:
                if (s1touch[(pos+ i + 2)] and sum(s1touch) == 1):
                    color1measurement = 1
        # print (pos , (pos + LED_SEPERATION // 8)%24)
        return pos1measurement , color1measurement

s2touch = np.zeros(12)
if mpr1212:
    def s2touch(s1):
        pos = -1
        if s1 >= 8 and s1 <= 144+8:
            pos = (s1 - 8) // 8
        pos1measurement = 0
        color1measurement = 0
        s2touch = np.zeros(12)
        for i in range(12):
            # Call is_touched and pass it then number of the input.  If it's touched
            # it will return True, otherwise it will return False.
            if mpr1212[i].value:
                s2touch[i] = 1
        # print(pos , (pos + LED_SEPERATION//8))
        for i in range(LED_SEPERATION//8//2):
            for j in range(LED_SEPERATION//8 // 2):
                if s2touch[(pos + i)%12] == 1 and s2touch[(pos + j + LED_SEPERATION//8)%12] == 1 and pos!= -1:
                    pos1measurement = 1
        # print(s2touch)
        # print(sum(s1touch))
        # print(s1touch[0])
        for i in range(LED_SEPERATION // 8 //2):
            if pos + i + 2 < 12:
                if (s2touch[(pos+ i + 2)] and sum(s2touch) == 1):
                    color1measurement = 1
        # print (pos , (pos + LED_SEPERATION // 8)%24)
        return pos1measurement , color1measurement


purple = Color(128,0,128)
red = Color(255,0,0)
blue = Color(0,0,255)
black = Color(0,0,0)


def server():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip1 = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip2 = Adafruit_NeoPixel(LED_COUNT, LED_PIN2, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL2)
    # Intialize the library (must be called once before other functions).
    strip1.begin()
    strip2.begin()

    host = socket.gethostname()   # get local machine name
    port = 8000  # Make sure it's within the > 1024 $$ <65535 range
    port2 = 5000
    s = socket.socket()
    s.bind((host, port))
    s2 = socket.socket()
    s2.bind((host, port2))
    s.listen(5)
    s2.listen(5)
    Monitor2, addr2 = s2.accept()
    Monitor1, addr = s.accept()
    print("Connection from: " + str(addr))
    print("Connection from: " + str(addr2))
    Monitor1.setblocking(0)
    Monitor2.setblocking(0)
    prev = -1
    prev2 = -1


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
    s1p = LED_COUNT - LED_SEPERATION - 1
    s2p = LED_COUNT - LED_SEPERATION - 1


    while True:
        try:
            if (times % 50 == 0 or s2p == LED_COUNT - LED_SEPERATION )and s1flag == 1 :
                print("reached")
                s1flag = 0
                s2flag = 0
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
                Monitor1.send(RESET)
                Monitor2.send(RESET)
            if (times % 50 == 0 or s1p == LED_COUNT - LED_SEPERATION )and s2flag == 1 :
                print("reached")
                s1flag = 0
                s2flag = 0
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
                Monitor1.send(RESET)
                Monitor2.send(RESET)
            

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
            # color1 = blue
            quantumlights(strip1 , strip2, color1 , color2 ,color3 , color4, s1p, s2p)

            pos1f , color1f = s1touch(s1p)
            if color1f and not s1flag:
                if firstmeasurent:
                    x = random.randint(0,10000) % 2
                    firstmeasurent = 0
                    firsttype = 0
                    if x:
                        color1 = color2 =red
                        c1f = 0
                        Monitor1.send(COLOR0)
                    else:
                        color1 = color2 =blue
                        c1f = 1
                        Monitor1.send(COLOR1)
                elif firsttype == 0:
                    if c2f:
                        color1 = color2 =red
                        Monitor1.send(COLOR0)
                    else:
                        color1 = color2 =blue
                        Monitor1.send(COLOR1)
                else:
                    x = random.randint(0,10000) % 2
                    if x:
                        color1 = color2 =red
                        Monitor1.send(COLOR0)
                    else:
                        color1 = color2 =blue
                        Monitor1.send(COLOR1)
                p1 = s1p
                s1flag = 1
                times = 1
            if pos1f and not s1flag:
                if firstmeasurent:
                    x = random.randint(0,10000) % 2
                    firstmeasurent = 0
                    firsttype = 1
                    if x:
                        color1 = black
                        p1f = 0
                        Monitor1.send(POS0)
                    else:
                        color2 = black
                        p1f = 1
                        Monitor1.send(POS1)
                elif firsttype == 1:
                    if p2f:
                        color1 = black
                        Monitor1.send(POS0)
                    else:
                        color2 = black
                        Monitor1.send(POS1)
                else:
                    x = random.randint(0,10000) % 2
                    if x:
                        color1 = black
                        Monitor1.send(POS0)
                    else:
                        color2 = black
                        Monitor1.send(POS1)
                p1 = s1p
                s1flag = 1
                times = 1
            pos2f , color2f = s2touch(s2p) 
            if color2f and not s2flag:
                if firstmeasurent:
                    x = random.randint(0,10000) % 2
                    firstmeasurent = 0
                    firsttype = 0
                    if x:
                        color3 = color4 =red
                        c2f = 0
                        Monitor2.send(COLOR0)
                    else:
                        color3 = color4 =blue
                        c2f = 1
                        Monitor2.send(COLOR1)
                elif firsttype == 0:
                    if c1f:
                        color3 = color4 =red
                        Monitor2.send(COLOR0)
                    else:
                        color3 = color4 =blue
                        Monitor2.send(COLOR1)
                else:
                    x = random.randint(0,10000) % 2
                    if x:
                        color3 = color4 =red
                        Monitor2.send(COLOR0)
                    else:
                        color3 = color4 =blue
                        Monitor2.send(COLOR1)
                p2 = s2p
                s2flag = 1
                times = 1
            if pos2f and not s2flag:
                if firstmeasurent:
                    x = random.randint(0,10000) % 2
                    firstmeasurent = 0
                    firsttype = 1
                    if x:
                        color3 = black
                        p2f = 0
                        Monitor2.send(POS0)
                    else:
                        color4 = black
                        p2f = 1
                        Monitor2.send(POS1)
                elif firsttype == 1:
                    if p1f:
                        color3 = black
                        Monitor2.send(POS0)
                    else:
                        color4 = black
                        Monitor2.send(POS1)
                else:
                    x = random.randint(0,10000) % 2
                    if x:
                        color3 = black
                        Monitor2.send(POS0)
                    else:
                        color4 = black
                        Monitor2.send(POS1)
                p2 = s2p
                s2flag = 1
                times = 1

            if s1flag == 0:
                s1p -= 1
            if s2flag == 0:
                s2p -= 1
            times += 1
            # if Monitor2.recv(1024) == "Done".encode() or Monitor1.recv(1024) == "Done".encode():
            #     Monitor1.send("Quit".encode())
            #     Monitor2.send("Quit".encode())
            #     Monitor1.close()
            #     Monitor2.close()
            #     colorWipe(strip1, Color(0,0,0), 1)
            #     colorWipe(strip2, Color(0,0,0), 1)
            #     break
        except KeyboardInterrupt:
            Monitor1.send("Quit".encode())
            Monitor2.send("Quit".encode())
            Monitor1.close()
            Monitor2.close()
            colorWipe(strip1, Color(0,0,0), 1)
            colorWipe(strip2, Color(0,0,0), 1)
            break



if __name__ == '__main__':
    server()