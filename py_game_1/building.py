import pygame
Black = (0,0,0)
class Building:
    def __init__(self,screen):
        self.screen = screen
    def display(self,x,y):
        pygame.draw.rect(self.screen,Black,(x, y, 100, 200),3)
        pygame.draw.rect(self.screen, Black, (x+25, y+125, 50, 75))