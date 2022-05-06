
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
chilli_wishlist.insert(1, 'peanut butter')
print(chilli_wishlist)

chilli_wishlist.insert(-2, 'snacks')
chilli_wishlist.pop(2)
chilli_wishlist.remove('igloo')
print(chilli_wishlist)

# Logic
if "tennis ball" in chilli_wishlist:
    print("Chilli would like a tennis ball!")
else:
    print("Chilli doesn't feel like playing fetch.")

if "blueberries" in chilli_wishlist:
    print("Chilli loves blueberries!")
else:
    chilli_wishlist.append("blueberries")
    print(chilli_wishlist)
    print("Chilli's wishlist now has blueberries.")

chilli_wishlist = [
    ['igloo'], #bed
    ['donut toy','tennis ball', 'crocodile toy'], # toys
    ['chicken', 'peanut butter'], # treats
    ['cardboard box', 'kong', 'dig mat'] # activity based toys
]

print(chilli_wishlist[2])
print(chilli_wishlist[2][1])