import pygame,math
Black	=	(0,0,0)
class Bird:
    def __init__(self,screen):
        self.screen = screen
    def display(self,x,y):
        pygame.draw.arc(self.screen, Black, (x, y, 25, 25),0,math.pi,2)
        pygame.draw.arc(self.screen, Black, (x+25, y, 25, 25),0,math.pi,2)