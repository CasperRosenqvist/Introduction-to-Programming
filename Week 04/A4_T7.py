
print("Program starting.\n")
print("Check multiplicative persistence.")


number = input("Insert an integer: ")

steps = 0  

while len(number) > 1:
    digits = [int(d) for d in number] 
    result = 1
    print(" * ".join(number), end=" = ")
    for digit in digits:
        result *= digit
    print(result)
    number = str(result) 
    steps += 1

print("No more steps.\n")
print(f"This program took {steps} step(s)\n")
print("Program ending.")
