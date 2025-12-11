########################################################
# Task A10_T1
# Developer Casper Rosenqvist
# Date 2025-12-10
########################################################

def fileHandle(filename):
    with open(filename, 'r') as f:
        values = [line.strip() for line in f.readlines()]
    return values



def main():
    print("Program starting.")
    filename = input("Insert filename: ")
    values = fileHandle(filename)
    print("#----Vertically----#")
    for v in values:
        print(v)
    print("#----Vertically----#")
    print("#----Horizontally----#")
    print(", ".join(values))
    print("#----Horizontally----#")
    print("Program-ending.")

if __name__ == "__main__":
    main()