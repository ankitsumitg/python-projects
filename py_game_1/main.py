#import statements
import sys
import pygame
from sun import *
from cloud import *
from text import *
from bird import *
from mountain import *
from building import *
from colors import *


# Intialize the pygame
pygame.init()
# Set window size
size   = width, height = 800, 600
screen = pygame.display.set_mode(size)

# Setting title and Icon for the game
pygame.display.set_caption('Shapes Illustrate')
icon = pygame.image.load('cube.png')
pygame.display.set_icon(icon)

# Loading Image
# Bird Picture
birdpic = pygame.image.load('bird.png')

# creating objects to display
sun      = Sun(screen, Yellow)
cloud    = Cloud(screen, Blue)
text     = Text(screen, Black)
bird     = Bird(screen)
mountain = Mountain(screen)
building = Building(screen)

# Starting the game
# Showing the window of the Game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(Cyan)
    mountain.display()
    building.display(600, 250)
    bird.display(50, 50)
    bird.display(110, 50)
    bird.display(75, 75)
    cloud.display(200, 110)
    cloud.display(250, 75)
    sun.display(700, 100)
    text.display('Birds', 75, 100)
    text.display('Clouds', 300, 110)
    text.display('Sun', 680, 90)
    text.display('Mountain', 100, 400)
    text.display('Building', 600, 460)
    x, y = pygame.mouse.get_pos()
    screen.blit(birdpic, (x-30, y-60))
    text.display('Make me fly', x-60, y)
    pygame.display.update()
