import socket
import os
import pyglet

window = pyglet.window.Window()
window2 =pyglet.window.Window()
label = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')
label2 = pyglet.text.Label('Hell, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window2.width//2, y=window2.height//2,
                          anchor_x='center', anchor_y='center')
@window.event
def on_draw():
    window.clear()
    label.draw()
@window2.event
def on_draw2():
    window2.clear()
    label2.draw(window2)


pyglet.app.run()