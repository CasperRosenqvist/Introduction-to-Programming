print("Program starting.")
print("Insert two integers.")

int1 = int(input("Insert first integer: "))
int2 = int(input("Insert second integer: "))

print("Comparing inserted integers")

if int1 > int2:
    print("First integer is greater.")
elif int2 > int1:
    print("Second integer is greater.")
elif int1 == int2:
    print("Integers are the same")

result = int1 + int2

print(f"\nAdding integers together")
print(f"{int1}+{int2}={result}")

print(f"\nChecking the parity of the sum...")
parity = result % 2

if parity == 0:
    print("Sum is even.")
else:
    print("Sum is odd.")

print("Program ending.")