#list is used to store multiple items in a single variable

food = ["pizza", "pasta", "dosa","rice"]
food[0] = "sushi"
#print(food)
#print(food[0])
#print(food[2])
#print(food[1])

food.append("ice cream")
food.remove("sushi")
food.pop()
food.insert(0, "cake")
food.sort()
food.clear()

for x in food:
    print(x)