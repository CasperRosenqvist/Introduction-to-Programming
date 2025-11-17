def collector(integers):
    print("Collect positive integers.")
    index = -1
    while True:
        integer = int(input("Insert positive integer (negative stops): "))
        if integer >= 0:
            integers.append(integer)
            index += 1
        elif integer < 0:
            print("Stopped collecting positive integers.")
            break
    return integers

def results(total):
    print(f"Dispalying {len(total)} integers")

def main():
    print("Program starting.")
    integers = []
    total = collector(integers)
    results(total)
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()