#Program starting.

#Insert a closed compound word: Moonbanana
#The word you inserted is 'Moonbanana' and in reverse it is 'ananabnooM'.
#The inserted word length is 10
#Last character is 'a'

#Take substring from the inserted word by inserting...
#1) Starting point: 0
#2) Ending point: 4
#3) Step size: 1

#The word 'Moonbanana' sliced to the defined substring is 'Moon'.
#Program ending.

print("Program starting. \n")

Compound = input("Insert a closed compound word: ")
print(f"The word you inserted is '{Compound}' and in reverse it is '{Compound [::-1]}'.")
print(f"The inserted word length is {len(Compound)}")
print(f"Last character is '{Compound [-1]}'\n")

print("Take substring from the inserted word by inserting...")
Starting_point = int(input("1) Starting point: "))
Ending_point = int(input("2) Ending point: "))
Step_size = int(input("3) Step size: "))

Substring = Compound[Starting_point:Ending_point:Step_size] 
print(f"\n The word '{Compound}' sliced to defined substring is '{Substring}'")
print("Program ending.")
