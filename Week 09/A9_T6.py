
def showOptions() -> None:
    print("Options:")
    print("1 - Insert line")
    print("2 - Save lines")
    print("0 - Exit")

def askChoice() -> int:
    try:
        return int(input("Your choice: "))
    except ValueError:
        return -1

def saveLines(PLines: list[str]) -> None:
    try:
        filename = input("Insert filename: ")
        with open(filename, "w") as filehandle:
            for line in PLines:
                filehandle.write(line + "\n")
    except Exception as err:
        print(err)

def insertLine(PLines: list[str]) -> None:
    text = input("Insert text: ")
    PLines.append(text)

def onInterrupt(PLines: list[str]) -> None:
    try:
        if len(PLines) > 0:
            answer = input("Save before quit (y/n?): ")
            if answer.lower() == "y":
                saveLines(PLines)
    except Exception as err:
        print(err)

def main() -> None:
    Lines: list[str] = []
    Choice = -1
    print("Program starting.")
    try:
        while Choice != 0:
            showOptions()
            Choice = askChoice()
            if Choice == 1:
                insertLine(Lines)
            elif Choice == 2:
                saveLines(Lines)
            elif Choice == 0:
                print("Exiting program.")
            else:
                print("Unknown option!")
            print("")
    except KeyboardInterrupt:
        print("^C Keyboard interrupt and unsaved progress!")
        onInterrupt(Lines)
    Lines.clear()
    print("Program ending.")

if __name__ == "__main__":
    main()
