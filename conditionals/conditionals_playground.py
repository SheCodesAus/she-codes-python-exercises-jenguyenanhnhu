# Data Types - Strings, Integer, Floats, Boolean
b1 = True
b2 = False
print(type(b1))

knows_password = True
knows_username = True
login = knows_username and knows_username
recover = knows_password or knows_username
print(login)
print(recover)

#Boolean Operators - NOT (reverse output), AND (both outputs must be TRUE = TRUE), OR (both outputs must be FAlSE = FALSE)
# Refer to Asli's truth tables.

is_raining = False
is_cold = True
print(not is_raining)
print(is_raining and is_cold)
print(is_raining and not is_cold) 

is_raining = True
is_cold = True
print(is_raining) #True
print(not is_raining) #False
print(is_raining or is_cold) #True
print(is_raining and not is_cold) #False
print(is_raining or not is_cold) #True
print(not is_raining and not is_cold) #False
print(not(is_raining and is_cold)) #False

#Comparison Operators
# == Equal
# != Not Equal
# > Greater than
# < Less than
# >= Greater than or equal
# <= Less than or equal 
print(10 > 5)
print(1 > 1.5)
print(5.9 != 5.8)
print(9/3 == 3)
print("Jen" < "jen")

temperature = 16
print(temperature < 18)
wind_chill = 3
print(wind_chill > 4)
print(temperature - wind_chill < 16)
name = "Hayley"
print("Hayley" == name)

if 5 != 4:
    print("Hello")

name = "B"
if name == "Jenny":
    print("Hello again")
elif name == "Asli":
    print(f"Congratulations {name}, you're in!")
else:
    print("You have been denied access.")

is_raining = True
temperature = 6
wind_chill = 3
if is_raining:
    print("Remember your umbrella.")
else: 
    print("Do not take an umbrella.")

if temperature - wind_chill < 16:
    print("Take a jumper.")
elif temperature - wind_chill > 30:
    print("It's hot today. Make sure to get some ice packs.")
else:
    print("What a lovely day!")

if temperature - wind_chill < 16 and is_raining:
    print("Just stay home.")
else:
    if is_raining:
        print("You'll need an umbrella today.")
    elif temperature - wind_chill < 16:
        print("You'll need a jumper today!")