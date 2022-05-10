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
colours = ['Red', 'Green', 'Blue', 'Yellow']
colour = 0
with open("csv_files/colours_20.csv") as csv_file:
    reader = csv.reader (csv_file)


#Exercise 5
with open("csv_files/galaxies.csv") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
