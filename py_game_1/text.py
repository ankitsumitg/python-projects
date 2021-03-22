import pygame
class Text:
    def __init__(self,screen,color):
        self.screen = screen
        self.color = color
    def display(self,text,x,y):
        font = pygame.font.Font('freesansbold.ttf', 25)
        text = font.render(text, True, self.color)
        self.screen.blit(text, (x,y))
