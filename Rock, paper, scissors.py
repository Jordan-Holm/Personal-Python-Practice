import random

win_color = "win"
lose_color = "lose"
#main menu for player to choose which mode to play
def menu():
    print("Welcome to Rock, Paper, Scissors. \n Press 1 to play quick round. \n press 2 for best 2 out of 3")
    user_input = int(input())
    if user_input == 1:
        quick_round()
    elif user_input == 2:
        best_of()
    else:
        print("Invalid input please try again")
        menu()

#takes player input to determine what their play is
def player_turn():
    player_input = int(input("Select: 1 for Rock, 2 for Paper, 3 for Scissors"))
    match player_input:
        case 1:
            return "Rock"
        case 2:
            return "Paper"
        case 3:
            return "Scissors"
        case _:
            print("Invalid input, try again")
            player_turn()
    
#Randomly picks a play for the computer
def computer_turn():
    computer_input = int(random.randint(1,3))
    match computer_input:
        case 1:
            return "Rock"
        case 2:
            return "Paper"
        case 3:
            return "Scissors"
        case _:
            print("computer failure")

#takes both the player_choice & the computer_choice to determine who won
def determine_winner(player_choice, computer_choice):
    

    if player_choice == computer_choice:
        round_conclusion = "Draw!"
        print(round_conclusion)
        winner = "None"
        return winner
    elif player_choice == "Rock" and computer_choice == "Paper":
        round_conclusion = f"You {lose_color}! Rock loses to Paper"
        print(round_conclusion)
        winner = "Computer"
        return winner
    elif player_choice == "Rock" and computer_choice == "Scissors":
        round_conclusion = f"You {win_color}! Rock beats Scissors"
        print(round_conclusion)
        winner = "Player"
        return winner
    elif player_choice == "Paper" and computer_choice == "Rock":
        round_conclusion = f"You {win_color}! Paper beats Rock"
        print(round_conclusion)
        winner = "Player"
        return winner
    elif player_choice == "Paper" and computer_choice == "Scissors":
        round_conclusion = f"You {lose_color}! Paper loses to Scissors"
        print(round_conclusion)
        winner = "Computer"
        return winner
    elif player_choice == "Scissors" and computer_choice == "Rock":
        round_conclusion = f"You {lose_color}! Scissors loses to Rock"
        print(round_conclusion)
        winner = "Computer"
        return winner
    elif player_choice == "Scissors" and computer_choice == "Paper":
        round_conclusion = f"You {win_color}! Scissors beats Paper"
        print(round_conclusion)
        winner = "Player"
        return winner
    else:
        print("Error, rebooting menu")
        menu()

#Starts the quick round game mode
def quick_round():
    player_choice = player_turn()
    print(f"Player choice: {player_choice}")
    computer_choice = computer_turn()
    print(f"Computer choice: {computer_choice}")

    winner = determine_winner(player_choice, computer_choice)
    menu()

#Starts the best two out of three game mode
def best_of():
    player_score = 0
    computer_score = 0

    for i in range(10):
        if player_score < 3 and computer_score < 3:
            player_choice = player_turn()
            print(f"Player selection: {player_choice}")
            computer_choice = computer_turn()
            print(f"Computer selection: {computer_choice}\n")

            round_winner = determine_winner(player_choice, computer_choice)
            if round_winner == "Player":
                player_score += 1
            elif round_winner == "Computer":
                computer_score += 1
            print(f"Player: {player_score}\nComputer: {computer_score}")
        else:
            break

    # Shows the final winner and how many points they lost by
    if player_score > computer_score:
        print(f"You {win_color} by {player_score - computer_score} points!")
    else:
        print(f"You {lose_color} by {computer_score - player_score} points")

    menu()
    
        

menu()