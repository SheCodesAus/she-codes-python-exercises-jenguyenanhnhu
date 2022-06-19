# Part A
list = []
list2 = []
number = input("Enter a number: ")
while number != '':
    list.append(number)
    number = input("Enter a number: ")
else:
    for numbers in list:
        concatenate = ''.join(list)
    print(concatenate)
for i in range(0, len(list)):
    list[i] = int(list[i])
print(sum(list))
print(list)


# Part B
import re

string = input("Enter your phrase: ")
string_without_vowels = re.sub("[aeiouAEIOU]", '',string)
print(string_without_vowels)


# Part C
winning_number = 2345

guess = input("Guess the number:")
while guess != winning_number:
    for i in range(len(guess)):
        if i == winning_number[i]:
            print([i])
        else: 
            print('X')
    guess = input("Guess the number: ")
print(f"You got it! {guess} is correct.")