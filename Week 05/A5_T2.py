def frameWord(word):
    length = len(word) + 4 
    print("*" * length)
    print(f"* {word} *")
    print("*" * length)
    return None

def main():
    print("Program starting.")
    word = input("Insert word: ")
    print("")
    frameWord(word)
    print("\nProgram ending.")
    return None

main()