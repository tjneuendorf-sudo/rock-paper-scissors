import random
import json
valid_choices = ["rock", "paper" , "scissors"]
play_again_choices = ["yes", "no"]
def computer_choice_func():
    return random.choice(valid_choices)

def player_choice_func():
    while True:
        try:
            raw_player_pick = input("Choose rock, paper, or scissors: ")
            lower_player_pick = raw_player_pick.lower()
            final_player_pick = lower_player_pick.strip()
            if final_player_pick in valid_choices:
                break
            else:
                print("Invalid Option! Please pick rock, paper, or scissors.")
        except Exception as e:
            print(e)
    return final_player_pick

def win_lose_condition(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "draw"
    elif player_choice == "paper" and computer_choice == "rock":
        return "win"
    elif player_choice == "scissors" and computer_choice == "paper":
        return "win"
    elif player_choice == "rock" and computer_choice == "scissors":
        return "win"
    else:
        return "lose"

def show_score(player_score, computer_score):
    return f"Player score is {player_score}. Computer score is {computer_score}."

def play_again_function():
    while True:
        try:
            raw_play_again = input("Do you want to play again? yes or no: ")
            lower_play_again = raw_play_again.lower()
            final_play_again = lower_play_again.strip()
            if final_play_again in play_again_choices:
                break
            else:
                print("Invalid choice. Select yes or no.")
        except Exception as e:
            print(e)
    return final_play_again

def play_game():
    while True:

        player_score = 0
        computer_score = 0
        while player_score < 2 and computer_score < 2:
            computer_choice = computer_choice_func()
            player_choice = player_choice_func()
            who_wins = win_lose_condition(player_choice, computer_choice)
            if who_wins == "draw":
                print (f"Draw! Computer chose {computer_choice}")
                print (show_score(player_score, computer_score))
            elif who_wins == "win":
                print(f"Player Scores! Computer chose {computer_choice}")
                player_score += 1
                print(show_score(player_score, computer_score))
            else:
                print(f"Computer Scores! Computer chose {computer_choice}")
                computer_score += 1
                print(show_score(player_score, computer_score))
        if player_score > computer_score:
            print("Player Wins!")
            return "Player Wins"
        else:
            print("Computer Wins!")
            return "Computer Wins"

def check_create_save():
    try: 
        with open("rps_save.json", 'r') as file: 
            save_file = json.load(file) 
            return save_file 
    except FileNotFoundError: 
        print("Error: the file rps_save.json not found")
        with open("rps_save.json", 'w') as file:
            starting_score = {"player_wins": 0, "computer_wins": 0}
            json.dump(starting_score, file, indent=4)
            return starting_score

def update_save(result):
    with open("rps_save.json",'r') as file:
        updating_save = json.load(file)
    if result == "Player Wins":
        updating_save['player_wins'] += 1
    else:
        updating_save['computer_wins'] += 1
    with open("rps_save.json", 'w') as file:
        json.dump(updating_save, file, indent=4)
        print(updating_save)
        return updating_save

check_create_save()
while True:
    result = play_game()
    update_save(result)
    play_again_choice = play_again_function()
    if play_again_choice == "no":
        break


