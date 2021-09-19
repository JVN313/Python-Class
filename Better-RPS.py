import random

playing = True
player_wins = 0
computer_wins = 0
options = ["ROCK","PAPER","SCISSORS"]
answer = options[random.randrange(0,3)]
user_input = input("Type Rock, Paper, Scissors, or Q to quit the game: ").upper()

while playing:
    if user_input == "Q":
        playing = False
    elif user_input == "PAPER" and answer == "ROCK":
        player_wins+=1
        print("You Won!")
        answer = options[random.randrange(0,3)]
        user_input = input("To play again type Rock, Paper, Scissors, or Q to quit the game: ").upper()
    elif user_input == "ROCK" and answer == "SCISSORS":
        player_wins+=1
        print("You Won!")
        answer = options[random.randrange(0,3)]
        user_input = input("To play again type Rock, Paper, Scissors, or Q to quit the game: ").upper()
    elif user_input == "SCISSORS" and answer == "PAPER":
        player_wins+=1
        print("You Won!")
        answer = options[random.randrange(0,3)]
        user_input = input("To play again type Rock, Paper, Scissors, or Q to quit the game: ").upper()
    else:
        computer_wins+=1
        print("Sorry You Lost :( ")
        answer = options[random.randrange(0,3)]
        user_input = input("To play again type Rock, Paper, Scissors, or Q to quit the game: ").upper()
    
print("You Won This "+str(player_wins)+" Many Times. And Lost This "+str(computer_wins)+" Many Times")
print("Thanks For Playing!")