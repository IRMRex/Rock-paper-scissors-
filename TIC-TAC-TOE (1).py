
import time
import random
AIchose = random.randint(1,3)
MODE = input("What mode would you like, 1) Easy, 2)Hard")
if MODE == "2":
    TTTDO = input("Rock, paper, or scissors?")
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
    elif TTTDO == "paper" or TTTDO == "Paper":
        print("The AI chose Scissors")
    elif TTTDO == "Scissors" or TTTDO == "scissors":
        print("The AI chose Rock")
if MODE == "1":
    TTTDO = input("Rock, paper, or scissors?")
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
        if TTTDO == "Rock" or TTTDO == "rock":
            print("DRAW")
        elif TTTDO == "paper" or TTTDO == "Paper":
            print("YOU WON")
        elif TTTDO == "Scissors" or TTTDO == "scissors":
            print("YOU LOST")
    elif AIchose == 2:
        if TTTDO == "Rock" or TTTDO == "rock":
            print("YOU LOST")
        elif TTTDO == "paper" or TTTDO == "Paper":
            print("DRAW")
        elif TTTDO == "Scissors" or TTTDO == "scissors":
            print("YOU WON")
    elif AIchose == 3:
        if TTTDO == "Rock" or TTTDO == "rock":
            print("YOU WON")
        elif TTTDO == "paper" or TTTDO == "Paper":
            print("YOU LOST")
        elif TTTDO == "Scissors" or TTTDO == "scissors":
            print("DRAW")