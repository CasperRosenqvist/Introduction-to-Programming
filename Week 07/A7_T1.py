def collector():
    print("Collect positive integers.")
    integers = []
    while True:
        integer = int(input("Insert positive integer (negative stops): "))
        if integer >= 0:
            integers.append(integer)
        else:
            print("Stopped collecting positive integers.")
            break
    return integers


def results(integers):
    if len(integers) == 0:
        print("No integers to display.")
    else:
        print(f"Displaying {len(integers)} integers:")
        index = 0
        for value in integers:
            ordinal = index + 1
            print(f"-Index: {index} -> Ordinal: {ordinal} -> Integer: {value}")
            index += 1

def main():
    print("Program starting.")
    integers = collector()
    results(integers)
    print("Program ending.")

if __name__ == "__main__":
    main()