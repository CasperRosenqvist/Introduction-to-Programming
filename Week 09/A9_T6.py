
def printOptions() -> None:
    print("Options:")
    print("1 - Insert line")
    print("2 - Save lines")
    print("0 - Exit")

def insertLine(Lines: list[str]) -> None:
    Text = input("Insert text:")
    Lines.append(Text)

def saveLines(Lines: list[str]) -> None:
    Filename = input("Insert filename:")
    with open(Filename, "w") as Filehandle:
        for Line in Lines:
            Filehandle.write(Line + "\n")

def main() -> None:
    print("Program starting.")
    Lines: list[str] = []
    while True:
        printOptions()
        try:
            Choice = input("Your choice:")
        except KeyboardInterrupt:
            print("^CKeyboard interrupt and unsaved progress!")
            if len(Lines) > 0:
                Answer = input("Save before quit(y/n?):")
                if Answer.lower() == "y":
                    saveLines(Lines)
            break

        if Choice == "1":
            insertLine(Lines)
        elif Choice == "2":
            saveLines(Lines)
        elif Choice == "0":
            break
        else:
            print("unknown option!")

    print("Program ending.")
    return None

main()