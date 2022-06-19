# Exercise 1
from random import random


number = int(input("Enter a number: "))

for i in range(1, number+1):
    print(f"{number} * {i} = {number * i}")

#Exercise 2
number = int(input("Enter a number"))
total = 0
for i in range(number+1):
    total += i
print(total)

#Exercise 3 
random_numbers = [3, 5, 9, 1]
total = 0
for i in random_numbers:
    total += i
print(total)

#Exercise 4 
mailing_list = [
    ["Chilli", "chilli@thechihuahua.com"],
    ["Roary", "roary@moth.catchers"],
    ["Remus", "remus@kapers.dog"],
    ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
    ["Ivy", "noreply@goldendreamers.xyz"],
]
for info in mailing_list:
    print(f"{info[0]}: {info[1]}")
