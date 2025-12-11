
########################################################
# Task A10_T6
# Developer Casper Rosenqvist
# Date 2025-12-10
########################################################

import copy
import time
from typing import Callable

def readValues(PValues: list[int|float]) -> str:
    filename = input("Insert dataset filename: ")
    PValues.clear()
    with open(filename, "r") as f:
        for line in f:
            s = line.strip()
            if s != "":
                PValues.append(int(s))
    return filename

def quickSort(PNums: list[int]) -> list[int]:
    if len(PNums) <= 1:
        return PNums
    pivot = PNums[len(PNums)//2]
    left = [x for x in PNums if x < pivot]
    mid  = [x for x in PNums if x == pivot]
    right= [x for x in PNums if x > pivot]
    return quickSort(left) + mid + quickSort(right)

def bubbleSort(PNums: list[int]) -> list[int]:
    a = copy.deepcopy(PNums)
    n = len(a)
    for i in range(n-1):
        for j in range(0, n-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

def measureSortingTime(PSortingAlgorithm: Callable, PArr: list[int]) -> int:
    start = time.perf_counter_ns()
    PSortingAlgorithm(PArr)
    end = time.perf_counter_ns()
    return end - start

def main() -> None:
    print("Program starting.")
    Values: list[int] = []
    Results: list[str] = []
    dataset_name = ""
    builtin_ns = None
    bubble_ns = None
    quick_ns = None
    while True:
        print("Options:")
        print("1 - Read dataset values")
        print("2 - Measure speeds")
        print("3 - Save results")
        print("0 - Exit")
        choice = input("Your choice: ")
        if choice == "1":
            dataset_name = readValues(Values)
        elif choice == "2":
            builtin_ns = measureSortingTime(sorted, copy.deepcopy(Values))
            bubble_ns = measureSortingTime(bubbleSort, copy.deepcopy(Values))
            quick_ns = measureSortingTime(quickSort, copy.deepcopy(Values))
            print(f"Measured speeds for dataset '{dataset_name}':")
            print(f" - Built-in sorted {builtin_ns} ns")
            print(f" - Buble sort {bubble_ns} ns")
            print(f" - Quick sort {quick_ns} ns")
        elif choice == "3":
            save_name = input("Insert results filename: ")
            Results.clear()
            Results.append(f"Measured speeds for dataset '{dataset_name}':")
            Results.append(f" - Built-in sorted {builtin_ns} ns")
            Results.append(f" - Buble sort {bubble_ns} ns")
            Results.append(f" - Quick sort {quick_ns} ns")
            with open(save_name, "w") as f:
                for line in Results:
                    f.write(line + "\n")
        elif choice == "0":
            print("Exiting program.")
            break
    Values.clear()
    Results.clear()
    print("Program ending.")

if __name__ == "__main__":
    main()
