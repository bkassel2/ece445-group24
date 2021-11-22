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
out = ['   ', '0' , '1']
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
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





def client():
    host = socket.gethostname()  # get local machine name
    port = 8004  # Make sure it's within the > 1024 $$ <65535 range

    s = socket.socket()
    s.connect((host, port))
    s.setblocking(0)
    message = 0
    prev = 0
    timer = 1000
    while message != 'q':
        # s.send(message.encode('utf-8'))
        try:
            data = s.recv(1024).decode('utf-8')
            message = data
            if message == 'q':
                break
            print(message , int(message) % 3)
            event = pygame.event.Event(pygame.KEYUP, key=pygame.K_r)
            pygame.event.post(event)
        except BlockingIOError:
            data = 0
        
        showscreen(font.render(out[int(message) % 3], True, purple, black))

        # print('Received from server: ' + data)
        # message = input('==> ')s
    s.close()

if __name__ == '__main__':
    client()