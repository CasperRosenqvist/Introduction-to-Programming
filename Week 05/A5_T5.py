def option_menu():
    print("Options:")
    print("1 - Insert word")
    print("2 - Show current word")
    print("3 - Show current word in reverse")
    print("0 - Exit")
    choice = int(input("Your choice: "))
    return choice

def main():
    print("Program starting.")
    word = ""
    while True:
        choice = option_menu()
        if choice == 1:
            word = input("Insert word: ")
            print("")
        elif choice == 2:
            print(f"Current word - \"{word}\"\n")
        elif choice == 3:
            print(f"Word reversed - \"{word[::-1]}\"\n")
        elif choice == 0:
            print("Exiting program.")
            break
        elif choice < 0 or choice > 3:
            print("Unknown option! Try again.\n")

    print("program ending.")

main()