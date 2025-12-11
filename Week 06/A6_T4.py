def main():
    print("Program staring.")
    print("This program analyses a list of names from a file.")
    fname = input("Insert filename read: ")
    print(f'Reading names from "{fname}"')
    file = open(fname, "r")
    content = file.read()
    print("Analysing names...")

    names = [name.strip() for name in content.replace("\n", ";").split(";") if name.strip()]

    count = len(names)
    shortest = len(min(names, key=len))
    longest = len(max(names, key=len))
    average = (sum(len(name) for name in names) / count)


    print("Analysis complete!")
    print("### REPORT BEGIN ###")
    print(f"Name count - {count}")
    print(f"Shortest name - {shortest} chars")
    print(f"Longest name - {longest} chars")
    print(f"Average name - {average:.2f} chars")
    print("### REPORT END ###")
    file.close()
    print("Program ending.")

if __name__ == "__main__":
    main()