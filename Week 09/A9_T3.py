
import sys

def readLines(PFilepath: str, PLines: list[str]) -> None:
    try:
        Filehandle = open(PFilepath, 'r')
        Line = Filehandle.readline()
        while Line != '':
            PLines.append(Line)
            Line = Filehandle.readline()
    except Exception:
        print(f"Couldn't read file \"{PFilepath}\"")
        sys.exit(1)
        return None

def main() -> None:
    print("Program starting.")
    Lines: list[str] = []
    Filename = input("Insert filename: ")
    readLines(Filename, Lines)
    print(f"Reading from file: {Filename}")
    for Line in Lines:
        print(Line)
    print("Program ending.")
    return None

main()
