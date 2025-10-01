print("Program starting.\n")

print("Options:")
print("1 - Celsius to Fahrenheit")
print("2 - Fahrenheit to Celsius")
print("0 - Exit")

choice = int(input("Your choice: "))



if choice == 1:
    cel = float(input("Insert the amount of Celsius: "))
    res1 = (cel * 1.8) +32
    print(f"{round(cel, 1)} °C equals to {round(res1, 1)} °F ")
elif choice == 2:
    fah = float(input("Insert the amount of Fahrenheit: "))
    res2 = (fah -32) /1.8
    print(f"{round(fah, 1)} °F equals to {round(res2, 1)} °C ")

elif choice == 0:
    print("Exiting...")
else:
    print("Unknown option.")

print("\nProgram ending.")
