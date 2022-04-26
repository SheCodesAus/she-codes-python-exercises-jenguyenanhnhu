# Data Types
# String - text, put quotes around it
day = "Saturday"
print(type(day))
message = f"Today is {day}!"
print(message)

# Integer - numerical data (whole numbers)
run1_dist = 1400
run2_dist = 536
total_dist = run1_dist + run2_dist
print(total_dist)

run3_dist = 3.4
run4_dist = 6
total_dist = run3_dist + run4_dist
print(total_dist)

print(run1_dist / 1000)
print(run3_dist * 1000)
# Division always produces floats.
# Other calculations depends on data type.
# As long as there is one float, sum will be a float.

# Float - numerical data (decimals) 

weather = "rainy"
name = "Jen"

# Type cast to change the data type
print(name + str(run4_dist))
print(name * int(run4_dist))





