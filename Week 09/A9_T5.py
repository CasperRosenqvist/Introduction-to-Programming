
RGB_MIN = 0
RGB_MAX = 255

def askIntByte(PPrompt: str) -> int:
    feed = input(PPrompt)
    try:
        value = float(feed)
    except ValueError:
        raise ValueError(f"'{feed}' is non-numeric value.")
    if not value.is_integer():
        raise ValueError(f"'{feed}' is not an integer.")
    value = int(value)
    if value < RGB_MIN or value > RGB_MAX:
        raise ValueError(f'Value "{value}" is out of range 0–255.')
    return value

def createHex(PRed: int, PGreen: int, PBlue: int) -> str:
    return "#{:02x}{:02x}{:02x}".format(PRed, PGreen, PBlue)

def main():
    print("Program starting.")
    try:
        r = askIntByte("Insert red: ")
        g = askIntByte("Insert green: ")
        b = askIntByte("Insert blue: ")
        hexcode = createHex(r, g, b)
        print("RGB Details:")
        print(f"- Red: {r}")
        print(f"- Green: {g}")
        print(f"- Blue: {b}")
        print(f"- Hex: {hexcode}")
        print(f"- Binary: {r:08b} {g:08b} {b:08b}")
    except Exception as err:
        print(err)
        print("Couldn't perform the designed task due to the invalid input values.")
    print("Program ending.")

if __name__ == "__main__":
    main()
