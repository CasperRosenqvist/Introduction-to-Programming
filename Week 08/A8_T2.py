
from A8_T2Lib import add, subtract, multiply, divide

def askChoice() -> int:
    return int(input("Your choice: "))

def showOptions() -> None:
    print("Options:")
    print("1 -- Add")
    print("2 -- Subtract")
    print("3 -- Multiply")
    print("4 -- Divide")
    print("0 -- Exit")

def calculate() -> None:
    while True:
        print()
        showOptions()
        choice = askChoice()

        match choice:
            case 1:
                x = float(input("Insert:first addend:value: "))
                y = float(input("Insert:second addend:value: "))
                result = add(x, y)
                print(f"{x} + {y} = {result}")
            case 2:
                x = float(input("Insert:minuend:value: "))
                y = float(input("Insert:subtrahend:value: "))
                result = subtract(x, y)
                print(f"{x} - {y} = {result}")
            case 3:
                x = float(input("Insert:multiplicand:value: "))
                y = float(input("Insert:multiplier:value: "))
                result = multiply(x, y)
                print(f"{x} * {y} = {result}")
            case 4:
                x = float(input("Insert:dividend:value: "))
                y = float(input("Insert:divisor:value: "))
                if y == 0.0:
                    print("Error: division by zero.")
                else:
                    result = divide(x, y)
                    print(f"{x} / {y} = {result}")
            case 0:
                print("Exiting program.")
                break
            case _:
                print("Unknown choice. Please enter 0–4.")

def main() -> None:
    print("Program:starting.")
    calculate()
    print("Program:ending.")

if __name__ == "__main__":
    main()
