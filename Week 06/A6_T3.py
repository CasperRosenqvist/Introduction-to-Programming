def main():
    print("Program starting.")
    print("This program can copy a file.")
    sfile = input("Insert source filename: ")
    dfile = input("Insert destination filename: ")
    print(f"Reading file '{sfile}' content.")
    file1 = open(sfile, "r")
    content = file1.read()
    file1.close()
    print("File content ready in memory")
    print(f"Writing content into file '{dfile}'")
    file2 = open(dfile, "w")
    file2.write(content)
    print("Copying operation complete.")
    file2.close()
    print("Program ending.")
          

if __name__ == "__main__":
    main()