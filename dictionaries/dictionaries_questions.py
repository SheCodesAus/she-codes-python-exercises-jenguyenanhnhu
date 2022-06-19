# Question 1
prices = {
    "Baby Spinach": 2.78,
    "Hot Chocolate": 3.70,
    "Crackers": 2.10,
    "Bacon": 9.00,
    "Carrots": 0.56,
    "Oranges": 3.08
}

quantity = {
    "Baby Spinach": 1,
    "Hot Chocolate": 3,
    "Crackers": 2,
    "Bacon": 1,
    "Carrots": 4,
    "Oranges": 2
}

for a in quantity:
    total = quantity[a]*prices[a]
for b in quantity:
    print(f"{quantity[b]} {b} @ ${prices[b]} = ${round(total, 2)}")


quantity2 = {
    "Baby Spinach": 2,
    "Hot Chocolate": 1,
    "Crackers": 4,
    "Bacon": 0,
    "Carrots": 8,
    "Oranges": 5
}

for c in quantity2:
    total = quantity2[a]*prices[a]
for d in quantity2:
    print(f"{quantity2[b]} {b} @ ${prices[b]} = ${round(total, 2)}")



# Question 2
colour_counts = {
    "blue": 0,
    "green": 0,
    "yellow": 0,
    "red": 0,
    "purple": 0,
    "orange": 0,
}

colours = [
    "purple",
    "red",
    "yellow",
    "blue",
    "purple",
    "orange",
    "blue",
    "purple",
    "orange",
    "green"
]

for colour in colour_counts:
    word_count = colours.count(colour)
    print(f"{colour}: {word_count}")


colours2 = [
    "orange",
    "purple",
    "blue",
    "yellow",
    "green",
    "green",
    "purple",
    "purple",
    "green",
    "blue",
    "green",
    "orange",
    "purple",
    "blue",
    "green",
    "orange",
    "orange",
    "red",
    "yellow",
    "yellow"
]

for data in colour_counts:
    word_count2 = colours2.count(data)
    print(f"{data}: {word_count2}")



# Question 3
names = [
    "Maddy", "Bel", "Elnaz", "Gia", "Izzy",
    "Joy", "Katie", "Maddie", "Tash", "Nic",
    "Rachael", "Bec", "Bec", "Tabitha", "Teagen",
    "Viv", "Anna", "Catherine", "Catherine", "Debby",
    "Gab", "Megan", "Michelle", "Nic", "Roxy",
    "Samara", "Sasha", "Sophie", "Teagen", "Viv"
]

for name in names:
    number = names.count(name)
    print(f"{name} {number}")

names2 = [
    "Miranda", "Sophie", "Emily", "Taylor", "Anne",
    "Djuarli", "Anika", "Rosie", "Miranda", "Taylor",
    "Abby", "Sarah", "Teagen", "Abby", "Abby",
    "Maddie", "Miranda", "Rosie"
]

for data in names2:
    number2 = names2.count(data)
    print(f"{data}: {number2}")



# Question 4
import csv

with open("dictionaries/colours_20_simple.csv") as csv_file:
    read_data = csv.reader(csv_file)
    for line in read_data:
        print(f"{line[1]}: ['{line[0]}', '{line[2]}']")