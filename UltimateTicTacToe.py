import os

def board_vis(b):
    print(f"\n | {b[0][0]} {b[0][1]} {b[0][2]} | | {b[1][0]} {b[1][1]} {b[1][2]} | | {b[2][0]} {b[2][1]} {b[2][2]} |\n",
          f"| {b[0][3]} {b[0][4]} {b[0][5]} | | {b[1][3]} {b[1][4]} {b[1][5]} | | {b[2][3]} {b[2][4]} {b[2][5]} |\n",
          f"| {b[0][6]} {b[0][7]} {b[0][8]} | | {b[1][6]} {b[1][7]} {b[1][8]} | | {b[2][6]} {b[2][7]} {b[2][8]} |\n\n",
          f"| {b[3][0]} {b[3][1]} {b[3][2]} | | {b[4][0]} {b[4][1]} {b[4][2]} | | {b[5][0]} {b[5][1]} {b[5][2]} |\n",
          f"| {b[3][3]} {b[3][4]} {b[3][5]} | | {b[4][3]} {b[4][4]} {b[4][5]} | | {b[5][3]} {b[5][4]} {b[5][5]} |\n",
          f"| {b[3][6]} {b[3][7]} {b[3][8]} | | {b[4][6]} {b[4][7]} {b[4][8]} | | {b[5][6]} {b[5][7]} {b[5][8]} |\n\n",
          f"| {b[6][0]} {b[6][1]} {b[6][2]} | | {b[7][0]} {b[7][1]} {b[7][2]} | | {b[8][0]} {b[8][1]} {b[8][2]} |\n",
          f"| {b[6][3]} {b[6][4]} {b[6][5]} | | {b[7][3]} {b[7][4]} {b[7][5]} | | {b[8][3]} {b[8][4]} {b[8][5]} |\n",
          f"| {b[6][6]} {b[6][7]} {b[6][8]} | | {b[7][6]} {b[7][7]} {b[7][8]} | | {b[8][6]} {b[8][7]} {b[8][8]} |\n")

def pick_spot(b,n):
    print(f"        Current Board {n+1}")
    print(f"     | {b[n][0]} {b[n][1]} {b[n][2]} |   | 1 2 3 |\n",
          f"    | {b[n][3]} {b[n][4]} {b[n][5]} |   | 4 5 6 |\n",
          f"    | {b[n][6]} {b[n][7]} {b[n][8]} |   | 7 8 9 |\n",)

def check_small_win(b,n):
    wins = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    for line in wins:
        if all(b[n][i] == player for i in line): 
            return True
    return False

def check_large_win(b):
    wins = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    for line in wins:
        if all(b[i] == player for i in line): 
            return True
    return False

temp_board_data = []
entire_board_data = []
for i in range(9):
    temp_board_data.append([])
    entire_board_data.append(str(i+1))
    for j in range(9):
        temp_board_data[i].append(str(j+1))
board_data = temp_board_data
elem_spots = []
Game = True
turn = 0
player = "X"
playing_on = None
print("\n | 1 2 3 |\n | 4 5 6 |\n | 7 8 9 |\n")

while Game:
    while turn == 0:
        try:
            spot = input("Where would you like to start?[1-9]: ")
            spot = int(spot)-1
            turn += 1
        except TypeError:
            print("Please pick a number 1 through 9.")
    if turn % 2 == 0:
        player = "O"
    else:
        player = "X"
    os.system("cls")
    if spot == -1:
        print(f"{player}'s Turn...          Turn #{turn}")
        board_vis(board_data)
        while spot == -1:
            try:
                spot = input("Where would you like to start?[1-9]: ")
                spot = int(spot)-1
                if spot not in elem_spots:
                    os.system("cls")
                else:
                    print("Please pick an available square.")
            except TypeError:
                print("Please pick a number 1 through 9.")
    print(f"{player}'s Turn...          Turn #{turn}")
    board_vis(board_data)
    pick_spot(board_data, spot)
    mini_loop = True
    while mini_loop == True:
        try:
            pick = input("Where would you like to place?[1-9]: ")
            pick = int(pick)-1
            board_data[spot][pick] = player
            prev_spot = spot
            spot = pick
            turn += 1
            mini_loop = False
            if spot not in elem_spots:
                pass
            else:
                spot = -1
        except TypeError:
            print("Please pick a number 1 through 9.")
    sw = check_small_win(board_data, prev_spot)
    if sw == True:
        elem_spots.append(prev_spot)
        entire_board_data[prev_spot] = player
        for j in range(9):
            if j != 4:
                board_data[prev_spot][j] = " "
            else:
                board_data[prev_spot][j] = player
    lw = check_large_win(entire_board_data)
    if lw == True:
        Game = False
        os.system("cls")
        print(f"{player} Wins!          Turn #{turn}")
        board_vis(board_data)
        print("Thank you for playing...\n")
