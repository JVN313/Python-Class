#Working with Lists, Functions, and Classes
#List Functions .append, .extend, .insert(1,2), .remove, .clear, .pop, .count, .sort, .copy
import random
import requests
randomLists = [
    [1, 2, 3],
    ["tough", "Hard", "strong "]
]
games = ["Arcadia", "Sonic", "Dragon's Dogma"]

# Tax Calculator
def tax_cal(amount):
    tax = 0.06
    total = amount + amount*tax
    total = round(total,2)
    return total    

# Decade Calculator
def decade_cal():
        user_age = input("How old are you?: ")
        remainder = int(float(user_age) % 10)
        decade_age = int(int(user_age) / 10)
        print("You are " + user_age + " years old!")
        print("Thats " + str(decade_age) + " decades and " + str(remainder) + " years old")

# Retrieves Letters In Words
def letter_getter(word):
    i = 0
    for letter in word:
        print(letter)
        i+=1
    print("There are " +str(i)+ " letters in the word " + word.upper() + ". The first letter is " + word[0].upper())

# Tells If You Have Enough Bricks For A Fictional House
def brick_layer():
    num_bricks = int(input("How many bricks do you want to build your house: "))
    if num_bricks >= 5:
        print("Thats enough for the four walls and roof")
    else:
        print("That's not enough for, four walls and a roof")

# Takes an image url and downloads the image and saves the file as image.jpg
def image_getter(url):
     r = requests.get(url)
     image_open= open("image.jpg", "wb")
     image_write = image_open.write(r.content)



class game:
    def __init__(self, name, type, rating):
        self.name = name
        self.type = type
        self.rating = rating

class player:
    def __init__(self, name, age, console):
        self.name = name
        self.age = age
        self.console = console
