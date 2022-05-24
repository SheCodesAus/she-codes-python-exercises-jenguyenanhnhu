# Exercise 1
number = int(input("Enter a number: "))
all = []
while number != "":
    all.append(int(number))
    number = input("Enter a number: ")
print(sum(all))

# Exercise 2
number2 = int(input("Enter a number: "))
number3 = 1
while number3 <= number2:
    if number3 % 2 != 0:
        print(number3)
        number3 += 2


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