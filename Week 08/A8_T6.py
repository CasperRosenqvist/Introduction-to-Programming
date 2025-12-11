
from drawLib import drawCircle, drawSquare, saveSvg, Drawing

def main() -> None:
    Dwg = Drawing()
    print("Program starting.")
    while True:
        showOptions()
        choice = askChoice()
        match choice:
            case 1:
                print('Insert square')
                left = int(askValue1("Left edge position"))
                top = int(askValue1("Top edge position"))
                size = int(askValue1("Size"))
                drawSquare(Dwg, left, top, size)
            case 2:
                print('Insert circle')
                cx = int(askValue1("Center X position"))
                cy = int(askValue1("Center Y position"))
                r = int(askValue1("Radius"))
                drawCircle(Dwg, cx, cy, r)
            case 3:
                filename = askValue2("Filename")
                confirm = askValue2("Confirm save (y/n)")
                if confirm.lower() == "y":
                    saveSvg(Dwg, filename)
            case 0:
                print("Exiting program.\n")
                break
        print()
    print("Program ending.")

def showOptions() -> None:
    print("Options:")
    print("1 - Draw square")
    print("2 - Draw circle")
    print("3 - Save svg")
    print("0 - Exit")

def askChoice() -> int:
    return int(input("Your choice: "))

def askValue1(PPrompt: str) -> str:
    return input(f"- {PPrompt}: ")

def askValue2(PPrompt: str) -> str:
    return input(f"{PPrompt}: ")

if __name__ == "__main__":
    main()
