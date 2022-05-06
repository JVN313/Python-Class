
#New Guessing Game

comp_num = random.randint(0,10)
attemps = 1

# Main Game Loop
def Game_Loop():
    global attemps, player_guess
    while attemps < 3 and player_guess != comp_num:
        if player_guess != comp_num:
            attemps+=1
            print("Sorry, wrong number try again?\n")
            player_guess = int(input("Guess A number from 0-10\n"))

    if attemps >= 3:
        print("Sorry you lost")
    
    if player_guess == comp_num:
        print("You Win")

    Replay()

# Replay Function
def Replay():
    global attemps, player_guess, comp_num
    replay_answer = input("Would You like to play again?: ").upper()
    if replay_answer == "Y":
        attemps = 1
        comp_num = random.randint(0,10)
        player_guess = int(input("Guess A number from 0-10\n"))
        Game_Loop()
    else:
        print("Thanks For Playing")
        quit()

print("I'm thinking of a number can you guess what it is? I'll give you 3 tries to figure it out.")
player_guess = int(input("Guess A number from 0-10\n"))

Game_Loop()
