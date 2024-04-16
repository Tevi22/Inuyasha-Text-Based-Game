# Dictionary containing locations and items
locations = {
    'Koede`s Village': {'South': 'Outskirt Land`s', 'East': 'The Forest of InuYasha'},
    'The Forest of InuYasha': {'West': 'Koede`s Village', 'Item': 'Shikon Jewel Shard'},
    'Outskirt Land`s': {'North': 'Koede`s Village', 'South': 'Mushin`s Temple', 'West': 'Toga`s Tomb',
                        'East': 'Temple of Kannon', 'Item': 'Fire Robe'},
    'Toga`s Tomb': {'East': 'Outskirt Land`s', 'Item': 'Shikon Jewel Shard'},
    'Totosai Blacksmith Hut': {'South': 'Temple of Kannon', 'Item': 'Tenseiga'},
    'Temple of Kannon': {'North': 'Totosai Blacksmith Hut', 'West': 'Outskirt Land`s', 'Item': 'Shikon Jewel Shard'},
    'Mushin`s Temple': {'North': 'Outskirt Land`s', 'East': 'Mt. Hakurai', 'Item': 'Shikon Jewel Shard'},
    'Mt. Hakurai': {'West': 'Mushin`s Temple'}
}

# Initialize current location
current_location = 'Koede`s Village'

# Inventory to store collected items
inventory = []

# Required items to win the game
required_item = ['Shikon Jewel Shard', 'Shikon Jewel Shard', 'Shikon Jewel Shard', 'Shikon Jewel Shard', 'Tenseiga',
                 'Fire Robe']


# Function to show game instructions
def show_instructions():
    print(
        "\nWelcome to InuYasha: Quest for The Shikon Jewels Text Adventure Game!"
        "\nObjective:"
        "\n- Defeat the evil demon Naraku by collecting all four shards of the Shikon Jewel."
        "\n- Find Inuyasha's demon-slaying sword, Tenseiga, and the demon fire robe to protect yourself."
        "\n\nWinning and Losing:"
        "\n- To win the game, collect all required items and reach Mt. Hakurai."
        "\n- If you reach Mt. Hakurai without all required items, Naraku will overpower you, and you'll lose the game."
        "\n\nInstructions:"
        "\n- Use commands like 'go north,' or 'north,' 'go east,' or 'east' to navigate."
        "\n- Type 'get item' or 'item' to collect items in a location."
        "\n- Type 'location' or 'where am I' to check your current location."
        "\n- Type 'exit' to end the game."
        "\n\nLet the adventure begin!"
    )


# Function to show initial status
def show_status():
    global current_location
    print('\nCurrent Location', current_location)
    if 'Item' in locations[current_location]:
        print('Item in this Location:', locations[current_location]['Item'])
        get_item()
    print('Inventory:', inventory)
    print('Directions:', ', '.join(locations[current_location].keys()))
    print('----------------------------')


# Call the function to show instructions and initial status
show_instructions()
show_status()


# Function to move between locations
def move(direction):
    global current_location
    if 'south' in direction or 'go south' in direction:
        direction = 'South'
    elif 'east' in direction or 'go east' in direction:
        direction = 'East'
    elif 'west' in direction or 'go west' in direction:
        direction = 'West'
    elif 'north' in direction or 'go north' in direction:
        direction = 'North'
    # Helps user find there current location
    elif 'location' in direction or 'where am I' in direction:
        print('You are currently at', current_location)
        return current_location
    elif 'get item' in direction or 'item' in direction:
        get_item()
        return current_location
    else:
        print('Invalid direction')
        return current_location  # Return the current location if the command is not recognized

    if direction in locations[current_location]:
        current_location = locations[current_location][direction]
        print('\nYou have moved', direction.lower(), 'to', current_location + '.')
        return current_location
    else:
        print('\nInvalid direction.')
        return current_location


# Function to collect items
def get_item():
    global current_location
    if 'Item' in locations[current_location]:
        item = locations[current_location]['Item']
        inventory.append(item)
        print('\nYou have collected:', item)
        # Remove the item from the location dictionary to prevent duplication
        del locations[current_location]['Item']
    else:
        print('\nNo items are available')


# Function to update new status
def get_new_status():
    global current_location
    global locations
    global inventory

    print('\nCurrent Location:', current_location)

    print('Inventory:', inventory)

    if 'Item' in locations[current_location]:
        item_name = locations[current_location]['Item']
        print(f'You see the great sword {item_name}' if item_name == 'Tenseiga' else f'You see a {item_name}')

    print('Directions:', ', '.join(locations[current_location].keys()))

    print('----------------------------')


# Main Program
while True:
    # Take user input as direction
    user_input = input('Enter your move: ').lower()

    # Check for exit condition
    if user_input == 'exit':
        print('You have exited the game')
        exit()

    # Move based on user input and get new location
    current_location = move(user_input)

    # Display updated status information to the user
    get_new_status()

    # Game end conditions
    if current_location == 'Mt. Hakurai':
        if all(item in inventory for item in required_item):
            print("\nThe Evil Demon Naraku was no match for your full-demon form."
                  "\n\n··········································"
                  "\n:__   __           __        ___       _ :"
                  "\n:\ \ / /__  _   _  \ \      / (_)_ __ | |:"
                  "\n: \ V / _ \| | | |  \ \ /\ / /| | '_ \| |:"
                  "\n:  | | (_) | |_| |   \ V  V / | | | | |_|:"
                  "\n:  |_|\___/ \__,_|    \_/\_/  |_|_| |_(_):"
                  "\n··········································"
                  "\n\nThanks for playing the game. Hope you enjoyed it."
                  )
            exit()
        else:
            print("\nNaraku: You were a fool to come here unprepared."
                  "\nNaraku overwhelms you with his power."
                  "\n\n·····················································"
                  "\n:  ____                         ___                 :"
                  "\n: / ___| __ _ _ __ ___   ___   / _ \__   _____ _ __ :"
                  "\n:| |  _ / _` | '_ ` _ \ / _ \ | | | \ \ / / _ \ '__|:"
                  "\n:| |_| | (_| | | | | | |  __/ | |_| |\ V /  __/ |   :"
                  "\n: \____|\__,_|_| |_| |_|\___|  \___/  \_/ \___|_|   :"
                  "\n·····················································"
                  "\n\nThanks for playing the game. Hope you enjoyed it."
                  )
            exit()
