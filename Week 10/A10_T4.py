########################################################
# Task A10_T4
# Developer Casper Rosenqvist
# Date 2025-12-10
########################################################


import sys
from A10_TLib import readValues, displayValues

def merge(PLeft: list[int], PRight: list[int], PMerge: list[int], PAsc: bool = True) -> None:
    left_index = 0
    right_index = 0
    merge_index = 0

    while left_index < len(PLeft) and right_index < len(PRight):
        left_val = PLeft[left_index]
        right_val = PRight[right_index]
        if (PAsc and left_val <= right_val) or ((not PAsc) and left_val >= right_val):
            PMerge[merge_index] = left_val
            left_index += 1
        else:
            PMerge[merge_index] = right_val
            right_index += 1
        merge_index += 1

    while left_index < len(PLeft):
        PMerge[merge_index] = PLeft[left_index]
        left_index += 1
        merge_index += 1

    while right_index < len(PRight):
        PMerge[merge_index] = PRight[right_index]
        right_index += 1
        merge_index += 1
    return None

def mergeSort(PValues: list[int], PAsc) -> None:
    size = len(PValues)
    if size <= 1:
        return None
    mid = size // 2
    left = PValues[:mid]
    right = PValues[mid:]
    mergeSort(left, PAsc)
    mergeSort(right, PAsc)
    merge(left, right, PValues, PAsc)
    return None

def main() -> None:
    print("Program-starting.")
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = input("Insert-filename: ")

    numbers: list[int] = []
    readValues(filename, numbers)

    print(f"Raw '{filename}' :--> ", end="")
    displayValues(numbers, Horisontally=True)

    asc_numbers = numbers[:]
    mergeSort(asc_numbers, PAsc=True)
    print(f"Ascending '{filename}' -> ", end="")
    displayValues(asc_numbers, Horisontally=True)

    desc_numbers = numbers[:]
    mergeSort(desc_numbers, PAsc=False)
    print(f"Descending '{filename}' -> ", end="")
    displayValues(desc_numbers, Horisontally=True)


    print("Program-ending.")

if __name__ == "__main__":
    main()
