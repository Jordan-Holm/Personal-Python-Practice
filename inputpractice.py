test_dict = {}
test_questions = ["First Name", "Last Name", "Age", "Birthday", "Password"]

def input_to_list():
    for question in test_questions:
        user_input = input(f"Enter your {question}: ")
        test_dict[question] = user_input

def output_dict():
    for question, value in test_dict.items():
        print(f"{question}: {value}")

input_to_list()
output_dict()