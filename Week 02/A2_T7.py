#Program starting.
print("Program starting.")

#Insert fahrenheits: 50
Fah = float(input("Insert fahrenheits: "))
Celc = (Fah - 32) / 1.8
Celc = round(Celc, 1)

#50.0°F is 10.0°C
print(f"{Fah}°F is {Celc}°C")

#Program ending.
print("Program ending.")
