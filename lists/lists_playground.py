
# Python Lists start from 0 (index).
characters = ["a", "b", "c"]
print(characters[0])
print(type(characters))

characters.append("d") #add one item to the list
print(characters)

characters.extend(['e', 'f']) #add multiple items to the list
print(characters)

characters.insert(1,"g")
print(characters)
print(characters[3])
print(characters[-1]) #last element in list
print(characters[0:4]) #range

print(characters.pop(4)) #shows what element you are popping.
print(characters.remove("b")) #None

chilli_wishlist = ['igloo', 'chicken', 'donut toy', 'cardboard box']
print(chilli_wishlist)
print(chilli_wishlist[1:3])
chilli_wishlist[1] = 'carrot' #replaces what was in [1]
print(chilli_wishlist)

print(chilli_wishlist[2:4])
print(chilli_wishlist[-3])

print(chilli_wishlist)
chilli_wishlist.append("dig mat")
print(chilli_wishlist.extend(['kong', 'tennis ball', 'crocodile toy']))