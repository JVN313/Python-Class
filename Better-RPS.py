import random

# Game Variables
playing = True
player_wins = 0
computer_wins = 0
games_played = 0
options = ["ROCK","PAPER","SCISSORS"]
short_options = ["R","P","S"]
answer = options[random.randrange(0,3)]
user_input = input("Type Rock, Paper, Scissors, or Q to quit the game: ").upper()

# Game Functions
def player_win():
    global player_wins
    player_wins+=1
    print("You Won!")

def replay():
    global answer,user_input
    answer = options[random.randrange(0,3)]
    user_input = input("To play again type Rock, Paper, Scissors, or Q to quit the game: ").upper()

def score_board():
    score_board_add = open("RPSscoreboard.txt","a")
    score_entry = input("ENTER YOUR NAME TO BE PLACED ON THE LEADERBOARDS: ").upper()
    score_board_add.write("\n"+score_entry+" "+str(player_wins)+"/"+str(games_played))
    score_board_show = open("RPSscoreboard.txt","r")
    print(score_board_show.read())
    score_board_show.close()
    score_board_add.close()

# Game Loop
while playing:
    if user_input == "Q" or user_input =="QUIT":
        playing = False
    elif user_input == "PAPER" or user_input == short_options[1] and answer == options[0]:
        games_played+=1
        player_win()
        replay()
    elif user_input == "ROCK" or user_input == short_options[0] and answer == options[2]:
        games_played+=1
        player_win()
        replay()
    elif user_input == "SCISSORS" or user_input == short_options[2] and answer == options[1]:
        games_played+=1
        player_win()
        replay()
    elif user_input not in options and user_input not in short_options:
        print("Invalid Input")
        replay()
    else:
        games_played+=1
        computer_wins+=1
        print("Sorry You Lost :( ")
        replay()
    
print("You Won "+str(player_wins)+" Time(s). And Lost "+str(computer_wins)+" Time(s)")
score_board()
print("Thanks For Playing!")