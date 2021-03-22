import pygame
Silver	=	(192,192,192)
class Mountain:
    def __init__(self,screen,):
        self.screen = screen
    def display(self):
        pygame.draw.polygon(self.screen, Silver,((0, 450), (150, 300), (400, 400), (620, 300), (800, 415), (800, 600), (0, 600)))