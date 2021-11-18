import socket
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import board
import busio
import adafruit_mpr121
import numpy as np
import adafruit_mpr121
import time
# Create I2C bus.
i2c = busio.I2C(board.SCL, board.SDA)

# Create MPR121 object.
mpr121 = adafruit_mpr121.MPR121(i2c , address = 0x5a)

def server():
    host = socket.gethostname()   # get local machine name
    port = 8004  # Make sure it's within the > 1024 $$ <65535 range
    port2 = 5004
    s = socket.socket()
    s.bind((host, port))
    s2 = socket.socket()
    s2.bind((host, port2))
    s.listen(5)
    s2.listen(5)
    c2, addr2 = s2.accept()
    c, addr = s.accept()
    print("Connection from: " + str(addr))
    print("Connection from: " + str(addr2))
    c.setblocking(0)
    c2.setblocking(0)
    prev = -1
    prev2 = -1
    while True:
        try:
            for i in range(12):
                # Call is_touched and pass it then number of the input.  If it's touched
                # it will return True, otherwise it will return False.
                if mpr121[i].value:
                    print("Input {} touched!".format(i))
                    if i >= 6:
                        if i == prev:
                            continue
                        c2.send(str(i).encode('utf-8'))
                        prev = i
                        continue
                    else:
                        if i == prev2:
                            continue
                        c.send(str(i).encode('utf-8'))
                        prev2 = i
            # try:
            #   data = c.recv(1024).decode('utf-8')
            # except BlockingIOError:
            #   data = 0
            # try:
            #   data2 = c2.recv(1024).decode('utf-8')
            # except BlockingIOError:
            #   data2 = 0
            # if data:
            #   print('From online user: ' + data)
            #   data = data.upper()
            #   prev = int(data) % 2
            #   c.send(data.encode('utf-8'))
            #   event = pygame.event.Event(pygame.KEYUP, key=pygame.K_r)
            #   pygame.event.post(event)
            # if data2:
            #   print('From online user: ' + data2)
            #   data2 = data2.upper()
            #   prev = int(data2) % 2
            #   c2.send(data2.encode('utf-8'))
            #   event = pygame.event.Event(pygame.KEYUP, key=pygame.K_r)
            #   pygame.event.post(event)
            # showscreen(font.render(out[prev], True, purple, black))
        except KeyboardInterrupt:
            c2.send(str('q').encode('utf-8'))
            c.send(str('q').encode('utf-8'))
            c.close()
            c2.close()
            break
if __name__ == '__main__':
    server()