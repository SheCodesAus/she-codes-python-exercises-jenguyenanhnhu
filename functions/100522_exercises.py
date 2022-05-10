
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
def list(a, n):
    list = a/n
    a = 4, 3, 2, 6
    n = len(a)
    return list


# Exercise 4