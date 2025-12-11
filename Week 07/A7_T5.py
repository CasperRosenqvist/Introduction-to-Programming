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
    print("Analysing timestamps.")
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    daily_usage = {day: 0.0 for day in weekdays}
    daily_cost = {day: 0.0 for day in weekdays}
    for ts in timestamps:
        weekday, hour, consumption, price = ts
        daily_usage[weekday] += consumption
        daily_cost[weekday] += consumption * price
    print("Displaying results.")
    print("###Electricity consumption summary.###")
    for day in weekdays:
        print(f"--{day}-usage: {daily_usage[day]:.2f} kWh, cost: {daily_cost[day]:.2f} €")
    print("###Electricity consumption summary.###")

def main():
    print("Program starting.")
    timestamps = readfile()
    analyse(timestamps)
    print("Program ending.")

if __name__ == "__main__":
    main()
