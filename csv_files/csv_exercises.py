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
    next(csv_file)
    galaxy_list = []
    velocity_list = []
    for line in reader:
        print(line)
        galaxy_list.append(int(line[0]))
        velocity_list.append(int(line[1]))
    min_velocity = min(velocity_list)
    for a in range(len(velocity_list)):
        if velocity_list[a]==min_velocity:
            min_galaxy = galaxy_list[a]
    max_velocity = max(velocity_list)
    for b in range(len(velocity_list)):
        if velocity_list[b]==max_velocity:
            max_galaxy = galaxy_list[b]
    print(f"Galaxy {min_galaxy} has the min velocity of {min_velocity}km/sec.\nGalaxy {max_galaxy} has the max velocity of {max_velocity}km/sec.")