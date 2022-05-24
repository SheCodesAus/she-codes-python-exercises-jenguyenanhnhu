# Exercise 1
groceries = [
["Baby Spinach", 2.78],
["Hot Chocolate", 3.70],
["Crackers", 2.10],
["Bacon", 9.00],
["Carrots", 0.56],
["Oranges", 3.08]
]

items = []
price = []
grand_total = []

for item in groceries:
    # items.append(groceries[0])
    # price.append(groceries[1])
    quantity = int(input("How many/much?"))
    total = round(quantity*item[1], 2)
    grand_total.append(total)
print(f"====Izzy's Food Emporium====")
for item in groceries:
    print(f"{item[0]}: {grand_total}")
print(f"${sum(grand_total)}")


# Exercise 2
word = input("Please enter a string: ")
index = -1
for letter in word:
    index += 1
    print(index, letter)


# Exercise 3
pyramid = int(input("Pyramid size: "))
row = 0

while row <= pyramid:
    print(row*'*')
    row += 1
