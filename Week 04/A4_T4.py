print("Program starting.\n")

wordc = -1
charc = 0



continueLoop = True
while continueLoop == True:
    word = input("Insert word (empty stops): ")
    wordc +=1
    charc +=len(word)
    if word == "":
        break

print("\n You inserted:")
print(f"- {wordc} words")
print(f"- {charc} characters")

print("\nProgram ending.")
