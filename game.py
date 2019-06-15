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

bg1 = pygame.image.load("campus.png")
bg2 = pygame.image.load("scene 1.png")
bg3 = pygame.image.load("scene 2.png")
bg4 = pygame.image.load("scene 3.png")
bg5 = pygame.image.load("scene 4.png")
winbg = pygame.image.load("win.png")
losebg = pygame.image.load("lose.png")


def text_objects(text, font, color):
    """displays text"""
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def text_box(text):
    """displays text in a text box similar to those of classic games"""

    pygame.draw.rect(window, black, (50, 350, 750, 140))
    pygame.draw.rect(window, white, (55, 355, 740, 130))
    pygame.draw.rect(window, black, (60, 360, 730, 120))

    smallText = pygame.font.SysFont("comicsansms",20)
    TextSurf, TextRect = text_objects(text, smallText, white)
    TextRect.center = (415, 415)
    window.blit(TextSurf, TextRect)

def win():
    """screen if they win the game"""
    window.blit(winbg, (0,0))
    pygame.display.update()
    
def lose():
    """sceen if they lose the game"""
    window.blit(losebg, (0,0))
    pygame.display.update()

def scene():
    """opening scene"""
    window.blit(bg1, (0,0))
    text_box("test test")
    pygame.display.update()

    
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
        win()

pygame.quit()
quit()