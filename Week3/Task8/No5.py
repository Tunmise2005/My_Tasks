# store inventory
store = {"Book": 20, "Pen": 30, "Bag": 15}

# inventory update
user = input("What would like to buy? ")
quantity = input("How many do you want to buy? ")

# using assignment operator
store[user] -= quantity
print(store)