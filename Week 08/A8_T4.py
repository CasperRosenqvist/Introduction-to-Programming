
from datetime import datetime

months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

formats = [
    "%Y-%m-%d %H:%M:%S",
    "%Y-%m-%d %H:%M",
    "%Y-%m-%d",
    "%Y/%m/%d %H:%M:%S",
    "%Y/%m/%d %H:%M",
    "%Y/%m/%d",
    "%d.%m.%Y %H:%M:%S",
    "%d.%m.%Y %H:%M",
    "%d.%m.%Y",
    "%Y-%m-%dT%H:%M:%S",
    "%Y-%m-%dT%H:%M"
]

def parse_date(text):
    for f in formats:
        try:
            return datetime.strptime(text.strip(), f)
        except:
            pass
    return None

def load_file(filename):
    timestamps = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if line == "":
                continue
            dt = parse_date(line)
            if dt:
                timestamps.append(dt)
    return timestamps

def count_year(year, timestamps):
    count = 0
    for t in timestamps:
        if t.year == int(year):
            count += 1
    return count

def count_month(month, timestamps):
    mnum = None
    if month.isdigit():
        mnum = int(month)
    else:
        for i in range(len(months)):
            if month.lower() == months[i].lower() or month.lower() == months[i][:3].lower():
                mnum = i + 1
    if mnum is None:
        return 0
    count = 0
    for t in timestamps:
        if t.month == mnum:
            count += 1
    return count

def count_weekday(day, timestamps):
    wnum = None
    if day.isdigit():
        num = int(day)
        if 1 <= num <= 7:
            wnum = num - 1
    else:
        for i in range(len(weekdays)):
            if day.lower() == weekdays[i].lower() or day.lower() == weekdays[i][:3].lower():
                wnum = i
    if wnum is None:
        return 0
    count = 0
    for t in timestamps:
        if t.weekday() == wnum:
            count += 1
    return count

def showOptions():
    print("Options:")
    print("1:--Calculate amount of timestamps during year")
    print("2:--Calculate amount of timestamps during month")
    print("3:--Calculate amount of timestamps during weekday")
    print("0:--Exit")

def main():
    print("Program starting.")
    filename = input("Insert: filename: ")
    timestamps = load_file(filename)

    while True:
        showOptions()
        choice = input("Your choice: ")
        if choice == "1":
            year = input("Insert: year: ")
            result = count_year(year, timestamps)
            print(f"Amount of timestamps during year: '{year}' : {result}")
            print()
        elif choice == "2":
            month = input("Insert: month: ")
            result = count_month(month, timestamps)
            print(f"Amount of timestamps during month: '{month}' : {result}")
            print()
        elif choice == "3":
            day = input("Insert: weekday: ")
            result = count_weekday(day, timestamps)
            print(f"Amount of timestamps during weekday: '{day}' : {result}")
            print()
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")
            print()

    print("Program ending.")

if __name__ == "__main__":
    main()
