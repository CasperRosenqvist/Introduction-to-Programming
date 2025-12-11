
RGB_MIN = 0
RGB_MAX = 255

def collector(name: str) -> int:
    feed = input(f"Insert {name}: ")
    try:
        value = int(feed)
    except ValueError:
        raise ValueError(f"'{feed}' is non-numeric value. \n Couldn't perform the designed task due to the invalid input values. ")
    if value < RGB_MIN or value > RGB_MAX:
        raise Exception(f'Value "{value}" is out of range 0-255.')
    return value

def main() -> None:
    print("Program starting.")
    try:
        r = collector("red")
        g = collector("green")
        b = collector("blue")
        print("RGB Details:")
        print(f"- Red: {r}")
        print(f"- Green: {g}")
        print(f"- Blue: {b}")
        hexcode = "{:02x}{:02x}{:02x}".format(r, g, b)
        print(f"- Hex: #{hexcode}")
    except Exception as err:
        print(err)
    print("Program ending.")
    return None


main()
