import csv
import os

# Exercise 1
with open("csv_files/colours_20_simple.csv") as csv_file:
    reader = csv.reader (csv_file)
    for line in reader:
        print(line)

# Exercise 2 & 3
with open("csv_files/colours_20_simple.csv") as csv_file:
    reader = csv.reader (csv_file)
    for line in reader:
        print(f"{line[2]}, Hex: {line[1]}, RGB {line[0]}")

#Exercise 4
colours = ['red', 'green', 'blue', 'yellow']
list = 0

with open("csv_files/colours_20.csv") as csv_file:
    read_data = csv_file.read()
    for data in colours:
        list += 1
        word_count = read_data.count(data)
        print(f"{data}: {word_count}")


with open("csv_files/colours_213.csv") as csv_file:
    read_data = csv_file.read()
    for data in colours:
        list += 1
        word_count = read_data.count(data)
        print(f"{data}: {word_count}")

#Exercise 5
with open("csv_files/galaxies.csv") as csv_file:
    reader = csv.reader (csv_file)
    read_data = csv_file.read()
    for line in reader:
        max_velocity = max(line[1])
        min_velocity = min(line[1])
        print(f"{max_velocity}")