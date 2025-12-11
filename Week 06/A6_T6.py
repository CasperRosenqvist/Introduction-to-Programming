AlphabetsLower = "abcdefghijklmnopqrstuvwxyz"
AlphabetsUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

rows = []

def askRows():
    while True:
        word = input("Insert row(empty stops): ")
        if word == "":
            break
        rows.append(word)
    return rows

resultCiph = []

def cipher(words):
    for row in words:
        cipherRow =""
        for char in row:
            if char in AlphabetsLower:
                index = AlphabetsLower.index(char)
                cipherRow += AlphabetsLower[(index + 13) % 26]
            elif char in AlphabetsUpper:
                index = AlphabetsUpper.index(char)
                cipherRow += AlphabetsUpper[(index + 13) % 26]
            else:
                cipherRow += char
        resultCiph.append(cipherRow)
    return resultCiph




def filesave(ciphWords):
    fname = input("Insert filename to save: ")
    while True:
        if fname == "" :
            print("File name not defined.")
            print("Aborting save operation.")
            break
        else:
            file = open(fname, "w")
            file.write("\n".join(ciphWords))
            file.close()
            print("Ciphered text saved!")
            break


def main():
    print("Program starting.\n")
    print("Collecting plain text rows for ciphering.")
    words = askRows()
    print("")
    print("#### Ciphered text ####")
    ciphWords = cipher(words)
    for line in ciphWords:
        print(line)
    print("#### Ciphered text ####")
    filesave(ciphWords)
    print("Program ending.")

if __name__ == "__main__":
    main()