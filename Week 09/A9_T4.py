
TEMP_MIN = -273.15
TEMP_MAX = 10000

def collectCelsius() -> float:
    feed = input("Insert Celsius: ")
    try:
        celsius = float(feed)
    except ValueError:
        raise ValueError(f"could not convert string to float: '{feed}'")

    if (celsius < TEMP_MIN) or (celsius > TEMP_MAX):
        raise Exception(f"{celsius} temperature out of range.")

    return celsius

def main() -> None:
    print("Program starting.")
    try:
        c = collectCelsius()
        print(f"You inserted {c}°C")
    except Exception as err:
        print(err)
    print("Program ending.")

if __name__ == "__main__":
    main()
