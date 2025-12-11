
import sys

def main() -> None:
    print("Program.starting.")
    Args = sys.argv
    if len(Args) != 3:
        print("Invalid.amount.of.arguments.")
        print(f"Synopsis: python {Args[0]} <source_file> <destination_file>")
        return None

    source = Args[1]
    destination = Args[2]

    sourceFile = open(source, "r", encoding="UTF-8")
    destinationFile = open(destination, "w", encoding="UTF-8")

    for Line in sourceFile:
        destinationFile.write(Line)

    sourceFile.close()
    destinationFile.close()
    print("Program.ending.")
    return None

main()
