WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

def readfile():
    rows = []
    filename = input("Insert filename: ")
    print('Reading file "' + filename + '".')
    file = open(filename, "r")
    first_line = file.readline()
    line = file.readline()
    while line != "":
        if line.strip() != "":
            rows.append(line.strip())
        line = file.readline()

    file.close()
    return rows

def analyse(rows):
    print("Analysing timestamps.")
    counts = [0, 0, 0, 0, 0, 0, 0]
    for row in rows:
        for i in range(len(WEEKDAYS)):
            if row.startswith(WEEKDAYS[i]):
                counts[i] = counts[i] + 1
    return counts

def results(counts):
    print("Displaying results.")
    print("### Timestamp analysis ###")
    for i in range(len(WEEKDAYS)):
        print(f'- {WEEKDAYS[i] + ": " + str(counts[i])}')
    print("### Timestamp analysis ###")

def main():
    print("Program starting.")

    rows = readfile()
    counts = analyse(rows)
    results(counts)

    print("Program ending.")

if __name__ == "__main__":
    main()
