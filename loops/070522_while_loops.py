# Exercise 1



# Exercise 2




# Exercise 3
i=25
guess=int(input("Guess a number:"))

while guess != i:
    if guess < i:
        print("Too low!")
    elif guess > i:
        print("Too high!")
    guess=int(input("Try again: "))  
print("Correct!")