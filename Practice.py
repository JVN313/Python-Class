# File for working with Pluralsight videos
test = True
while test:
    def decade_cal():
        user_age = input("How old are you?: ")
        remainder = int(float(user_age) % 10)
        decade_age = int(int(user_age) / 10)
        print("You are " + user_age + " years old!")
        print("Thats " + str(decade_age) + " decades and " + str(remainder) + " years old")

    decade_cal()

    testing = input("continue?: ")
    if not test == "yes":
        test = False
    elif testing == "no":
        test = False


