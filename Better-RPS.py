import random

playing = True
player_wins = 0
computer_wins = 0
options = ["ROCK","PAPER","SCISSORS"]
answer = options[random.randrange(0,3)]
user_input = input("Type Rock, Paper, Scissors, or Q to quit the game: ").upper()

while playing:
    if user_input == "Q" or user_input =="QUIT":
        playing = False
    elif user_input == "PAPER" and answer == options[0]:
        player_wins+=1
        print("You Won!")
        answer = options[random.randrange(0,3)]
        user_input = input("To play again type Rock, Paper, Scissors, or Q to quit the game: ").upper()
    elif user_input == "ROCK" and answer == options[2]:
        player_wins+=1
        print("You Won!")
        answer = options[random.randrange(0,3)]
        user_input = input("To play again type Rock, Paper, Scissors, or Q to quit the game: ").upper()
    elif user_input == "SCISSORS" and answer == options[1]:
        player_wins+=1
        print("You Won!")
        answer = options[random.randrange(0,3)]
        user_input = input("To play again type Rock, Paper, Scissors, or Q to quit the game: ").upper()
    elif user_input not in options:
        print("Invalid Input")
        answer = options[random.randrange(0,3)]
        user_input = input("To play again type Rock, Paper, Scissors, or Q to quit the game: ").upper()
    else:
        computer_wins+=1
        print("Sorry You Lost :( ")
        answer = options[random.randrange(0,3)]
        user_input = input("To play again type Rock, Paper, Scissors, or Q to quit the game: ").upper()
    
print("You Won "+str(player_wins)+" Time(s). And Lost "+str(computer_wins)+" Time(s)")
print("Thanks For Playing!")