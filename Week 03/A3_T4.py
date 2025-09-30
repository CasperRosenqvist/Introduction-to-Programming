print("Program starting.")
print("This is a program with simple menu, where you can choose which operation the program performs.")

Name = input("Before the menu, please insert your name: ")

print("\nOptions: ")
print("1 - Print welcome message")
print("2 - Print the name backwards")
print("3 - Print the first character")
print("4 - Show the amount of characters in the name")
print("0 - Exit")

choice = int(input("Your choice: "))

backw = Name[::-1]
first = Name[0]
length = len(Name)

if choice == 1:
    print(f"Welcome {Name}!")
elif choice == 2:
    print(f"Your name backwards is \"{backw}\"")
elif choice == 3:
    print(f"The first character in name \"{Name}\" is \"{first}\"")
elif choice == 4:
    print(f"There are {length} characters in the name \"{Name}\"")
elif choice == 0:
    print(f"Exiting...")
else:
    print("Unknown option.")

print("\nProgram ending.")