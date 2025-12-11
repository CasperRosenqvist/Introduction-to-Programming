from A8_T3Lib import read_values, amount_of_values, sum_of_values, average_of_values

def askChoice() -> int:
    try:
        return int(input("Your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        return -1  # Invalid selection

def showOptions() -> None:
    print("Options:")
    print("1. Read values from file")
    print("2. Show amount of values")
    print("3. Calculate sum of values")
    print("4. Calculate average of values")
    print("0. Exit")

def calculate() -> None:
    values = []
    while True:
        print()
        showOptions()
        choice = askChoice()

        match choice:
            case 1:
                filename = input("Insert filename: ")
                try:
                    values = read_values(filename)
                    print("Values loaded successfully.")
                except Exception as e:
                    print(f"Error loading file: {e}")

            case 2:
                print(f"Amount of values: {amount_of_values(values)}")

            case 3:
                if not values:
                    print("No values loaded yet!")
                else:
                    print(f"Sum of values: {sum_of_values(values):.1f}")

            case 4:
                if not values:
                    print("No values loaded yet!")
                else:
                    print(f"Average of values: {average_of_values(values):.1f}")

            case 0:
                print("Exiting program.")
                break

            case _:
                print("Unknown choice. Try again.")

def main() -> None:
    print("Program starting.")
    calculate()
    print("Program ending.")

if __name__ == "__main__":
    main()
