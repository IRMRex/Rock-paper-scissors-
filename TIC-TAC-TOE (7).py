from colorama import Fore
import time
import random
def SET():
    print("1) About, 2) Text Color, 3) Back")
    SETDO = input("What would you like to do? ")
    if SETDO == "1":
        print("Version 2.0 beta 1 2I1-008")
        SET()
    elif SETDO == "2":
        print('What color: 1) Default, 2) Blue, 3) Green')
        COLO = input("What color? ")
        if COLO == "1":
            print(Fore.WHITE+"White")
            SET()
        elif COLO == "2":
            print(Fore.BLUE+"Blue")
            SET()
        elif COLO == "3":
            print(Fore.GREEN+"Green")
            SET()
        elif COLO == "4":
            print(Fore.YELLOW+"Yellow")
            SET()
    elif SETDO == "3":
        MAINMENU()
    else:
        print("Not an option!")
        SET()
def NUMG():
    print("Not here yet")
    MAINMENU()
def RPS():
    AIchose = random.randint(1,3)
    MODE = input("What mode would you like, 1) Easy, 2) Hard, 3) Home ")
    if MODE == "2":
        TTTDO = input("Rock, paper, or scissors? ")
        ws = 0
        while ws < 4:
            if ws == 1:
                print("Rock")
            elif ws == 2:
                print("Paper")
            elif ws == 3:
                print("Scissors")
            time.sleep(1)
            ws += 1
        print("SHOOT!")
        if TTTDO == "Rock" or TTTDO == "rock":
            print("The AI chose Paper")
            RPS()
        elif TTTDO == "paper" or TTTDO == "Paper":
            print("The AI chose Scissors")
            RPS()
        elif TTTDO == "Scissors" or TTTDO == "scissors":
            print("The AI chose Rock")
            RPS()
    if MODE == "1":
        TTTDO = input("1) Rock, 2) paper, or 3) scissors? ")
        ws = 0
        while ws < 4:
            if ws == 1:
                print("Rock")
            elif ws == 2:
                print("Paper")
            elif ws == 3:
                print("Scissors")
            time.sleep(1)
            ws += 1
        if AIchose == 1:
            if TTTDO == "Rock" or TTTDO == "rock" or TTTDO == "1":
                print("DRAW")
                RPS()
            elif TTTDO == "paper" or TTTDO == "Paper" or TTTDO == "2":
                print("YOU WON")
                RPS()
            elif TTTDO == "Scissors" or TTTDO == "scissors" or TTTDO == "3":
                print("YOU LOST")
                RPS()
        elif AIchose == 2:
            if TTTDO == "Rock" or TTTDO == "rock" or TTTDO == "1":
                print("YOU LOST")
                RPS()
            elif TTTDO == "paper" or TTTDO == "Paper" or TTTDO == "2":
                print("DRAW")
                RPS()
            elif TTTDO == "Scissors" or TTTDO == "scissors" or TTTDO == "3":
                print("YOU WON")
                RPS()
        elif AIchose == 3:
            if TTTDO == "Rock" or TTTDO == "rock" or TTTDO == "1":
                print("YOU WON")
                RPS()
            elif TTTDO == "paper" or TTTDO == "Paper" or TTTDO == "2":
                print("YOU LOST")
                RPS()
            elif TTTDO == "Scissors" or TTTDO == "scissors" or TTTDO == "3":
                print("DRAW")
                RPS() 
    elif MODE == "3":
        MAINMENU()
def MAINMENU():
    print("1) Rock, Paper, Scisors, 2) Random number game, 3) Settings")
    Game = input("Which game? ")
    if Game == "1":
        RPS()
    elif Game == "2":
        NUMG()
    elif Game == "3":
        SET()
    else:
        MAINMENU()
MAINMENU()