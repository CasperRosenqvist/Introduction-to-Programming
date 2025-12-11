AlphabetsLower = "abcdefghijklmnopqrstuvwxyz"
AlphabetsUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DELIMETER = ";"


def readfile(Pfilename) -> str:
    content = ""
    fileHandle = open(Pfilename, "r")
    row = fileHandle.readline()
    while row != '':
        content += row
        row = fileHandle.readline()
    fileHandle.close()
    return content

def writeFile() -> None:
    return None

def appendFile() -> None:
    return None


def getLocation(locationId):
    location = 'unknown'
    if locationId == 1:
        location = "Galba's palace"
    elif locationId == 2:
        location = "Otho's palace"
    elif locationId == 3:
        location = "Vitelius palace"
    elif locationId == 4:
        location = "Vespasian's palace"
    elif locationId == 0:
        location = "Home"
    return location

def shiftCharacter(Character: str, Alphabets: str, Shift: int = 13) -> str:
    NewCharacter = Character
    for i in range(len(Alphabets)):
        if (Character == Alphabets[i]):  
            ShiftedIndex = i + Shift 
            if ShiftedIndex >= len(Alphabets): 
                ShiftedIndex = ShiftedIndex - len(Alphabets)
            NewCharacter = Alphabets[ShiftedIndex]
    return NewCharacter

def rot(PContent: str, PShift: int = 13) -> str:
    NewContent = ""
    for Character in PContent:
        if (Character in AlphabetsLower):
            NewContent += shiftCharacter(Character, AlphabetsLower, PShift)
        elif (Character in AlphabetsUpper):  
            NewContent += shiftCharacter(Character, AlphabetsUpper, PShift)
        else:
            NewContent += Character 
    return NewContent


def main() -> None:
    print("Travel starting.")
    PlayerProgressFname = "player_progress.txt"
    progress = readfile(PlayerProgressFname)
    lastProgress= progress.strip().split('\n')[-1].split(DELIMETER)
    currentLocationId = int(lastProgress[0])
    currentLocation = getLocation(currentLocationId)
    nextLocationId = int(lastProgress[1])
    nextLocation = getLocation(nextLocationId)
    passPhrase = lastProgress[2]
    print(f"Currently at {currentLocation}.")
    print(f"Travelling to {nextLocation}...")
    print(f"...Arriving to {nextLocation}.")
    print("Passing the guard at the entrance.")
    PlainPassPhrase = rot(lastProgress[2])
    print(f'"{PlainPassPhrase}!"')
    print("Looking for message in the palace...")
    print("Ah, there it is! Seems cryptic.")
    print("[Game] Progress autosaved!")
    appendFile(PlayerProgressFname, (f"\n{nextLocationId}{DELIMETER}{currentLocationId}{DELIMETER}{rot(passPhrase)}"))
    print("Deciphering Emperor's message...")
    print("Looks like I've got now the plain version copy of the Emperor's message.")
    print("Time to leave...")
    print("Travel ending.")
    return None

if __name__ == "__main__":
    main()
