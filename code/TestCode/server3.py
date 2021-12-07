import socket
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

# activate the pygame library
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()
 
# define the RGB value for white,
#  green, blue colour .
out = ['0' , '1']
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
red = (255,0,0)
purple = (128,0,128)
black = (0,0,0)
# assigning values to X and Y variable
X = 1000
Y = 1000

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
 
UPSCREEN = pygame.event.custom_type()

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








def server():
  host = socket.gethostname()   # get local machine name
  port = 8000  # Make sure it's within the > 1024 $$ <65535 range
  port2 = 5000
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
  prev = 0
  while True:

    try:
      data = c.recv(1024).decode('utf-8')
    except BlockingIOError:
      data = 0
    try:
      data2 = c2.recv(1024).decode('utf-8')
    except BlockingIOError:
      data2 = 0
    if data:
      print('From online user: ' + data)
      data = data.upper()
      prev = int(data) % 2
      c.send(data.encode('utf-8'))
      event = pygame.event.Event(pygame.KEYUP, key=pygame.K_r)
      pygame.event.post(event)
    if data2:
      print('From online user: ' + data2)
      data2 = data2.upper()
      prev = int(data2) % 2
      c2.send(data2.encode('utf-8'))
      event = pygame.event.Event(pygame.KEYUP, key=pygame.K_r)
      pygame.event.post(event)
    showscreen(font.render(out[prev], True, purple, black))
  c.close()
  c2.close()
if __name__ == '__main__':
    server()