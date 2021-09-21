print("WELCOME TO THE KARDASHIANS QUIZ")

player = input("Enter Your Name: ")
playing = input("Would You Like To Play The Game " + player+"? ")
score = 0

if playing.upper() == "YES":
    print("Great Let's Play")
elif playing.upper() == "No":
    print("Okay Thanks For Stopping By!")
    quit()
else:
    print("Invalid Input")
    playing = input("Would You Like To Play The Game " + player+"? ")

answer1 = input("What Year Did Keeping Up With The Kardashians Start? \n a) 2003 \n b) 2005 \n c) 2007 \n ")

if answer1.upper() == "C" or answer1 == "2007":
    print("Correct!")
    score+=1
else:
    print("Incorrect! The Answer Is c) 2007")

answer2 = input("Who Is The Youngest Kardashian? \n a) Kim \n b) Khole \n c) Kylie \n ")

if answer2.upper() == "B" or answer2.upper() == "KHOLE":
    print("Correct!")
    score+=1
else:
    print("Incorrect! The Answer Is b) Khole")

answer3 = input("Who Was The Original Producer Of KUWTK? \n a) Robert Kardashian \n b) Kris Jenner \n c) Ryan Seacrest \n")

if answer3.upper() == "C" or answer3.upper() == "RYAN SEACREST":
    print("Correct!")
    score+=1
else:
    print("Incorrect! The Answer Is c) Ryan Seacrest")

answer4 = input("Which Kardashian Competed On Dancing With The Stars? \n a) Rob \n b) Khole \n c) Kourtney \n ")

if answer4.upper() == "A" or answer4.upper() == "ROB":
    print("Correct!")
    score+=1
else:
    print("Incorrect! The Answer Is a) Rob")

answer5 = input("Where did Kim and Kanye baptize their first daughter North? \n a) Paris \n b) Armenia \n c) Jerusalem \n ")

if answer5.upper() == "C" or answer5.upper() == "JERUSALEM":
    print("Correct!")
    score+=1
else:
    print("Incorrect! The Answer Is c) Jerusalem")

print("You Got " + str(score) + " Out Of 5 Right")
if score == 5:
    print("Perfect Score You're A Honorary Dash Baby " + player + "!")
else:
    print("Thanks For Playing " + player + "!")