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
shell = pygame.image.load("Shell.png")

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
    text_box("____ : ah sorry about that, I didn't see you there. my name is mrs. draesel")
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

def scene45():
    """scene"""
    window.blit(bg4, (0,0))
    text_box("stairs? are you kidding me? i have to do physical activity?? :((((")
    pygame.display.update()
    
def scene46():
    """scene"""
    window.blit(bg4, (0,0))
    window.blit(jeff, (100,100))
    text_box("____: WOAH!!! stop right there. don't go any further.")
    pygame.display.update()

def scene47():
    """scene"""
    window.blit(bg4, (0,0))
    window.blit(jeff, (100,100))
    text_box("who is that ???")
    pygame.display.update()

def scene48():
    """scene"""
    window.blit(bg4, (0,0))
    window.blit(jeff, (100,100))
    text_box("jeff: my name is jeff tan. not jeffrey. not jefferson. not teff jan. just jeff tan.")
    pygame.display.update()

def scene49():
    """scene"""
    window.blit(bg4, (0,0))
    window.blit(jeff, (100,100))
    text_box("huh. but why can't you go to class??")
    pygame.display.update()

def scene50():
    """scene"""
    window.blit(bg4, (0,0))
    window.blit(jeff, (100,100))
    text_box("jeff: its only been your first day, but i've heard a lot about you already.")
    pygame.display.update()

def scene51():
    """scene"""
    window.blit(bg4, (0,0))
    window.blit(jeff, (100,100))
    text_box("jeff: according to some people you're some sort of math genius.")
    pygame.display.update()

def scene52():
    """scene"""
    window.blit(bg4, (0,0))
    window.blit(jeff, (100,100))
    text_box("jeff: sorry to burst your bubble but there's only enough room for one math genius at this school.")
    pygame.display.update()

def scene53():
    """scene"""
    window.blit(bg4, (0,0))
    window.blit(jeff, (100,100))
    text_box("jeff: hint: its me.")
    pygame.display.update()

def scene54():
    """scene"""
    window.blit(bg4, (0,0))
    window.blit(jeff, (100,100))
    text_box("jeff: SO I CHALLENGE YOU TO A DUEL!!!!!! i'll ask you several calc questions.")
    pygame.display.update()

def scene55():
    """scene"""
    window.blit(bg4, (0,0))
    window.blit(jeff, (100,100))
    text_box("jeff: if and only if you answer them all correctly i will admit defeat.")
    pygame.display.update()

def scene56():
    """scene"""
    window.blit(bg4, (0,0))
    window.blit(jeff, (100,100))
    text_box("jeff: are you ready?")
    pygame.display.update()

def scene57():
    """scene"""
    window.blit(bg4, (0,0))
    window.blit(jeff, (100,100))
    text_box("jeff: what theorem can be considered as Rolle's theorem but tilted?")
    pygame.display.update()

def scene58():
    """scene"""
    window.blit(bg4, (0,0))
    window.blit(jeff, (100,100))
    text_box("press 1 [intermediate value theorem], 2 [mean value theorem], or 3 [extreme value theorem]")
    pygame.display.update()

def scene59():
    """scene"""
    window.blit(bg4, (0,0))
    window.blit(jeff, (100,100))
    text_box("jeff: AAAA NO!! IT'S OK I STILL HAVE 2 MORE TRIES TO DEFEAT YOU !!!")
    pygame.display.update()

def scene60():
    """scene"""
    window.blit(bg4, (0,0))
    window.blit(jeff, (100,100))
    text_box("jeff: When the function is concave down the slope is _____ ?")
    pygame.display.update()

def scene61():
    """scene"""
    window.blit(bg4, (0,0))
    window.blit(jeff, (100,100))
    text_box("press 1 [decreasing], 2 [increasing], or 3 [constant]")
    pygame.display.update()

def scene62():
    """scene"""
    window.blit(bg4, (0,0))
    window.blit(jeff, (100,100))
    text_box("jeff: HOW DID YOU KNOW THAT? I GUESS I'LL HAVE TO PULL PUT THE BIG GUNS FOR THIS LAST QUESTION!!")
    pygame.display.update()

def scene63():
    """scene"""
    window.blit(bg4, (0,0))
    window.blit(jeff, (100,100))
    text_box("jeff: how would you find out where the function is increasing, decreasing, or constant?")
    pygame.display.update()

def scene64():
    """scene"""
    window.blit(bg4, (0,0))
    window.blit(jeff, (100,100))
    text_box("press 1 [first derivative test], 2 [disk method], 3 [by jumping up and down until you become one with the function]")
    pygame.display.update()

def scene65():
    """scene"""
    window.blit(bg4, (0,0))
    window.blit(jeff, (100,100))
    text_box("NANI???!!!??? HOW COULD THIS BE?????? I'VE BEEN BEATEN,,,,,")
    pygame.display.update()

def scene66():
    """scene"""
    window.blit(bg4, (0,0))
    text_box("he fades into dust. you're confused but it's 7:59. you have one minute to get to class. you better hurry.")
    pygame.display.update()

def scene67():
    """scene"""
    window.blit(bg5, (0,0))
    text_box("you walk up the stairs and go through the doors. you're right in front of your calc class!")
    pygame.display.update()

def scene68():
    """scene"""
    window.blit(bg5, (0,0))
    text_box("suddenly a man appears")
    pygame.display.update()

def scene69():
    """scene"""
    window.blit(bg5, (0,0))
    window.blit(wei, (100,100))
    text_box("____: hello! my name is Mr. Weisser! i'm your calculus teacher!")
    pygame.display.update()

def scene70():
    """scene"""
    window.blit(bg5, (0,0))
    window.blit(wei, (100,100))
    text_box("Mr. Weisser: before you enter class i'm going to challenge you to something i only offer new students")
    pygame.display.update()

def scene71():
    """scene"""
    window.blit(bg5, (0,0))
    window.blit(wei, (100,100))
    text_box("Mr. Weisser: basically i'll give you a small quiz. if you get them all right i lose and if you don't i win.")
    pygame.display.update()

def scene72():
    """scene"""
    window.blit(bg5, (0,0))
    window.blit(wei, (100,100))
    text_box("Mr. Weisser: if you beat the teacher (me) you become the teacher")
    pygame.display.update()

def scene73():
    """scene"""
    window.blit(bg5, (0,0))
    window.blit(wei, (100,100))
    text_box("Mr. Weisser: let's start! What method uses this formula?")
    window.blit(shell, (600, 390))
    pygame.display.update()

def scene74():
    """scene"""
    window.blit(bg5, (0,0))
    window.blit(wei, (100,100))
    text_box("press 1 [disk], 2 [washer], or 3 [shell]")
    pygame.display.update()

def scene75():
    """scene"""
    window.blit(bg5, (0,0))
    window.blit(wei, (100,100))
    text_box("Mr. Weisser: great job! next question: What is the 'opposite' of the chain rule?")
    pygame.display.update()

def scene76():
    """scene"""
    window.blit(bg5, (0,0))
    window.blit(wei, (100,100))
    text_box("press 1 [change of bounds], 2 [u sub], or 3 [quotient rule]")
    pygame.display.update()

def scene77():
    """scene"""
    window.blit(bg5, (0,0))
    window.blit(wei, (100,100))
    text_box("Mr. Weisser: im actually getting kind of nervous;;; but i'm the final boss you can't win!!")
    pygame.display.update()

def scene78():
    """scene"""
    window.blit(bg5, (0,0))
    window.blit(wei, (100,100))
    text_box("Mr. Weisser: What is the indefinite integral of 1/x or x^-1?")
    pygame.display.update()

def scene79():
    """scene"""
    window.blit(bg5, (0,0))
    window.blit(wei, (100,100))
    text_box("press 1 [loglxl + C], 2 [lnlxl], or 3 [lnlxl + C]")
    pygame.display.update()

def scene80():
    """scene"""
    window.blit(bg5, (0,0))
    window.blit(wei, (100,100))
    text_box("Mr. Weisser: great job but i kind of can't let you just take my job.")
    pygame.display.update()

def scene81():
    """scene"""
    window.blit(bg5, (0,0))
    window.blit(wei, (100,100))
    text_box("Mr. Weisser: what if i give you a win screen instead??")
    pygame.display.update()

def scene82():
    """scene"""
    window.blit(bg5, (0,0))
    window.blit(wei, (100,100))
    text_box("ok.")
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
            lose()
        elif key[pygame.K_3]:
            lose()
    elif count == 16:
        scene17()
    elif count == 17:
        scene18()
    elif count == 18:
        scene19()
        if key[pygame.K_1]:
            lose()
        elif key[pygame.K_2]:
            count += 1
        elif key[pygame.K_3]:
            lose()
    elif count == 19:
        scene20()
    elif count == 20:
        scene21()
    elif count == 21:
        scene22()
        if key[pygame.K_1]:
            lose()
        elif key[pygame.K_2]:
            count += 1
        elif key[pygame.K_3]:
            lose()
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
            lose()
        elif key[pygame.K_2]:
            lose()
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
            lose()
        elif key[pygame.K_3]:
            lose()
    elif count == 38:
        scene39()
    elif count == 39:
        scene40()
    elif count == 40:
        scene41()
        if key[pygame.K_1]:
            lose()
        elif key[pygame.K_2]:
            count += 1
        elif key[pygame.K_3]:
            lose()
    elif count == 41:
        scene42()
    elif count == 42:
        scene43()
    elif count == 43:
        scene44()
    elif count == 44:
        scene45()
    elif count == 45:
        scene46()
    elif count == 46:
        scene47()
    elif count == 47:
        scene48()
    elif count == 48:
        scene49()
    elif count == 49:
        scene50()
    elif count == 50:
        scene51()
    elif count == 51:
        scene52()
    elif count == 52:
        scene53()
    elif count == 53:
        scene54()
    elif count == 54:
        scene55()
    elif count == 55:
        scene56()
    elif count == 56:
        scene57()
    elif count == 57:
        scene58()
        if key[pygame.K_1]:
            lose()
        elif key[pygame.K_2]:
            count += 1
        elif key[pygame.K_3]:
            lose()
    elif count == 58:
        scene59()
    elif count == 59:
        scene60()
    elif count == 60:
        scene61()
        if key[pygame.K_1]:
            count += 1
        elif key[pygame.K_2]:
            lose()
        elif key[pygame.K_3]:
            lose()
    elif count == 61:
        scene62()
    elif count == 62:
        scene63()
    elif count == 63:
        scene64()
        if key[pygame.K_1]:
            count += 1
        elif key[pygame.K_2]:
            lose()
        elif key[pygame.K_3]:
            lose()
    elif count == 64:
        scene65()
    elif count == 65:
        scene66()
    elif count == 66:
        scene67()
    elif count == 67:
        scene68()
    elif count == 68:
        scene69()
    elif count == 69:
        scene70()
    elif count == 70:
        scene71()
    elif count == 71:
        scene72()
    elif count == 72:
        scene73()
    elif count == 73:
        scene74()
        if key[pygame.K_1]:
            lose()
        elif key[pygame.K_2]:
            lose()
        elif key[pygame.K_3]:
            count += 1
    elif count == 74:
        scene75()
    elif count == 75:
        scene76()
        if key[pygame.K_1]:
            lose()
        elif key[pygame.K_2]:
            count += 1
        elif key[pygame.K_3]:
            lose()
    elif count == 76:
        scene77()
    elif count == 77:
        scene78()
    elif count == 78:
        scene79()
        if key[pygame.K_1]:
            lose()
        elif key[pygame.K_2]:
            lose()
        elif key[pygame.K_3]:
            count += 1
    elif count == 79:
        scene80()
    elif count == 80:
        scene81()
    elif count == 81:
        scene82()
    elif count == 82:
        win()

pygame.quit()
quit()