print("Program starting\n")

start = int(input("Insert staring point: "))
stop = int(input("Insert stopping point: "))
inspect = int(input("Insert inspection point: "))

run = True
print("")

if start >= stop:
    print("Starting point value must be less than the stopping point value.")
    run = False
if inspect < start or inspect > stop:
    print("Inspection value must be within the range of start and stop.")
    run = False
if run == False:
    print("\nProgram ending.")

if run == True:
    print("First loop - inspection with break:")
    for i in range(start, stop):
        if i == inspect:
            break
        else:
            print(i, end = " ")
    print("")
    print("Second loop - inspection with continue:")
    for i in range(start, stop):
        if i == inspect:
            continue
        else:
            print(i, end = " ")
    print("\nProgram ending.")