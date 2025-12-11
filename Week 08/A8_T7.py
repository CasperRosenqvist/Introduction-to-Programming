
import math
import svgwrite
from svgwrite import Drawing
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


def drawHexagon(PDwg: Drawing) -> None:
    print("Insert hexagon")
    cx = int(input("--Center x coord: "))
    cy = int(input("--Center y coord: "))
    a = float(input("--Apothem length: "))
    R = 2 * a / math.sqrt(3)
    pts = [
        (cx + R / 2, cy - (math.sqrt(3) * R / 2)),
        (cx + R, cy),
        (cx + R / 2, cy + (math.sqrt(3) * R / 2)),
        (cx - R / 2, cy + (math.sqrt(3) * R / 2)),
        (cx - R, cy),
        (cx - R / 2, cy - (math.sqrt(3) * R / 2))
    ]
    pts = [(int(round(x)), int(round(y))) for x, y in pts]


def saveSvg(PDwg: Drawing) -> None:
    filename = input("Insert filename: ")
    print(f'Saving file to "{filename}"')
    confirm = input("Proceed (y/n)?: ")
    if confirm.lower() == "y":
        PDwg.saveas(filename)
        print("Vector saved successfully!")


def main() -> None:
    print("Program starting.")
    Dwg = svgwrite.Drawing(size=(500, 400))
    while True:
        print("Options:")
        print("1--Draw square")
        print("2--Draw circle")
        print("3--Draw hexagon")
        print("4--Save svg")
        print("0--Exit")
        choice = input("Your choice: ")
        if choice == "1":
            drawSquare(Dwg)
        elif choice == "2":
            drawCircle(Dwg)
        elif choice == "3":
            drawHexagon(Dwg)
        elif choice == "4":
            saveSvg(Dwg)
        elif choice == "0":
            print("Exiting program.")
            break
    print("Program ending.")


if __name__ == "__main__":
    main()
