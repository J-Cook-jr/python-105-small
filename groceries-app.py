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
start_index_to_replace = (input('Which start index item would you like to replace? '))
end_index_to_replace = (input('What is the last index item you want to replace? '))

if start_index_to_replace == '' and end_index_to_replace == '':
    pass
    
     # -replace item at that index with the new item.
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
    print(f'{i}:{item}')   

index_of_item_to_delete = int(input('Would you like to delete an item? Enter the index number or press Enter to exit. '))
   
print('Before delete list')
for i in indexes:
    item = groceries[i]
    print(f'{i}:{item}') 

if index_of_item_to_delete != '':
    del groceries[index_of_item_to_delete]

print('Updated list')
indexes = range(len(groceries))
for i in indexes:
    item = groceries[i]
    print(f'{i}:{item}') 
        
        





