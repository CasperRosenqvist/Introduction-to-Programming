def collector(values):
    integers = input("Insert comma-separated integers: ")
    parts = integers.split(",")
    for part in parts:
        part = part.strip()
        if part.isnumeric():
            values.append(int(part))
        else:
            print(f"Invalid value detected: '{part}'")
    return None

def analyse(values):
    if len(values) == 0:
        print("No valid integers to analyze.")
    else:
        total = sum(values)
        parity = "even" if total % 2 == 0 else "odd"
        print(f"There are {len(values)} integers in the list.")
        print(f"Sum of the integers is: {total} and it's {parity}")

def main():
    print("Program starting.")
    values: list[int] = []
    collector(values)
    analyse(values)
    print("Program ending.")

if __name__ == "__main__":
    main()