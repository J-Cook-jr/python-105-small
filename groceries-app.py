#This program will create a groceries app that will allow the user to add, update,and remove items.

groceries = []

# Create a while loop that will prompt the user until they hit Enter.
while True:
    item = input("What do you need from the store? ")
    if item == '':
        break
    groceries.append(item)