import pygame
class Sun:
    def __init__(self,screen,color):
        self.screen = screen
        self.color = color
    def display(self,x,y):
        pygame.draw.circle(self.screen, self.color, (x, y), 60)