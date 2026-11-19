'''
Title:
    Magic 8 Ball
Author:
    Max Epstein
Date:
    11/19/2026
Description:
    Uses random list arguments and pygame to create a magic 8 ball game. Pygame provides a graphical interface that is useable for shaking.
Challangesr:
    Pygame for Graphical interface
Bugs:
    None
'''



#imports random module and pygame module & intitlizes pygame module
import random
import pygame

pygame.init()

#sets the dimentions for the screen
screen_width = 600
screen_height = 600

#Inital bool value for displaying certin texts
display_text = False

#inital message on window
start_text = pygame.font.SysFont(None, 36).render("Press space to shake", True, "black")

# Sets the screen
screen = pygame.display.set_mode((screen_width, screen_height))

#List of magic 8 ball answears
answear_list = ["It is certin", "It is decidedly so", "Without a doubt", "Yes, definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy, try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]


#running loop for program
Running = True

while Running:
    key = pygame.key.get_pressed()                                                      #Gets information about a key that is pressed
    if key[pygame.K_ESCAPE]:                                                            #Escape key or quiting out of the app closes the window and stops the program
        Running = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
    if key[pygame.K_SPACE]:                                                             #sets an answer for the pourpose of displaying it
        answear = random.choice(answear_list)                                           #Allows to display text
        display_text = True
        responce_text = pygame.font.SysFont(None, 36).render(answear, True, "black")    #Sets what the text should be


    screen.fill("white")                                                                #Setts a white backround
    if display_text:                                                                    #Shows either an inital messsage or the 8 ball responce
        screen.blit(responce_text, (200,250))
    else:
        screen.blit(start_text, (200,250))
    pygame.display.update()                                                             #Updates the display

pygame.quit()                                                                           #When the game is over quits the program