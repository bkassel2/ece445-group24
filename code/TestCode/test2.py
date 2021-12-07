import socket
import os
from _thread import *
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
# activate the pygame library
# initiate pygame and give permission
# to use pygame's functionality.
 
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
pygame.init()

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
 
# create a rectangular object for the
# text surface object

 
# infinite loop
def showscreen(texts):
    # completely fill the surface object
    # with white color
    display_surface.fill(black)
    # copying the text surface object
    # to the display surface object
    # at the center coordinate.
    display_surface.blit(texts, textRect)
    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    # for event in pygame.event.get():
    #     # if event object type is QUIT
    #     # then quitting the pygame
    #     # and program both.
    #     if event.type == pygame.QUIT:
    #         # deactivates the pygame library
    #         pygame.quit()
    #         # quit the program.
    #         quit()
    #     # Draws the surface object to the screen.
    pygame.display.update()
    print("In showscreen")



ServerSocket = socket.socket()
host = socket.gethostname()
port = 8080
ThreadCount = 0
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waitiing for a Connection..')
ServerSocket.listen(5)

text = font.render(out[1], True, purple, black)
textRect = text.get_rect()
textRect.center = (X // 2, Y // 2)
globalint = 0

def threaded_client(connection):
    connection.send(str.encode('Welcome to the Servern'))
    while True:
        data = connection.recv(2048)
        reply = data.decode('utf-8')
        print("Reached" , int(reply) % 2)
        globalint = int(reply) % 2
        print(globalint)
        text = font.render(out[int(reply) % 2], True, purple, black)
        showscreen(text)
        if not data:
            break
        # text = font.render(out[int(reply) % 2], True, purple, black)
        connection.sendall(str.encode(reply))
    connection.close()

while True:
    print(globalint)
    showscreen(text)
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSocket.close()