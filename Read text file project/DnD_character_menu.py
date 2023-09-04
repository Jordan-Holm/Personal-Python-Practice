from DnD_character_sorting import view_sorted_list
from DnD_create_character import add_character_to_character_list

def menu():
    print("Welcome to D&D Campaign info")
    print(
        "Please select what you'd like to do\n",
        "1. View Campaign Characters\n",
        "2. View Inventory\n",
        "3. Add Item To Inventory\n",
        "4. Add Character To Campaign"

    )
    user_input = int(input())
    determine_user_input(user_input)

def determine_user_input(user_input):
    match user_input:
        case 1:
            print(view_sorted_list())
            menu()
        case 2:
            print("Not yet implemented")
            menu()
        case 3:
            print("Not yet implemented")
            menu()
        case 4:
            add_character_to_character_list()
            menu()
        case _:
            print("Invalid input")
            menu()

menu()