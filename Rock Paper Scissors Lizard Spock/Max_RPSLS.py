'''
Coder:
    Max Epstein
Title:
    RPSLS
Date:
    11/23/2026
Description:
    Rock Paper Scissors Lizzard Spock - but it works in the same way that using a terminal does
Bugs:
    None
'''
#imports questionary, random, and LMstudio
import questionary #type: ignore
from questionary import Choice, Style #type: ignore
import random
import lmstudio as lms #type: ignore

#List of options for the game
options = ['Rock', 'Paper', 'Scissors', 'Lizzard', 'Spock']

#Local AI model for the game
model = lms.llm("qwen2.5-coder-7b-instruct")

#Style for the selector
style = Style([
    ("pointer", "fg:#5c8dff bold"),
    ("highlighted", "fg:#5c8dff bold"),
])

#Game varibles
game_count = 0
pts = 0
Running = True
ppr = []

#defines robot choice for first round
bot = random.choice(options)


while Running:
    #Clears screan
    print("\033[H\033[J", end="") 
    #Print top opening
    print("Welcome to Rock, Paper, Siccors, Lizzard, Spock")

    #selector panel
    selected = questionary.select(
        "What would you like to play:",
        choices=options,
        pointer=">",
        qmark="",
        style=style,
    ).ask()

    #adds prevous choice to a list
    ppr.append (selected)

    #if there has been more than one game, then the bot will be based on an ai model that has acess to prevous responces
    if game_count >= 1:
        bot = model.respond(
            f'''Here are all the prevous responces in a game of Rock Paper Siccors Lizard Spock. {ppr}
            Choose an option from the list: {options}
            Make sure to only choose options from that list.
            Your goal is to win and outsmart the other person.
            Respond with nothing but your choice.
            A sample responce would be: "Rock" ''',
        ).parsed

    #displays what you and the bot choose
    print(f"You chose {selected} and the bot chose {bot}")
    if selected == bot:                               #If the player and the bot got the same thing, display "Draw"
        print("Draw")  
    elif selected == "Rock":                          #If the player plays rock
        if bot == "Paper":                              #and the bot plays paper, print "Player covers rock"
            print("Paper covers rock")
            pts += 0
        elif bot == "Scissors":                         #and the bot plays scissors, print "Rock crusshes scissors", and increase your score by one
            print("Rock crushes scissors")
            pts += 1
        elif bot == "Lizzard":                          #and the bot plays Lizzard, print "Rock crushes lizzard" and increaces you score by one
            print("Rock crushes lizzard")
            pts += 1
        elif bot == "Spock":                            #and the bot plays spock, print "Spock vaporizes rock"
            print("Spock vaportizes rock")
            pts += 0
    elif selected == "Paper":                        #Follows same outline as prevous block
        if bot == "Rock":
            print ("Paper covers rock")
            pts += 0
        elif bot == "Scissors":
            print("Scissors cuts paper")
            pts += 1
        elif bot == "Lizzard":
            print("Lizzard eats paper")
            pts += 0
        elif bot == "Spock":
            print("Paper disproves spock")
            pts += 1
    elif selected == "Scissors":                     #Follows same outline as prevous block
        if bot == "Paper":
            print("Siccors cuts paper")
            pts += 1
        elif bot == "Rock":
            print("Rock cuts scissors")
            pts += 0
        elif bot == "Lizzard":
            print("Scissors decapitates Lizzard")
            pts += 1
        elif bot == "Spock":
            print("Spock smashes scissors")
            pts += 0
    elif selected == "Lizzard":                     #Follows same outline as prevous block
        if bot == "Paper":
            print("Lizzard eats paper")
            pts += 1
        elif bot == "Scissors":
            print("Scissors decapitates Lizzard")
            pts += 0
        elif bot == "Rock":
            print("Rock crushes Lizzard")
            pts += 0
        elif bot == "Spock":
            print("Lizzard poisons Spock")
            pts += 1
    elif selected == "Spock":                      #Follows same outline as prevous block
        if bot == "Paper":
            print("Paper disproves Spock")
            pts += 0
        elif bot == "Scissors":
            print("Spock smashes scissors")
            pts += 1
        elif bot == "Lizzard":
            print("Lizzard poisons Spock")
            pts += 0
        elif bot == "Rock":
            print("Spock vaporizes Rock")
            pts += 1

    #increases games played by one
    game_count += 1

    #prints how many games you have won and total games
    print(f"You have won {pts} points out of {game_count} games.")

    #asks if you want to play again, and if it isn't yes, stop the running loop
    if not questionary.confirm("Play again?").ask():
        Running = False

#Clears screan
print("\033[H\033[J", end="") 
print("Thanks for playing!")
questionary.press_any_key_to_continue().ask()
