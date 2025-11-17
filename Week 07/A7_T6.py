import random
random.seed(1234)

def start():
    player = input("Insert player name: ")
    print(f"Welcome {player}!")
    print("Your opponent is RPS-3PO.")
    print("Game starts...")
    return player

def menu():
    print("\nOptions:")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")
    print("0 - Quit game")
    choice = int(input("Your choice: "))
    return choice

def game(player):
    wins = 0
    losses = 0
    draws = 0
    while True:
        choice = menu()
        if choice == 0:
            print("\nGame Over!")
            print(f"{player} - Wins: {wins}, Losses: {losses}, Draws: {draws}")
            break
        if choice not in [1, 2, 3]:
            print("Unknown option, try again!")
            continue

        print("\nRock! Paper! Scissors! Shoot!")
        opponent_choice = random.randint(1, 3)
        options = {1: "Rock", 2: "Paper", 3: "Scissors"}
        print(f"{player} chose {options[choice]}")
        print(f"RPS-3PO chose {options[opponent_choice]}")
        if choice == opponent_choice:
            print("Result: Draw!")
            draws += 1
        elif (choice == 1 and opponent_choice == 3) or (choice == 2 and opponent_choice == 1) or(choice == 3 and opponent_choice == 2):
            print(f"Result: {player} win!")
            wins += 1
        else:
            print(f"Result: {player} lose!")
            losses += 1

def main():
    print("Program starting.")
    print("Welcome to the rock-paper-scissors game!")
    player = start()
    game(player)
    print("Program ending.")


if __name__ == "__main__":
    main()
