########################################################
# Task A10_T2
# Developer Casper Rosenqvist
# Date 2025-12-10
########################################################


def fileHandle(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    return [int(number) for number in lines]

def main():
    print("Program starting.")
    filename = input("Insert filename: ")
    numbers = fileHandle(filename)

    total_sum = sum(numbers)
    total_product = 1
    for number in numbers:
        total_product *= number

    print("# --- Sum of numbers --- #")
    print(total_sum)
    print("# --- Sum of numbers --- #")
    print("# --- Sum of numbers --- #")
    print("# --- Product of numbers --- #")
    print(total_product)
    print("# --- Product of numbers --- #")
    print("Program ending.")

if __name__ == "__main__":
    main()
