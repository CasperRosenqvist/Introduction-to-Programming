########################################################
# Task A10_T3
# Developer Casper Rosenqvist
# Date 2025-12-10
########################################################


import sys
from A10_TLib import readValues, quickSort, displayValues

def main():
    print("Program-starting.")
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = input("Insert-filename: ")

    numbers = []
    readValues(filename, numbers)

    print(f"Raw '{filename}' -> ", end="")
    displayValues(numbers, Horisontally=True)

    asc_numbers = numbers[:]
    quickSort(asc_numbers, PAsc=True)
    print(f"Ascending '{filename}' -> ", end="")
    displayValues(asc_numbers, Horisontally=True)

    desc_numbers = numbers[:]
    quickSort(desc_numbers, PAsc=False)
    print(f"Descending '{filename}' -> ", end="")
    displayValues(desc_numbers, Horisontally=True)

    print("Program-ending.")

if __name__ == "__main__":
    main()
