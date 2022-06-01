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
    colour_counts += 1


    read_data = csv_file.read()
    for data in colours:
        list += 1
        word_count = read_data.count(data)
        print(f"{data}: {word_count}")
# colours = [
#     "orange",
#     "purple",
#     "blue",
#     "yellow",
#     "green",
#     "green",
#     "purple",
#     "purple",
#     "green",
#     "blue",
#     "green",
#     "orange",
#     "purple",
#     "blue",
#     "green",
#     "orange",
#     "orange",
#     "red",
#     "yellow",
#     "yellow"
# ]
