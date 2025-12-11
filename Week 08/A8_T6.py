
import svgwrite
from svgwrite import Drawing, cm
from svgwrite.shapes import Rect, Circle, Polygon


def drawSquare(PDwg: Drawing) -> None:
    print("Insert square")
    x = int(input("--Left edge position: "))
    y = int(input("--Top edge position: "))
    side = int(input("--Side length: "))
    fill = input("--Fill color: ")
    stroke = input("--Stroke color: ")
    PDwg.add(Rect(insert=(x, y), size=(side, side), fill=fill, stroke=stroke))


def drawCircle(PDwg: Drawing) -> None:
    print("Insert circle")
    cx = int(input("--Center x coord: "))
    cy = int(input("--Center y coord: "))
    r = int(input("--Radius: "))
    fill = input("--Fill color: ")
    stroke = input("--Stroke color: ")
    PDwg.add(Circle(center=(cx, cy), r=r, fill=fill, stroke=stroke))


def saveSvg(PDwg: Drawing) -> None:
    filename = input("Insert filename: ")
    print(f'Saving file to "{filename}"')
    confirm = input("Proceed (y/n)?: ")
    if confirm.lower() == "y":
        PDwg.saveas(filename, pretty=True)
        print("Vector saved successfully!")


def main() -> None:
    print("Program starting.")
    Dwg = svgwrite.Drawing(size=(400, 200))  # Canvas size
    while True:
        print("Options:")
        print("1--Draw square")
        print("2--Draw circle")
        print("3--Save svg")
        print("0--Exit")
        choice = input("Your choice: ")
        if choice == "1":
            drawSquare(Dwg)
        elif choice == "2":
            drawCircle(Dwg)
        elif choice == "3":
            saveSvg(Dwg)
        elif choice == "0":
            print("Exiting program.")
            break
    print("\nProgram ending.")


if __name__ == "__main__":
    main()
