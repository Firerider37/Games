'''
Name:
    Max Epstein
Title:
    Leaglly Not Pong
Use:
    Player 1 controls the paddle on the left (W & S)
    Player 2 controlls the paddle on the right (Up and Down)
Bugs:
    Time stepping for sppeding up
Changes:
    None
'''

import pygame
import random
import time

pygame.init()                                                                                                                                                                                                                                                                                                                                                                                                       #Max Epstein's code

#-------------------------------
#Screen definition and setup
#-------------------------------

screen_width = 1400
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")


#-----------------------
#Players/ball definition
#-----------------------
ball = pygame.Rect((700, 400), (25, 25))
P1 = pygame.Rect((50, 400), (30, 150))
P2 = pygame.Rect((1350, 400), (30, 150))
p1pts = 0
p2pts = 0



#-----------------------
#Game variables
#-----------------------
starting = True
ball_x_momentum = 0
ball_y_momentum = 0
tick_count = 0
tick_count_step_by = 5
frame_rate = 240
clock = pygame.time.Clock()



#---------------
#Running Loop - allows the game to run until the user quits or loses
#---------------
Running = True
while Running:
    key = pygame.key.get_pressed()

    #---------------------------------------------
    # KEYBOARD INPUTS
    #---------------------------------------------

    if key[pygame.K_w]:
        P1.y -= 1
    if key[pygame.K_s]:
        P1.y += 1


    if key[pygame.K_UP]:
        P2.y -= 1
    if key[pygame.K_DOWN]:
        P2.y -= -1

    if P1.top < 0:
        P1.top = 0
    if P1.bottom > screen_height:
        P1.bottom = screen_height

    if P2.top < 0:
        P2.top = 0
    if P2.bottom > screen_height:
        P2.bottom = screen_height

    if key[pygame.K_SPACE] and starting:
        starting = False
        ball_x_momentum = random.choice([-1, 1])
        ball_y_momentum = random.choice([-1, 1])
    if ball.left == P1.right and ball.y > P1.top and ball.y < P1.bottom:
        ball_x_momentum *= -1
    elif ball.left < P1.right:
        p2pts += 1
        starting = True
        ball.x = 700
        ball.y = 400
        ball_x_momentum = 0
        ball_y_momentum = 0
        if key[pygame.K_SPACE]:
            ball_x_momentum = random.uniform(-1, 1)
            ball_y_momentum = random.uniform(-1, 1)

    if ball.right == P2.left and ball.y > P2.top and ball.y < P2.bottom:
        ball_x_momentum *= -1
    elif ball.right > P2.left:
        p1pts += 1
        starting = True
        ball.x = 700
        ball.y = 400
        ball_x_momentum = 0
        ball_y_momentum = 0
        if key[pygame.K_SPACE]:
            ball_x_momentum = random.uniform(-1, 1)
            ball_y_momentum = random.uniform(-1, 1)

    if ball.top == 0 or ball.bottom == screen_height:
        ball_y_momentum *= -1


    ball.y += ball_y_momentum
    ball.x += ball_x_momentum

    score_text = pygame.font.SysFont(None, 36).render(f"Player 1: {p1pts}  Player 2: {p2pts}", True, "white")

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), ball)
    pygame.draw.rect(screen, (0, 0, 255), P1)
    pygame.draw.rect(screen, (255, 0, 0), P2)

    screen.blit(score_text, (screen_width // 2 - score_text.get_width() // 2, 10))
    pygame.display.update()

    #if tick_count % tick_count_step_by == 0:
    #    frame_rate += 1
    #tick_count += 1
    frame_rate += 0.1
    clock.tick(frame_rate)

    if key[pygame.K_ESCAPE]:
        time.sleep(3)
        Running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False

pygame.quit()


#