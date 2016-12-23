# make a list to hold onto our items
shopping_list = []

# print out instructions on how to use the app
print("""
--------------------------------------------------------------------
The Shopping List
Copyright 2016 ExplodingCow
This is a simple shopping list intended for educational purposes only.
---------------------------------------------------------------------
What should we pick up at the store?
Enter 'HELP' for list of commands.
""")


# Help
def listhelp():
    print("""
    LIST OF COMMANDS
    DONE - Exits The Shopping List
    SHOW - Shows current items stored in The Shopping List
    HELP - You are already here
    """)


# Removes nonsense
def clearnonsense():
    if 'SHOW' in shopping_list:
        shopping_list.remove('SHOW')
    if 'HELP' in shopping_list:
        shopping_list.remove('HELP')


# Shows The List
def show_list():
    print("Here's your list:")
    for item in shopping_list:
        print(item)
        
        
# Add items to the list (Able to detect singular or multiple)
def add_item():
    shopping_list.append(new_item)
    if len(shopping_list) < 2:
        print("{} has been added to the list. The list now contains 1 item.".format(new_item))
    else:
        print("{} has been added to the list. The list now contains {} items.".format(new_item, len(shopping_list)))


while True:
    # ask for new items
    new_item = input("> ")

    # be able to quit the app
    if new_item == 'DONE':
        clearnonsense()
        break

    # Show current list of items
    elif new_item == 'SHOW':
        clearnonsense()
        for item in shopping_list:
            print(item)
        continue

    # Show a help page
    elif new_item == 'HELP':
        listhelp()
        continue

    # add new items to our list
    add_item()

# print out the list
show_list()
