def main():
    print("Program starting.")
    fname = input("Insert first name: ")
    lname = input("Insert last name: ")
    filename = input("Insert file name: ")
    nfile = open(filename, "w")
    nfile.write(f"{fname}\n")
    nfile.write(f"{lname}\n")
    nfile.close()
    print("Program ending.")

if __name__ == "__main__":
    main()