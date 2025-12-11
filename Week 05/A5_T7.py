DELIMITER = ","

def collectWords():
    words = []
    while True:
        word = input("Insert word(empty stops): ")
        if word == "":
            break
        words.append(word)
    return DELIMITER.join(words)


def analyseWords(words_string):
    words_list = words_string.split(DELIMITER)
    numWords = len(words_list)
    chars = sum(len(word) for word in words_list)
    Avg = chars / numWords if numWords > 0 else 0
    print(f"- {numWords}-words")
    print(f"- {chars}-characters")
    print("- {:.2f}-Average-word-length".format(Avg))


def main():
    print("Program starting.")
    words_string = collectWords()
    analyseWords(words_string)
    print("Program ending.")

main()