
import random
random.seed(1234)

def layMines(PMineField, PMines):
    rows = len(PMineField)
    cols = len(PMineField[0]) if rows > 0 else 0
    positions = []
    i = 0
    while i < rows:
        j = 0
        while j < cols:
            positions.append((i, j))
            j += 1
        i += 1
    random.shuffle(positions)
    count = PMines
    if count > len(positions):
        count = len(positions)
    k = 0
    while k < count:
        r, c = positions[k]
        PMineField[r][c] = 9
        k += 1
    return None

def calculateNearbys(PMineField):
    rows = len(PMineField)
    cols = len(PMineField[0]) if rows > 0 else 0
    i = 0
    while i < rows:
        j = 0
        while j < cols:
            if PMineField[i][j] != 9:
                cnt = 0
                di = -1
                while di <= 1:
                    dj = -1
                    while dj <= 1:
                        if not (di == 0 and dj == 0):
                            ni = i + di
                            nj = j + dj
                            if 0 <= ni < rows and 0 <= nj < cols:
                                if PMineField[ni][nj] == 9:
                                    cnt += 1
                        dj += 1
                    di += 1
                PMineField[i][j] = cnt
            j += 1
        i += 1
    return None

def generateMinefield(PMineField, PRows, PCols, PMines):
    PMineField.clear()
    i = 0
    while i < PRows:
        PMineField.append([])
        j = 0
        while j < PCols:
            PMineField[i].append(0)
            j += 1
        i += 1
    layMines(PMineField, PMines)
    calculateNearbys(PMineField)
    return None

def main():
    MineField = []
    while True:
        print("Options:")
        print("1 - Generate minesweeper board")
        print("2 - Show generated board")
        print("3 - Save board")
        print("0 - Exit")
        choice = input("Your choice: ")
        if choice == "1":
            rows = int(input("Rows: "))
            cols = int(input("Cols: "))
            mines = int(input("Mines: "))
            generateMinefield(MineField, rows, cols, mines)
        elif choice == "2":
            r = 0
            while r < len(MineField):
                row_values = ""
                c = 0
                while c < len(MineField[r]):
                    if c == 0:
                        row_values = str(MineField[r][c])
                    else:
                        row_values = row_values + "," + str(MineField[r][c])
                    c += 1
                print(row_values)
                r += 1
        elif choice == "3":
            filename = input("Insert filename: ")
            with open(filename, "w") as f:
                r = 0
                while r < len(MineField):
                    row_values = ""
                    c = 0
                    while c < len(MineField[r]):
                        if c == 0:
                            row_values = str(MineField[r][c])
                        else:
                            row_values = row_values + "," + str(MineField[r][c])
                        c += 1
                    f.write(row_values + "\n")
                    r += 1
        elif choice == "0":
            break

if __name__ == "__main__":
    main()