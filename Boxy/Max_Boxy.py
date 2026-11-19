'''
Author:
    Max Epstein
Project title:
    Box Chaser/Boxy
Use:
    Use WASD or arrow keys to move the box around the screen and collect biscuts.
    Easy game_mode/pt game_mode: Box increases speed as you collect biscuts. If you hit the wall, you lose.
    Hard game_mode/grad game_mode: Box increases speed by increasing the rate that speed is increased as you collect more biscuts.
    If you the wall, you loose. Score is displayed at the end of the game.
Bugs:
    None known.
To do/Changes:
    [ ] Introduce a way to restart the game after losing.
    [ ] Introduce baby game_mode where box does not increase speed and you can play forever without losing.
    [ ] Make Fancy rects - draw surface ontop of rects

'''


import pygame
import random
import time

pygame.init()                                                                                                                                                                                                                                                                                                                                                                                                       #Max Epstein's code

#-------------------------------
#Screen definition and setup
#-------------------------------

screen_width = 800
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
game_icon = pygame.image.load(r"C:\Users\mepstein30\Documents\CS1+\Boxy\Box.png")
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Boxy")

with open(r"C:\Users\mepstein30\Documents\CS1+\Boxy\HardModeScore", 'r+') as doc:
    hard_mode_score =int(doc.read())
    doc.seek(0)
    doc.truncate()
with open(r"C:\Users\mepstein30\Documents\CS1+\Boxy\EasyModeScore", 'r+') as doc:
    easy_mode_score = int(doc.read())
    doc.seek(0)
    doc.truncate()

#-----------------------
#Player and Rect definition
#-----------------------
boxy = pygame.Rect((400,400), (50,50))
box_icon = pygame.image.load(r"C:\Users\mepstein30\Documents\CS1+\Boxy\Box.png")
biscut_icon = pygame.image.load(r"C:\Users\mepstein30\Documents\CS1+\Boxy\Biscut.png")

biscut0 = pygame.Rect((random.randint(1, 15)*50, random.randint(1, 15)*50), (50,50))
biscut1 = pygame.Rect((random.randint(1, 15)*50, random.randint(1, 15)*50), (50,50))
biscut2 = pygame.Rect((random.randint(1, 15)*50, random.randint(1, 15)*50), (50,50))
biscut3 = pygame.Rect((random.randint(1, 15)*50, random.randint(1, 15)*50), (50,50))
biscut4 = pygame.Rect((random.randint(1, 15)*50, random.randint(1, 15)*50), (50,50))

#-----------------------
#Game variables
#-----------------------
clock = pygame.time.Clock()
boxy_direction = None
score = 0
frame_rate = 20
tick_count = 0
tick_count_step_by = 5
game_mode = None
screen_color = "grey71"
biscut_color = "indianred4"
box_color = "seagreen"
handle_stop = None

intro_text = pygame.font.SysFont(None, 36).render("Move box left for easy mode \n and right for hard mode", True, (0,0,0))

#---------------
#Running Loop - allows the game to run until the user quits or loses
#---------------
Running = True
while Running:
    key = pygame.key.get_pressed()

    #---------------------------------------------
    # KEYBOARD INPUTS
    #---------------------------------------------
    if key[pygame.K_a] or key[pygame.K_LEFT]:
        if boxy_direction != 1:
            boxy_direction = 0

    if key[pygame.K_d] or key[pygame.K_RIGHT]:
        if boxy_direction != 0:
            boxy_direction = 1

    if key[pygame.K_w] or key[pygame.K_UP]:
        if boxy_direction != 3:
            boxy_direction = 2

    if key[pygame.K_s] or key[pygame.K_DOWN]:
        if boxy_direction != 2:
            boxy_direction = 3

    if key[pygame.K_RETURN]:
        handle_stop = True

    #---------------------------------------------
    #Backround color based on game mode selection
    #---------------------------------------------

    if game_mode == None:
        if boxy.center < (300,400):
            game_mode = "pt"
            screen_color = "darkolivegreen1"
        elif boxy.center > (500,400):
            game_mode = "grad"
            screen_color = "cadetblue1"

    # ---------------------------------------------
    #Boxy and biscut collision detection
    #---------------------------------------------

    if boxy.top < biscut0.bottom and boxy.bottom > biscut0.top and boxy.left < biscut0.right and boxy.right > biscut0.left:
                biscut0 = pygame.Rect((random.randint(1, 15)*50, random.randint(1, 15)*50), (50,50))
                score += 1
    elif boxy.top < biscut1.bottom and boxy.bottom > biscut1.top and boxy.left < biscut1.right and boxy.right > biscut1.left:
                biscut1 = pygame.Rect((random.randint(1, 15)*50, random.randint(1, 15)*50), (50,50))
                score += 1
    elif boxy.top < biscut2.bottom and boxy.bottom > biscut2.top and boxy.left < biscut2.right and boxy.right > biscut2.left:
                biscut2 = pygame.Rect((random.randint(1, 15)*50, random.randint(1, 15)*50), (50,50))
                score += 1
    elif boxy.top < biscut3.bottom and boxy.bottom > biscut3.top and boxy.left < biscut3.right and boxy.right > biscut3.left:
                biscut3 = pygame.Rect((random.randint(1, 15)*50, random.randint(1, 15)*50), (50,50))
                score += 1
    elif boxy.top < biscut4.bottom and boxy.bottom > biscut4.top and boxy.left < biscut4.right and boxy.right > biscut4.left:
                biscut4 = pygame.Rect((random.randint(1, 15)*50, random.randint(1, 15)*50), (50,50))
                score += 1
    else:
          update_frame_rate = False
    if boxy.left < 0 or boxy.top < 0 or boxy.right > screen_width or boxy.bottom > screen_height:
                handle_stop = True

    #---------------------------------------------
    #Score text for dispay at the end of the game/save to logs
    #---------------------------------------------

    score_text = pygame.font.SysFont(None, 36).render(f"Score: {score}", True, "black")
    if game_mode == "grad" and score > hard_mode_score:
        hard_mode_score = score
    elif game_mode == "pt" and score > easy_mode_score:
        easy_mode_score = score
    open(r"C:\Users\mepstein30\Documents\CS1+\Boxy\HardModeScore", 'w+').write(str(hard_mode_score))
    open(r"C:\Users\mepstein30\Documents\CS1+\Boxy\EasyModeScore", 'w+').write(str(easy_mode_score))

    #------------------------------
    #Screen Drawing and updates
    #------------------------------
    screen.fill(screen_color)

    #pygame.draw.rect(screen, box_color, boxy)
    screen.blit(box_icon, boxy)

    if game_mode == "pt" or game_mode == "grad":
        screen.blit(biscut_icon, biscut0)
        screen.blit(biscut_icon, biscut1)
        screen.blit(biscut_icon, biscut2)
        screen.blit(biscut_icon, biscut3)
        screen.blit(biscut_icon, biscut4)
        '''
        pygame.draw.rect(screen, biscut_color, biscut0)
        pygame.draw.rect(screen, biscut_color, biscut1)
        pygame.draw.rect(screen, biscut_color, biscut2)
        pygame.draw.rect(screen, biscut_color, biscut3)
        pygame.draw.rect(screen, biscut_color, biscut4)
        '''
    else:
        screen.blit(intro_text, (200, 200))

    if handle_stop:
        screen.blit(score_text, (300, 400))
        pygame.display.update()
        time.sleep(3)
        Running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
    pygame.display.update()

    #------------------------------------
    #Frame rate and tick count updates
    #------------------------------------

    if game_mode == "pt" and update_frame_rate:
        frame_rate += score/10
    elif game_mode == "grad" and frame_rate >= 20:
        frame_rate += score/100
    update_frame_rate = True

    if tick_count % tick_count_step_by == 0:
        if boxy_direction == 0:
            boxy.x += -50
        if boxy_direction == 1:
            boxy.x += 50
        if boxy_direction == 2:
            boxy.y += -50
        if boxy_direction == 3:
            boxy.y += 50

    tick_count += 1
    clock.tick(frame_rate)
pygame.quit()


#