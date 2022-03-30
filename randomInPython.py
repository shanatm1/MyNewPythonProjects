import random
x = random.randint(1,6)
y = random.random()      #this will give you a random floating number between 0 and 1

myLst = ["rock", "paper", "scissor"]
z = random.choice(myLst)

cards = [1,2,3,4,5,6,7,8,9,"j","q","k","a"]
random.shuffle(cards)

print(x)
print(y)
print(z)
print(cards)
