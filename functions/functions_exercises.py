
# Exercise 1
def temp_in_f(f):
    temp_in_f = (f - 32)/1.8
    return temp_in_f

print(temp_in_f(32))
print(temp_in_f(0))
print(temp_in_f(350))

# Exercise 2
def number(x):
    if x % 2 == 0:
        return("True")
    else:
        return("False")

print(number(-96))

# Exercise 3
def mean(list):
    mean = sum(list)/len(list)
    return mean
print(mean([4, 3, 2, 6]))
print(mean([10, 5, 6]))

# Exercise 4
def total(price_per_unit, num_units):
    total = price_per_unit*num_units
    return total
print(total(4.25, 3))
print(total(3.79, 1))
print(total(1.49, 7))