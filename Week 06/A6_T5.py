SEPARATOR = ";"


def readValues(fname: str) -> str:
    file = open(fname, "r")
    numbers = file.readlines()
    file.close()

    Values: str = ""
    for i in range(len(numbers)):
        Values += str(numbers[i].strip())
        if i < len(numbers) - 1:
            Values += SEPARATOR
    return Values


def analyseValues(value: str) -> str:
    nums = [int(x) for x in value.split(SEPARATOR)]
    count = len(nums)
    total = sum(nums)
    greatest = max(nums)
    average = total / count if count > 0 else 0
    data_row = f"{count};{total};{greatest};{average:.2f}"
    return f"Count;Sum;Greatest;Average\n{data_row}\n"


def main():
    print("Program starting.")
    fname = input("Insert filename: ")
    print("#### Number analysis - START ####")
    print(f'File "{fname}" results:')
    print("Count;Sum;Greatest;Average")
    value = readValues(fname)
    result = analyseValues(value)
    print(result, end="")
    print("\n#### Number analysis - END ####")
    print("Program ending.")


if __name__ == "__main__":
    main()