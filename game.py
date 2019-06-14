import pygame
import time
import random

pygame.init()

window_width = 850
window_height = 500

window = pygame.display.set_mode((window_width, window_height))

pygame.display.set_caption("calc is a thing ig")

black = (0,0,0)
white = (255, 255, 255)

clock = pygame.time.Clock()

count = 0

class Player:
    """defining player characteristics"""
    def __init__(self, name, atk, hp):
        self.name = name
        self.atk = 10
        self.hp = 30

class Enemy:
    """defining generic enemy class"""
    def __init__(self, name, atk, hp):
        self.name = name
        self.atk = atk
        self.hp = hp

back = pygame.image.load("campus.png")

def text_objects(text, font, color):
    """displays text"""
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def text_box(text):
    """displays text in a text box similar to those of classic games"""

    pygame.draw.rect(window, black, (50, 400, 700, 150))
    pygame.draw.rect(window, white, (55, 405, 690, 140))
    pygame.draw.rect(window, black, (60, 410, 680, 130))

    smallText = pygame.font.SysFont("comicsansms",10)
    TextSurf, TextRect = text_objects(text, smallText, white)
    TextRect.center = (400, 475)
    window.blit(TextSurf, TextRect)
    
run = False

while not run:
    clock.tick(4)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = True

    key = pygame.key.get_pressed()

    if key[pygame.K_SPACE]:
        count += 1

    if count == 0:
        window.blit(back, (0,0))
        text_box("test test")
        pygame.display.update()

pygame.quit()
quit()