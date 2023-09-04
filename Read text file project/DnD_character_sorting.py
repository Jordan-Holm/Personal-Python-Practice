character_file = open("D&D Characters.txt", 'r')
character_data = character_file.readlines()

def sort_characters():
    character_list = []

    character_dict = {'Name': '', 'Player': '', 'Class': '', 'Sub-Class': '', 'Race': '', 'Level': ''}

    new_line = []
    for line in character_data:
        new_line.append(line.strip())

    for line in new_line:

        if line:
            key, value = line.split(": ", 1)
            character_dict[key] = value

        if 'Level' in line:
            character_list.append(character_dict.copy())
            character_dict = {'Name': '', 'Player': '', 'Class': '', 'Sub-Class': '', 'Race': '', 'Level': ''}
    character_file.close()
    return character_list

def view_sorted_list():
    character_list = sort_characters()
    for character in character_list:
        for character_key, character_value in character.items():
            if character_key == "Level":
                print(f"{character_key}: {character_value}\n")
            else:
                print(f"{character_key}: {character_value}")