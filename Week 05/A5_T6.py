def askChoice():
    choice = int(input("Your choice: "))
    return choice

def showOptions():
    print("Options:")
    print("1 - Show count")
    print("2 - Increase count")
    print("3 - Reset count")
    print("0 - Exit")
    return None



def main():
    print("Program starting.")
    showOptions
    choice = askChoice
    count = 0
    while True:
        if choice == 1:
            print(f"Current count - {count}")
        elif choice == 2:
            count + 1
            print("Count increased!")
        elif choice == 3:
            count = 0
            print("Cleared count")
        elif choice == 0:
            print("Exiting program.")
            break
        elif choice.isnumeric() or choice < 0 or choice > 3:
            print("Unknown option!")
        
    print("Program ending.")

    main()