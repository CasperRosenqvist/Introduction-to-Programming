def main():
    print("Program starting.")
    print("This program can read a file.")
    filename = input("Insert a file name: ")
    file = open(filename, 'r')
    print(f'#### START "{filename}" ####')
    content = file.read()
    print(content)
    print(f'#### END "{filename}" ####')
    file.close()
    print("Program ending.")

if __name__ == "__main__":
    main()