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

bg1 = pygame.image.load("campus.png")
bg2 = pygame.image.load("scene 1.png")
bg3 = pygame.image.load("scene 2.png")
bg4 = pygame.image.load("scene 3.png")
bg5 = pygame.image.load("scene 4.png")
winbg = pygame.image.load("win.png")
losebg = pygame.image.load("lose.png")
raf = pygame.image.load("raf.png")
dra = pygame.image.load("dra.png")
jeff = pygame.image.load("jeff.png")
wei = pygame.image.load("wei.png")

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
    """scene"""
    window.blit(bg1, (0,0))
    text_box("today is your first day at Magnet!")
    pygame.display.update()

def scene3():
    """scene"""
    window.blit(bg1, (0,0))
    text_box("are you excited?")
    pygame.display.update()

def scene4():
    """scene"""
    window.blit(bg1, (0,0))
    text_box("well you shouldn't be!")
    pygame.display.update()

def scene5():
    """scene"""
    window.blit(bg1, (0,0))
    text_box("lets go anyways!")
    pygame.display.update()

def scene6():
    """scene"""
    window.blit(bg2, (0,0))
    text_box("you only took one step forward?? ok i guess ://")
    pygame.display.update()

def scene7():
    """scene"""
    window.blit(bg2, (0,0))
    text_box("right next to us is the office, and then inside the office is the principal's office")
    pygame.display.update()

def scene8():
    """scene"""
    window.blit(bg2, (0,0))
    text_box("offiception??")
    pygame.display.update()

def scene9():
    """scene"""
    window.blit(bg2, (0,0))
    text_box("woah wait a second, i think i spot a wild raf in his natural habitat")
    pygame.display.update()

def scene10():
    """scene"""
    window.blit(bg2, (0,0))
    window.blit(raf, (100, 100))
    text_box("raf: H E L L O. I see you're a new student here.")
    pygame.display.update()

def scene11():
    """scene"""
    window.blit(bg2, (0,0))
    window.blit(raf, (100, 100))
    text_box("raf: i'm kind of the principal around here and as you should know we're an engineering school.")
    pygame.display.update()

def scene12():
    """scene"""
    window.blit(bg2, (0,0))
    window.blit(raf, (100, 100))
    text_box("raf: and you know what they say where there's engineering there's calc.")
    pygame.display.update()

def scene13():
    """scene"""
    window.blit(bg2, (0,0))
    window.blit(raf, (100, 100))
    text_box("you've never heard that saying before but might as well pretend")
    pygame.display.update()

def scene14():
    """scene"""
    window.blit(bg2, (0,0))
    window.blit(raf, (100, 100))
    text_box("raf: therefore, let me ask you some calc questions to see whether or not you really belong at this school.")
    pygame.display.update()

def scene15():
    """scene"""
    window.blit(bg2, (0,0))
    window.blit(raf, (100, 100))
    text_box("raf: ok so when you do a derivative, you are finding the ___ of a curve?")
    pygame.display.update()

def scene16():
    """scene"""
    window.blit(bg2, (0,0))
    window.blit(raf, (100, 100))
    text_box("raf: press 1 [slope], 2 [area], 3 [volume].")
    pygame.display.update()

def scene17():
    """scene"""
    window.blit(bg2, (0,0))
    window.blit(raf, (100, 100))
    text_box("raf: great job, lets move on to the next question")
    pygame.display.update()

def scene18():
    """scene"""
    window.blit(bg2, (0,0))
    window.blit(raf, (100, 100))
    text_box("raf: to find the antiderivative of a function, what should you do?")
    pygame.display.update()

def scene19():
    """scene"""
    window.blit(bg2, (0,0))
    window.blit(raf, (100, 100))
    text_box("raf: press 1 [derive], 2 [integrate], 3 [snap like thanos].")
    pygame.display.update()

def scene20():
    """scene"""
    window.blit(bg2, (0,0))
    window.blit(raf, (100, 100))
    text_box("raf: ahh very nice! one last question and then you can head to your classes.")
    pygame.display.update()

def scene21():
    """scene"""
    window.blit(bg2, (0,0))
    window.blit(raf, (100, 100))
    text_box("raf: what is a hole?")
    pygame.display.update()

def scene22():
    """scene"""
    window.blit(bg2, (0,0))
    window.blit(raf, (100, 100))
    text_box("press 1 [a nonremovable discontinuity], 2[a removable discontinuity], or 3[neither]")
    pygame.display.update()

def scene23():
    """scene"""
    window.blit(bg2, (0,0))
    window.blit(raf, (100, 100))
    text_box("raf: wow! you passed! I guess that this is the school for you!")
    pygame.display.update()

def scene24():
    """scene"""
    window.blit(bg2, (0,0))
    window.blit(raf, (100, 100))
    text_box("raf: i've got important principal stuff to do but good luck! you're gonna need it. bye!")
    pygame.display.update()

def scene25():
    """scene"""
    window.blit(bg2, (0,0))
    text_box("huh you should probably head to class then, it's getting kind of late")
    pygame.display.update()

def scene26():
    """scene"""
    window.blit(bg3, (0,0))
    text_box("you walk further into the school and enter a hallway")
    pygame.display.update()

def scene27():
    """scene"""
    window.blit(bg3, (0,0))
    text_box("as you're walking to class you accidentally bump into someone")
    pygame.display.update()

def scene28():
    """scene"""
    window.blit(bg3, (0,0))
    window.blit(dra, (100, 100))
    text_box("draesel: ah sorry about that, I didn't see you there")
    pygame.display.update()

def scene29():
    """scene"""
    window.blit(bg3, (0,0))
    window.blit(dra, (100, 100))
    text_box("draesel: wait a sec, i don't recognize you. are you the new student?")
    pygame.display.update()

def scene30():
    """scene"""
    window.blit(bg3, (0,0))
    window.blit(dra, (100, 100))
    text_box("draesel: it's nice to meet you, i'm a math teacher at this school")
    pygame.display.update()

def scene31():
    """scene"""
    window.blit(bg3, (0,0))
    window.blit(dra, (100, 100))
    text_box("draesel: should i ask you a few warm-up questions before you head to your calc class?")
    pygame.display.update()

def scene32():
    """scene"""
    window.blit(bg3, (0,0))
    window.blit(dra, (100, 100))
    text_box("you don't really want to but you also don't want to be rude either.")
    pygame.display.update()

def scene33():
    """scene"""
    window.blit(bg3, (0,0))
    window.blit(dra, (100, 100))
    text_box("you end up giving in because your social anxiety doesn't let you say no.")
    pygame.display.update()

def scene34():
    """scene"""
    window.blit(bg3, (0,0))
    window.blit(dra, (100, 100))
    text_box("draesel: great! here's my first question? what is the derivative of x^2?")
    pygame.display.update()

def scene35():
    """scene"""
    window.blit(bg3, (0,0))
    window.blit(dra, (100, 100))
    text_box("press 1 [2/x], 2 [x/2], or 3 [2x]")
    pygame.display.update()

def scene36():
    """scene"""
    window.blit(bg3, (0,0))
    window.blit(dra, (100, 100))
    text_box("draesel: that was an easy one! lets go onto a harder question.")
    pygame.display.update()

def scene37():
    """scene"""
    window.blit(bg3, (0,0))
    window.blit(dra, (100, 100))
    text_box("draesel: what is the indefinite integral of e^x?")
    pygame.display.update()

def scene38():
    """scene"""
    window.blit(bg3, (0,0))
    window.blit(dra, (100, 100))
    text_box("press 1 [e^x + C], 2 [e^x], or 3 [2e^x]")
    pygame.display.update()

def scene39():
    """scene"""
    window.blit(bg3, (0,0))
    window.blit(dra, (100, 100))
    text_box("draesel: holy h-e-double hockey sticks! you're on a roll! let me ask one more question.")
    pygame.display.update()

def scene40():
    """scene"""
    window.blit(bg3, (0,0))
    window.blit(dra, (100, 100))
    text_box("draesel: what is the definite integral of 3x^3 on the interval of [0,1]?")
    pygame.display.update()

def scene41():
    """scene"""
    window.blit(bg3, (0,0))
    window.blit(dra, (100, 100))
    text_box("press 1 [1], 2 [3/4], or 3 [1/4]")
    pygame.display.update()

def scene42():
    """scene"""
    window.blit(bg3, (0,0))
    window.blit(dra, (100, 100))
    text_box("draesel: excellent! if i could i would give you an A+ right now!")
    pygame.display.update()

def scene43():
    """scene"""
    window.blit(bg3, (0,0))
    window.blit(dra, (100, 100))
    text_box("draesel: i have to go but if you need anything don't hesitate to ask me! see you around :))")
    pygame.display.update()

def scene44():
    """scene"""
    window.blit(bg3, (0,0))
    text_box("what a nice person! let's keep heading to class though.")
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
    elif count == 7:
        scene8()
    elif count == 8:
        scene9()
    elif count == 9:
        scene10()
    elif count == 10:
        scene11()
    elif count == 11:
        scene12()
    elif count == 12:
        scene13()
    elif count == 13:
        scene14()
    elif count == 14:
        scene15()
    elif count == 15:
        scene16()
        if key[pygame.K_1]:
            count += 1
        elif key[pygame.K_2]:
            count == 500
        elif key[pygame.K_3]:
            count == 500
    elif count == 16:
        scene17()
    elif count == 17:
        scene18()
    elif count == 18:
        scene19()
        if key[pygame.K_1]:
            count == 500
        elif key[pygame.K_2]:
            count += 1
        elif key[pygame.K_3]:
            count == 500
    elif count == 19:
        scene20()
    elif count == 20:
        scene21()
    elif count == 21:
        scene22()
        if key[pygame.K_1]:
            count == 500
        elif key[pygame.K_2]:
            count += 1
        elif key[pygame.K_3]:
            count == 500
    elif count == 22:
        scene23()
    elif count == 23:
        scene24()
    elif count == 24:
        scene25()
    elif count == 25:
        scene26()
    elif count == 26:
        scene27()
    elif count == 27:
        scene28()
    elif count == 28:
        scene29()
    elif count == 29:
        scene30()
    elif count == 30:
        scene31()
    elif count == 31:
        scene32()
    elif count == 32:
        scene33()
    elif count == 33:
        scene34()
    elif count == 34:
        scene35()
        if key[pygame.K_1]:
            count == 500
        elif key[pygame.K_2]:
            count == 500
        elif key[pygame.K_3]:
            count += 1
    elif count == 35:
        scene36()
    elif count == 36:
        scene37()
    elif count == 37:
        scene38()
        if key[pygame.K_1]:
            count += 1
        elif key[pygame.K_2]:
            count == 500
        elif key[pygame.K_3]:
            count == 500
    elif count == 38:
        scene39()
    elif count == 39:
        scene40()
    elif count == 40:
        scene41()
        if key[pygame.K_1]:
            count == 500
        elif key[pygame.K_2]:
            count += 1
        elif key[pygame.K_3]:
            count == 500
    elif count == 41:
        scene42()
    elif count == 42:
        scene43()
    elif count == 43:
        scene44()
    elif count == 500:
        lose()

pygame.quit()
quit()