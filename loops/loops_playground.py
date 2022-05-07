from nis import cat

#For Loops 
name = "Jenny"
for character in name: #assigns character variable to each letter
    print(name)

for num in range(10):
    print(num)

for num in range(1, 11):
    print(num)

for num in range(0, 11, 2):
    print(num)

for num in range(0,101):
    print(num)

for num in range(0, 101, 5):
    print(num)

chilli_wishlist = ['igloo', 'chicken', 'donut toy', 'cardboard box']
for item in range(len(chilli_wishlist)):
    print(chilli_wishlist[item])
for item in chilli_wishlist:
    print(f"Chilli wants: {item}.")

chilli_wishlist = [
    ['igloo'],
    ['donut toy', 'tennis ball', 'crocodile toy'],
    ['chicken', 'peanut butter'],
    ['cardboard box', 'kong', 'dig mat']
]

for category in chilli_wishlist:
    for item in category:
        print(item)


#While Loops
counter = 0

while counter < 5:
    print("Hello")
    print("counter1: ", counter)
    counter += 1
    print("counter2: ", counter)

guess = ""
while guess != "a":
    guess = input("Guess a letter: ")

counter = 10
while counter <= 10:
    print(counter)
    counter = counter + 1
