# Program starting.
# Insert a hex color: #FFA500

#Colors
#- Red FF
#- Green A5
#- Blue 00

#Program ending.

print("Program starting.\n")
Color = input("Insert a hex color: ")

Red = Color[1:3]
Green = Color[3:5]
Blue = Color[5:7]


print("\nColors")
print(f"- Red {Red}")
print(f"- Green {Green}")
print(f"- Blue {Blue}")

print("\nProgram ending.")