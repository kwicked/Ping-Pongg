from random import randint
from pygame import *

win_width = 700
win_height = 500

FPS = 60

clock = time.Clock()
window = display.set_mode((win_width, win_height))
display.set_caption('Ping-Pong!')
background = transform.scale(image.load('cool_cat.jpg'),(win_width, win_height))
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.blit(background, (0,0))
    display.update()
    time.delay(50)