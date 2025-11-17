DELIMITER = ";"

def readfile():
    filename = input("Insert filename: ")
    print(f'Reading file "{filename}".')
    timestamps = []
    file = open(filename, "r")
    header = file.readline()
    for line in file:
        line = line.strip()
        if line:
            columns = line.split(DELIMITER)
            weekday, hour, consumption, price = columns
            timestamps.append([weekday, hour, float(consumption), float(price)])
    file.close()
    return timestamps

def analyse(timestamps):
    print("Electricity usage:")
    for ts in timestamps:
        weekday, hour, consumption, price = ts
        total = consumption * price
        print(f"--{weekday} {hour}, price: {price} €, "
              f"consumption: {consumption} kWh, total: {total:.2f} €")

def main():
    print("Program starting.")
    timestamps = readfile()
    analyse(timestamps)
    print("Program ending.")

main()