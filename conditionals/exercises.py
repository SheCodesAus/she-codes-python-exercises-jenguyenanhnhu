from operator import contains


moths_in_house = False
mitch_is_home = False
if moths_in_house and mitch_is_home:
    print("Hooman! Help me get the moths!")
elif moths_in_house and not mitch_is_home:
    print("Meooooooooooooow! Hissssss!")
elif not moths_in_house and mitch_is_home:
    print("Climb on Mitch")
else:
    print("No threats are detected.")

light_colour = "Amber"
car_detected = True
if light_colour == "Red" and car_detected:
    print("Flash!")
else:
    print("Do nothing.")

height = 191
if height >= 120:
    print("Hop on!")
else:
    print("Sorry, not today :(")

username = "fleur"
password = "password123"
if username == "fleur" and password == "password123":
    print("Correct!")
else:
    print("Incorrect!")

email = "@.hayleytest.com"
if (email. __contains__("@") and email. __contains__(".")):
    print("Valid email address.")
else:
    print("Invalid email address.")

