character_file = open("D&D Characters.txt", 'a')
from DnD_character_sorting import sort_characters

def create_character():
    character_dict = {'Name': '', 'Player': '', 'Class': '', 'Sub-Class': '', 'Race': '', 'Level': ''}

    for key in character_dict:
        value = input(f"Please enter {key}: ")
        character_dict[key] = value

    return character_dict

def add_character_to_character_list():
    new_character = create_character()
    character_file.write("\n")
    for key, value in new_character.items():
        if key == "Level":
            character_file.write(f"{key}: {value}")
        else:
            character_file.write(f"{key}: {value}\n")

    print("Character added")
    character_file.close()
