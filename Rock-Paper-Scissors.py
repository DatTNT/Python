from typing import Counter
import random


def get_choice(choice):
    if choice == "R":
        return "Rock"
    elif choice == "P":
        return "Paper"
    elif choice == "S":
        return "Scissor"
    else:
        return "Your choice not avaible"


def main():
    print("Welcome to Rock, Paper, Scissor Game")
    print("[R] = Rock, [P] = Paper, [S] = Scissor, [Q] = Quit!!!")

    choices = ["R", "P", "S"]
    counter = 1
    game_on = True

    while game_on:
        user_choice = input(f"Game #{counter}. Please enter your choice: ")
        user_choice = user_choice.upper()

        if user_choice == "Q":
            print('Thanks for joining ! Have a nice day :)')
            game_on = False
        else:
            random_index = random.randint(0, 2)
            computer_choice = choices[random_index]

            print(
                f"You select {get_choice(user_choice)} vs Computer choice is {get_choice(computer_choice)}")
            # Winning rules
            if user_choice == "R" and computer_choice == "P":
                print("You lose, The Computer Winn")
            elif user_choice == "R" and computer_choice == "S":
                print("Congrat, you win")
            elif user_choice == "P" and computer_choice == "R":
                print("Congrat, you win")
            elif user_choice == "P" and computer_choice == "S":
                print("You lose, The Computer Winn")
            elif user_choice == "S" and computer_choice == "R":
                print("You lose, The Computer Winn")
            elif user_choice == "S" and computer_choice == "P":
                print("Congrat, you win")
            elif user_choice == computer_choice:
                print(
                    f"Fairrrrrr Because Both you and computer selected {get_choice(user_choice)}")
            else:
                print("Pls enter:[R], [P], [S]")
            counter += 1
        print("-"*40)


if __name__ == "__main__":
    main()
