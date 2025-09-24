

#Program starting.
print("Program starting.")

#Estimate how many minutes you spent on programming...
print("Estimate how many minutes you spent on programming... \n")

#A1_T1: 3
Task_1 = float(input("A1_T1: "))
Task_2 = float(input("A1_T2: "))
Task_3 = float(input("A1_T3: "))
Task_4 = float(input("A1_T4: "))
Task_5 = float(input("A1_T5: "))
Task_6 = float(input("A1_T6: "))
Task_7 = float(input("A1_T7: "))
#A1_T2: 7
#A1_T3: 9
#A1_T4: 8
#A1_T5: 13
#A1_T6: 14
#A1_T7: 21


#In total you spent 75 minutes on programming.#
Total = Task_1 + Task_2 + Task_3 + Task_4 + Task_5 + Task_6 + Task_7
print(f"\nIn total you have spent {round(Total)} minutes on programming.")

# Average per task was 10.71 min and same rounded to the nearest integer 11 min.
Average = Total / 7
print(f"Average per task was {round(Average, 2)} min and same rounded to the nearest integer {round(Average)} min.")

#Program ending.
print("\nProgram ending.")

