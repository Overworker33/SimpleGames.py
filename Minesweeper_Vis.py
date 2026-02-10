import pygame
import random
import numpy as np

# Define some colors
BG = (10, 10, 10)
WHITE = (255, 255, 255)
DUG = (175, 175, 175)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
DARK_BLUE = (0, 0, 139)
MAROON = (128, 0, 0)
TEAL = (0, 128, 128)
BLACK = (0, 0, 0)
SILVER = (128, 128, 128)
YELLOW = (255, 255, 0)
PINK = (255, 192, 203)
PURPLE = (128, 0, 128)
Bomb_Found = (225, 0, 0)
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 24
HEIGHT = 24
mines = 15
CELLS = 10
dif = CELLS
vis = False
# This sets the margin between each cell
MARGIN = 5
C = list(range(CELLS))
# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(CELLS+1):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(CELLS+1):
        grid[row].append(0)  # Append a cell
 
# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)
 
# Initialize pygame
pygame.init()
 
# Set the HEIGHT and WIDTH of the screen
S = (WIDTH * CELLS) + (MARGIN * CELLS+1)
WINDOW_SIZE = [S+4, (S+4)+((WIDTH + MARGIN)*2)]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("Minesweeper")
 
# Loop until the user clicks the close button.
done = False
Game = True
Win = False
mines_left = mines
mines_tot = mines
empty_space = 0
mine_dif = mines
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

font = pygame.font.Font(None, 30)
text1 = font.render(' 1',True, BLUE)
text2 = font.render(' 2',True, GREEN)
text3 = font.render(' 3',True, RED)
text4 = font.render(' 4',True, DARK_BLUE)
text5 = font.render(' 5',True, MAROON)
text6 = font.render(' 6',True, TEAL)
text7 = font.render(' 7',True, BLACK)
text8 = font.render(' 8',True, SILVER)
text0 = font.render(' |',True, BLACK)
text = font.render(' ~',True, RED)
digit_images = { '1':text1, '2':text2, '3':text3, '4':text4,
                 '5':text5, '6':text6, '7':text7, '8':text8,  
                 '12':text0, '14':text0}

text_font = pygame.font.SysFont("Arial", 20)
stext_font = pygame.font.SysFont("Arial", 17)
ltext_font = pygame.font.SysFont("Arial", 45, bold = True)
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))

# -------- Main Program Loop -----------
while not done:

    cells = np.zeros(((S+5) // 10, (S+5) // 10))

    for a in range(CELLS):
        for r in range(CELLS):
            for c in range(CELLS):
                if grid[r][c] == 9:
                    for dx, dy in [(-1, -1), (-1, 0), (-1, 1),( 0, -1),( 0, 1),( 1, -1), ( 1, 0), ( 1, 1)]:

                        try:
                            if grid[r+dx][c+dy] == 0:
                                grid[r+dx][c+dy] = 13
                        except IndexError:
                            pass

    for a in range(CELLS):
        for r in range(CELLS):
            for c in range(CELLS):
                if grid[r][c] == 13:
                    count = 0
                    for dx, dy in [(-1, -1), (-1, 0), (-1, 1),( 0, -1),( 0, 1),( 1, -1), ( 1, 0), ( 1, 1)]:

                        try:
                            if grid[r+dx][c+dy] == 10 or grid[r+dx][c+dy] == 14:
                                count += 1
                        except IndexError:
                            pass
                    if count > 0:
                        grid[r][c] = count
                    if count == 0:
                        grid[r][c] = 9

    for event in pygame.event.get():  # User did something

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                vis = False
                Game = True
                done = False
                Win = False
                mines = mine_dif
                CELLS = dif
                mines_left = mines
                mines_tot = mines
                for row in range(CELLS):
                    for column in range(CELLS):
                        grid[row][column] = 0
                S = (WIDTH * CELLS) + (MARGIN * CELLS+1)
                WINDOW_SIZE = [S+4, (S+4)+((WIDTH + MARGIN)*2)]
                screen = pygame.display.set_mode(WINDOW_SIZE)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                vis = False
                Game = True
                done = False
                Win = False
                mines = 12
                CELLS = 10
                mine_dif = mines
                dif = CELLS
                mines_left = mines
                mines_tot = mines
                C = list(range(CELLS))
                grid = []
                for row in range(CELLS+1):
                    grid.append([])
                    for column in range(CELLS+1):
                        grid[row].append(0)
                S = (WIDTH * CELLS) + (MARGIN * CELLS+1)
                WINDOW_SIZE = [S+4, (S+4)+((WIDTH + MARGIN)*2)]
                screen = pygame.display.set_mode(WINDOW_SIZE)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_2:
                vis = False
                Game = True
                done = False
                Win = False
                mines = 30
                CELLS = 15
                mine_dif = mines
                dif = CELLS
                mines_left = mines
                mines_tot = mines
                C = list(range(CELLS))
                grid = []
                for row in range(CELLS+1):
                    grid.append([])
                    for column in range(CELLS+1):
                        grid[row].append(0)
                S = (WIDTH * CELLS) + (MARGIN * CELLS+1)
                WINDOW_SIZE = [S+4, (S+4)+((WIDTH + MARGIN)*2)]
                screen = pygame.display.set_mode(WINDOW_SIZE)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_3:
                vis = False
                Game = True
                done = False
                Win = False
                mines = 72
                CELLS = 20
                mine_dif = mines
                dif = CELLS
                mines_left = mines
                mines_tot = mines
                C = list(range(CELLS))
                grid = []
                for row in range(CELLS+1):
                    grid.append([])
                    for column in range(CELLS+1):
                        grid[row].append(0)
                S = (WIDTH * CELLS) + (MARGIN * CELLS+1)
                WINDOW_SIZE = [S+4, (S+4)+((WIDTH + MARGIN)*2)]
                screen = pygame.display.set_mode(WINDOW_SIZE)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_4:
                vis = False
                Game = True
                done = False
                Win = False
                mines = 100
                CELLS = 25
                mine_dif = mines
                dif = CELLS
                mines_left = mines
                mines_tot = mines
                C = list(range(CELLS))
                grid = []
                for row in range(CELLS+1):
                    grid.append([])
                    for column in range(CELLS+1):
                        grid[row].append(0)
                S = (WIDTH * CELLS) + (MARGIN * CELLS+1)
                WINDOW_SIZE = [S+4, (S+4)+((WIDTH + MARGIN)*2)]
                screen = pygame.display.set_mode(WINDOW_SIZE)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_5:
                vis = False
                Game = True
                done = False
                Win = False
                mines = 172
                CELLS = 30
                mine_dif = mines
                dif = CELLS
                mines_left = mines
                mines_tot = mines
                C = list(range(CELLS))
                grid = []
                for row in range(CELLS+1):
                    grid.append([])
                    for column in range(CELLS+1):
                        grid[row].append(0)
                S = (WIDTH * CELLS) + (MARGIN * CELLS+1)
                WINDOW_SIZE = [S+4, (S+4)+((WIDTH + MARGIN)*2)]
                screen = pygame.display.set_mode(WINDOW_SIZE)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SLASH:
                vis = not vis

        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        if Game == True:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                while mines > 0:
                    x = random.choice(C)
                    y = random.choice(C)
                    try:
                        if grid[x][y] == 0 and not (x == row and y == column):
                            grid[x][y] = 10
                            mines -= 1
                    except IndexError:
                        pass

                if grid[row][column] == 0:
                    count = 0
                    for dx, dy in [(-1, -1), (-1, 0), (-1, 1),( 0, -1),( 0, 1),( 1, -1), ( 1, 0), ( 1, 1)]:

                        try:
                            if grid[row+dx][column+dy] == 10 or grid[row+dx][column+dy] == 14:
                                count += 1
                        except IndexError:
                            pass
                
                #Without constantly checking if it's an unopened cell, a funny bug occurs duping the id... 
                #...of the previus cell to the next ones clicked unless it's an undug cell.
                if grid[row][column] == 0 and count > 0:
                    grid[row][column] = count

                if grid[row][column] == 0 and count == 0:
                    grid[row][column] = 9

                if grid[row][column] == 10:
                    for r in range(CELLS):
                        for c in range(CELLS):
                            if grid[r][c] == 10 or grid[r][c] == 14:
                                grid[r][c] = 11

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pos = pygame.mouse.get_pos()
                    column = pos[0] // (WIDTH + MARGIN)
                    row = pos[1] // (HEIGHT + MARGIN)
                    if grid[row][column] == 0:
                        grid[row][column] = 12
                        mines_left -= 1
                    elif grid[row][column] == 10:
                        grid[row][column] = 14
                        mines_left -= 1
                    elif grid[row][column] == 12:
                        grid[row][column] = 0
                        mines_left += 1
                    elif grid[row][column] == 14:
                        grid[row][column] = 10
                        mines_left += 1
    # Set the screen background
    screen.fill(BG)
 
    # Draw the grid
    for row in range(CELLS):
        for column in range(CELLS):
            color = WHITE

            if grid[row][column] == 12 or grid[row][column] == 14:
                color = WHITE
            if grid[row][column] == 11:
                color = Bomb_Found
                Game = False
            if grid[row][column] == 10 and vis == False:
                color = WHITE
            if grid[row][column] == 10 and vis == True:
                color = GREEN
            if 1 <= grid[row][column] <= 9:
                color = DUG
            if grid[row][column] == 15:
                grid[row][column] = random.randint(16,20)

            if grid[row][column] == 16:
                color = BLUE
            if grid[row][column] == 17:
                color = YELLOW
            if grid[row][column] == 18:
                color = PINK
            if grid[row][column] == 19:
                color = PURPLE
            if grid[row][column] == 20:
                color = GREEN
            pygame.draw.rect(screen,
                            color,
                            [(MARGIN + WIDTH) * column + MARGIN,
                            (MARGIN + HEIGHT) * row + MARGIN,
                            WIDTH,
                            HEIGHT])

            if 1 <= grid[row][column] <= 8:
                grid[row][column] = str(grid[row][column])
                
                if (type(grid[row][column]) is str and grid[row][column] in "12345678"):
                    screen.blit(digit_images[grid[row][column]], [(MARGIN+column*(MARGIN+WIDTH))-1, (MARGIN +row*(MARGIN+HEIGHT))+1,WIDTH,HEIGHT])

                grid[row][column] = int(grid[row][column])

            if grid[row][column] == 12 or grid[row][column] == 14:
                grid[row][column] = str(grid[row][column])
                
                if (type(grid[row][column]) is str and grid[row][column] in "1214"):
                    screen.blit(digit_images[grid[row][column]], [(MARGIN+column*(MARGIN+WIDTH))-1, (MARGIN +row*(MARGIN+HEIGHT))+1,WIDTH,HEIGHT])
                    screen.blit(digit_images[grid[row][column]], [(MARGIN+column*(MARGIN+WIDTH)), (MARGIN +row*(MARGIN+HEIGHT))+1,WIDTH,HEIGHT])
                    screen.blit(text, [(MARGIN+column*(MARGIN+WIDTH))+2, (MARGIN +row*(MARGIN+HEIGHT))-6,WIDTH,HEIGHT])
                    screen.blit(text, [(MARGIN+column*(MARGIN+WIDTH))+2, (MARGIN +row*(MARGIN+HEIGHT))-5,WIDTH,HEIGHT])
                    screen.blit(text, [(MARGIN+column*(MARGIN+WIDTH))+2, (MARGIN +row*(MARGIN+HEIGHT))-4,WIDTH,HEIGHT])
                    screen.blit(text, [(MARGIN+column*(MARGIN+WIDTH))+2, (MARGIN +row*(MARGIN+HEIGHT))-3,WIDTH,HEIGHT])
                    screen.blit(text, [(MARGIN+column*(MARGIN+WIDTH))+2, (MARGIN +row*(MARGIN+HEIGHT))-2,WIDTH,HEIGHT])
                    screen.blit(text, [(MARGIN+column*(MARGIN+WIDTH))+2, (MARGIN +row*(MARGIN+HEIGHT))-1,WIDTH,HEIGHT])

                grid[row][column] = int(grid[row][column])

    if Game == True:
        empty_space = 0
        for r in range(CELLS):
            for c in range(CELLS):
                if grid[r][c] == 0:
                    empty_space += 1
                if grid[r][c] == 10:
                    empty_space += 1
                if grid[r][c] == 12:
                    empty_space += 1
                if grid[r][c] == 14:
                    empty_space += 1
        
        if empty_space == mines_tot:
            Game = False
            Win = True
            
    if Game == True:
        m = str(mines_left)
        draw_text("Controls", text_font, WHITE, 5, (S))
        draw_text("Mines :", text_font, WHITE, (S-95), (S))
        draw_text(m, text_font, WHITE, (S-30), (S))
        draw_text("Mouse : Dig", stext_font, YELLOW, 5, (S)+(WIDTH + MARGIN))
        draw_text("Space : Flag", stext_font, YELLOW, S-97, (S)+(WIDTH + MARGIN))

    if Game == False and Win == False and dif == 10:
        draw_text("Game Over", ltext_font, RED, (S//3)-78, (S))
    if Game == False and Win == False and dif == 15:
        draw_text("Game Over", ltext_font, RED, (S//3)-((WIDTH + MARGIN)*2), (S))
    if Game == False and Win == False and dif == 20:
        draw_text("Game Over", ltext_font, RED, (S//3)-((WIDTH + MARGIN)*2)+12, (S))
    if Game == False and Win == False and dif == 25:
        draw_text("Game Over", ltext_font, RED, (S//3)-((WIDTH + MARGIN)*2)+36, (S))
    if Game == False and Win == False and dif == 30:
        draw_text("Game Over", ltext_font, RED, (S//3)-((WIDTH + MARGIN)*2)+55, (S))

    if Game == False and Win == True:
        if dif == 10:
            draw_text("You Win", ltext_font, GREEN, (S//3)-45, (S))
        if dif == 15:
            draw_text("You Win", ltext_font, GREEN, (S//3)-25, (S))
        if dif == 20:
            draw_text("You Win", ltext_font, GREEN, (S//3)-5, (S))
        if dif == 25:
            draw_text("You Win", ltext_font, GREEN, (S//3)+15, (S))
        if dif == 30:
            draw_text("You Win", ltext_font, GREEN, (S//3)+40, (S))

        for row in range(CELLS):
            for column in range(CELLS):
                if grid[row][column] == 10 or grid[row][column] == 14:
                    grid[row][column] = 15

    # Limit to 15 frames per second
    clock.tick(15)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()