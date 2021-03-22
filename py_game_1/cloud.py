import pygame
class Cloud:
    def __init__(self,screen,color):
        self.screen = screen
        self.color = color
    def display(self,x,y):
        pygame.draw.ellipse(self.screen, self.color, (x, y,150,70))
        pygame.draw.ellipse(self.screen, self.color, (x+100, y, 150, 70))