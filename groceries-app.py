#This program will create a groceries app that will allow the user to add, update,and remove items.

groceries = []

# Create a while loop that will prompt the user until they hit Enter.
while True:
    item = input("What do you need from the store? ")
    if item == '':
        break
    groceries.append(item)


# After "break" python will move to the next unidented line of code after the loop.

# Print the grocery list with indexes.
indexes = range(len(groceries))
for i in indexes:
    item = groceries[i]
    print(f'{i}:{item}')

#Give them the chance to replace items in their cart.
start_index_to_replace = int(input('Which start index item would you like to replace? '))
end_index_to_replace = int(input('What is the last index item you want to replace? '))

if start_index_to_replace == end_index_to_replace:
    #prompt user for new item
    new_item = input('What is the new item? ')

    # -replace item at that index with the new item.
    groceries[start_index_to_replace] = new_item
else:
# Gather replacements.
    replacements = []
    while True:
        new_item = input("What is the new item? ")
        if new_item == '':
            break
        replacements.append(new_item)
        print(replacements)

    print(groceries)
    groceries[start_index_to_replace:end_index_to_replace] = replacements
    print(groceries)

# Print updated combined list.
indexes = range(len(groceries))
for i in indexes:
    item = groceries[i]
    print(f'{i}: {item}')    

delete_index = input("Would you like to delete an indexed item? If yes press Y. If no press Enter? ")
if delete_index == 'Y':
    delete_item = int(input('Which indexed item would you like to delete?'))
    groceries[delete_item] = delete_item
    del groceries[delete_item]

else:
    deletes = []
    while True:
        delete_index = input("Would you like to delete an indexed item? If yes press Y. If no press Enter? ")
        if delete_index == '':
            break
            print(groceries)
    

for delete_item in indexes:
    if groceries[delete_item]:
      print(f'{groceries[delete_item]: {item}')







