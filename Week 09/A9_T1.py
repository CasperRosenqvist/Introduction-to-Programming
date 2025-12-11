
def main() -> None:
    Sum = 0
    Value = -1
    print("Program starting.")

    while Value != 0:
        feed = input("Insert a number, 0 to stop: ")
        try:
            Value = float(feed)
            Sum += Value
        except Exception:
            print(f"Error! {feed} couldn't be converted to float")

    print(f"Final sum is {Sum}")
    print("Program ending.")
    return None


main()
