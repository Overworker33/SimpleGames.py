import random
print("Welcome To Aiden's Minesweeper Game!\n")
fact = [1,2,3]
neatfact = random.choice(fact)
print("Neat Fact:")
if neatfact == 1: print("This game was written in under 200 lines of Python code! Or 197 lines to be exact!\n")
elif neatfact == 2: print("This project took several days to complete.\n")
elif neatfact == 3: print("These neat facts are using shorthand if's and else's to keep the number of lines down, but the rest of the minesweeper code doesn't.\n")
while True:
    print("Please input your desired length, hight, and mine count.\n")
    height = input("Length Size (Max = 20)(Min = 5): ")
    length = input("Height Size (Max = 20)(Min = 5): ")
    if length == "":
        length = "5"
    if height == "":
        height = "5"
    l = int(length)
    h = int(height)
    a = h * l
    b = l + h
    c = a - b
    C = str(c)
    print("How Many Mines (Max =",C+")(Min = 3)")
    mine = input("Mines: ")
    if mine == "":
        mine = 5
    mines = int(mine)
    if l <= 20 and h <= 20:
        if l >= 5 and h >= 5:
            if mines >= 3 and mines <= c:
                print("--- Bottom Row Numbers After 9 Add 10 To Them Before Choosing! ---")
                break
            else:
                print("\n-----------------------------------\n")
                print("That Mine Count Is Invalid...")
                print("\n-----------------------------------\n")
        else:
            print("\n-----------------------------------\n")
            print("Those Sizes Are Invalid...")
            print("Pick A Number Between 5 And 20...")
            print("\n-----------------------------------\n")
    else:
        print("\n-----------------------------------\n")
        print("Those Sizes Are Invalid...")
        print("Pick A Number Between 5 And 20...")
        print("\n-----------------------------------\n")
grid = []
for x in range(l+2):
    grid.append([])
    for y in range(1, h+3):
        grid[x].append(y)
for x in range(0, l+2):
    for y in range(0, h+2):
        grid[x][y] = "0"    
v = []
for x in range(l+2):
    v.append([])
    for y in range(1, h+3):
        v[x].append(y)
for x in range(0, l+2):
    for y in range(0, h+2):
        v[x][y] = "-"   
vmc = mines
rmc = mines
H = list(range(1, l+1))
L = list(range(1, h+1))
def board():
    for x in reversed(range(1, l+1)):
        if x < 10:
            print(x,"",*v[x][1:h+1],)
        elif x >= 10:
            print(x,*v[x][1:h+1],)
    a = []
    for i in range(1, h+1):
        if i >= 10 and i < 20:
            i -= 10
        if i >= 20 and i < 30:
            i -= 20
        a.append(i)
    print("  ",*a)
while True:
    if rmc == 0:
        print("\n-------------------------------------\n")
        print("You Win!\n")
        board()
        break
    for a in range(l * h):
        for y in range(1, l+1):
            for x in range(1, h+1):
                if v[y][x] == "0":
                    v[y+1][x+1] = grid[y+1][x+1]
                    v[y+1][x] = grid[y+1][x]
                    v[y+1][x-1] = grid[y+1][x-1]
                    v[y-1][x+1] = grid[y-1][x+1]
                    v[y-1][x] = grid[y-1][x]
                    v[y-1][x-1] = grid[y-1][x-1]
                    v[y][x+1] = grid[y][x+1]
                    v[y][x-1] = grid[y][x-1]
    print("Mine Count:",vmc)
    board()
    dof = input("Edit A Flag[1] Or Dig[0]?: ")
    if dof == "1":
        print("Place Or Remove A Flag At The Coordinates...")
        X = input("X: ")
        Y = input("Y: ")
        if X == "":
            X = "0"
        if Y == "":
            Y = "0"
        x = int(X)
        y = int(Y)
        if x > h:
            x = 0
        if y > l:
            y = 0
        if v[y][x] == "-" and x != 0 and y != 0:
            v[y][x] = "F"
            vmc -= 1
            if grid[y][x] == "X":
                rmc -= 1
        elif v[y][x] == "F" and x != 0 and y != 0:
            v[y][x] = "-"
            vmc += 1
            if grid[y][x] == "X":
                rmc += 1
    elif dof != "1":
        print("Dig At The Coordinates...")
        X = input("X: ")
        Y = input("Y: ")
        if X == "":
            X = "0"
        if Y == "":
            Y = "0"
        x1 = int(X)
        y1 = int(Y)
        if x1 > h:
            x1 = 0
        if y1 > l:
            y1 = 0
        while mines > 0:
            X = random.choice(L)
            Y = random.choice(H)
            if grid[Y][X] == "0":
                if Y != y1 or X != x1:
                    grid[Y][X] = "X"
                    mines -= 1
        if mines == 0:
            for a in range(1, l * h):
                for x in range(1, l+1):
                    for y in range(1, h+1):
                        count = 0
                        if grid[x][y] != "X":
                            if grid[x+1][y+1] == "X":
                                count += 1
                            if grid[x+1][y] == "X":
                                count += 1
                            if grid[x+1][y-1] == "X":
                                count += 1
                            if grid[x][y+1] == "X":
                                count += 1
                            if grid[x][y-1] == "X":
                                count += 1
                            if grid[x-1][y+1] == "X":
                                count += 1
                            if grid[x-1][y] == "X":
                                count += 1
                            if grid[x-1][y-1] == "X":
                                count += 1
                            if count == 1:
                                grid[x][y] = "1"
                            elif count == 2:
                                grid[x][y] = "2"
                            elif count == 3:
                                grid[x][y] = "3"
                            elif count == 4:
                                grid[x][y] = "4"
                            elif count == 5:
                                grid[x][y] = "5"
                            elif count == 6:
                                grid[x][y] = "6"
                            elif count == 7:
                                grid[x][y] = "7"
                            elif count == 8:
                                grid[x][y] = "8"
        if grid[y1][x1] == "X" and v[y1][x1] != "F":
            v[y1][x1] = "X"
            for a in range(l * h):
                for x in range(1, l+1):
                    for y in range(1, h+1):
                        if grid[x][y] == "X":
                            v[x][y] = grid[x][y]
            print("\n-------------------------------------\n")
            print("Game Over!\n")
            board()
            break
        if grid[y1][x1] != "X" and v[y1][x1] != "F": 
            v[y1][x1] = grid[y1][x1]

