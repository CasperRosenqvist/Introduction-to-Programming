
print("Program starting.")
integer = int(input("Insert a positive integer: "))
rounds = 0

while integer != 1:
    print(f"{integer} ->", end=" ")
    if integer % 2 == 0:
        integer = integer // 2
    else:
        integer = (integer * 3) + 1
    rounds += 1
print("1")

print(f"Sequence had {rounds} total steps.")
print("\nProgram ending.")