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

def scene1():
    """opening scene"""
    window.blit(bg1, (0,0))
    text_box("Press Space to Continue")
    pygame.display.update()

def scene2():
    """opening scene"""
    window.blit(bg1, (0,0))
    text_box("Today is your first day at Magnet!")
    pygame.display.update()

def scene3():
    """opening scene"""
    window.blit(bg1, (0,0))
    text_box("Are you excited?")
    pygame.display.update()

def scene4():
    """opening scene"""
    window.blit(bg1, (0,0))
    text_box("well you shouldn't be!")
    pygame.display.update()

def scene5():
    """opening scene"""
    window.blit(bg1, (0,0))
    text_box("lets go!")
    pygame.display.update()

def scene6():
    """opening scene"""
    window.blit(bg1, (0,0))
    text_box("lets go!")
    pygame.display.update()

def scene7():
    """opening scene"""
    window.blit(bg2, (0,0))
    text_box("you only took one step forward?? ok i guess ://")
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
        scene1()
    elif count == 1:
        scene2()
    elif count == 2:
        scene3()
    elif count == 3:
        scene4()
    elif count == 4:
        scene5()
    elif count == 5:
        scene6()
    elif count == 6:
        scene7()

pygame.quit()
quit()