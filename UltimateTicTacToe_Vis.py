import pygame
pygame.init()

# Colors
BG = (250, 250, 250)
Black = (0, 0, 0)
Red = (255, 0, 0)
Blue = (0, 0, 255)
Gray = (200, 200, 200)
Green = (0, 200, 0)

# Screen setup
Width = 720
Height = 720
Margin = 60
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Ultimate Tic Tac Toe")

# Fonts
large_font = pygame.font.SysFont("Arial", 60)
small_font = pygame.font.SysFont("Arial", 30)
text_font = pygame.font.SysFont("Arial", 40)
win_font = pygame.font.SysFont("Arial", 50)

clock = pygame.time.Clock()

# Game variables
board_data = [[str(j+1) for j in range(9)] for i in range(9)]  # 9 small boards
entire_board_data = [str(i+1) for i in range(9)]  # Large board status
elem_spots = []  # Completed boards
player = "X"
turn = 0
spot = -1  # Which board we're playing on (-1 means any)
Game = True
game_over = False
winner = None
needs_redraw = True

# Grid calculations
big_cell_size = (Width - 2*Margin) // 3
small_cell_size = big_cell_size // 3
line_width = 4
thick_line_width = 8

def reset_game():
    #Reset all game variables to start a new game
    global board_data, entire_board_data, elem_spots, player, turn, spot, Game, game_over, winner, needs_redraw
    board_data = [[str(j+1) for j in range(9)] for i in range(9)]
    entire_board_data = [str(i+1) for i in range(9)]
    elem_spots = []
    player = "X"
    turn = 0
    spot = -1
    Game = True
    game_over = False
    winner = None
    needs_redraw = True

def draw_text_centered(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    rect = img.get_rect(center=(x, y))
    screen.blit(img, rect)

def check_small_win(b, n):
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

def check_tie():
    #Check if the game is a tie (all 9 boards are complete)
    return len(elem_spots) == 9

def get_big_board_pos(index):
    #Get the top-left corner of a big board cell
    row = index // 3
    col = index % 3
    x = Margin + col * big_cell_size
    y = Margin + row * big_cell_size
    return (x, y)

def get_small_cell_center(big_index, small_index):
    #Get center of a small cell within a big board
    big_x, big_y = get_big_board_pos(big_index)
    small_row = small_index // 3
    small_col = small_index % 3
    
    x = big_x + small_col * small_cell_size + small_cell_size // 2
    y = big_y + small_row * small_cell_size + small_cell_size // 2
    return (x, y)

def draw_board():
    #Draw the entire Ultimate Tic-Tac-Toe board
    screen.fill(BG)
    
    # Draw turn info or game over message
    if game_over:
        if winner:
            game_text = f"Player {winner} Wins!"
            text_color = Green
        else:
            game_text = "It's a Tie!"
            text_color = Blue
        draw_text_centered(game_text, win_font, text_color, Width // 2, 30)
        draw_text_centered("Press 'R' to Reset", text_font, Black, Width // 2, Height - 30)
    else:
        turn_text = f"{player}'s Turn - Turn #{turn+1}"
        draw_text_centered(turn_text, text_font, Black, Width // 2, 30)
    
    # Draw the 9 big boards
    for big_idx in range(9):
        big_x, big_y = get_big_board_pos(big_idx)
        
        # Draw small grid lines within each big board
        for row in range(3):
            for col in range(3):
                x = big_x + col * small_cell_size
                y = big_y + row * small_cell_size
                pygame.draw.rect(screen, Gray, [x, y, small_cell_size, small_cell_size], 1)
        
        # Draw X's and O's or board number in small cells
        if big_idx in elem_spots:
            # Board is won - draw large winner symbol
            center_x = big_x + big_cell_size // 2
            center_y = big_y + big_cell_size // 2
            draw_text_centered(entire_board_data[big_idx], large_font, Red, center_x, center_y)
        else:
            # Draw individual cells
            for small_idx in range(9):
                cell_value = board_data[big_idx][small_idx]
                center_x, center_y = get_small_cell_center(big_idx, small_idx)
                
                if cell_value in ["X", "O"]:
                    draw_text_centered(cell_value, small_font, Black, center_x, center_y)
    
    # Draw thick lines separating the 9 big boards
    for i in range(1, 3):
        # Vertical lines - adjusted to not extend beyond the board
        x = Margin + i * big_cell_size
        pygame.draw.line(screen, Black, (x, Margin + thick_line_width//2), (x, Height - Margin - thick_line_width//2), thick_line_width)
        # Horizontal lines - adjusted to not extend beyond the board
        y = Margin + i * big_cell_size
        pygame.draw.line(screen, Black, (Margin + thick_line_width//2, y), (Width - Margin - thick_line_width//2, y), thick_line_width)
    
    # Outer border
    pygame.draw.rect(screen, Black, [Margin, Margin, Width - 2*Margin, Height - 2*Margin], thick_line_width)
    
    # Draw highlight borders LAST so they appear on top (only if game not over) 
    if not game_over:
        for big_idx in range(9):
            big_x, big_y = get_big_board_pos(big_idx)
            big_x += 1
            big_y += 1
            # Determine position in the 3x3 grid
            row = big_idx // 3
            col = big_idx % 3
            
            # Adjust offset based on position (edges get less offset)
            offset_left = 4 if col > 0 else 1  # Left edge boards get minimal offset
            offset_right = 4 if col < 2 else -1  # Right edge boards get minimal offset
            offset_top = 4 if row > 0 else 1   # Top edge boards get minimal offset
            offset_bottom = 4 if row < 2 else -1 # Bottom edge boards get minimal offset
            
            if spot == big_idx:
                # Bright border for the specific board to play on
                pygame.draw.rect(screen, (255, 165, 0), 
                            [big_x - offset_left + 1, big_y - offset_top + 1, 
                                big_cell_size + offset_left + offset_right - 2, 
                                big_cell_size + offset_top + offset_bottom - 2], 6)  # Orange
            elif spot == -1 and big_idx not in elem_spots:
                # Lighter border for all available boards
                pygame.draw.rect(screen, (100, 200, 100), 
                            [big_x - offset_left + 1, big_y - offset_top + 1, 
                                big_cell_size + offset_left + offset_right - 2, 
                                big_cell_size + offset_top + offset_bottom - 2], 6)  # Light green

def get_clicked_position(mouse_pos):
    #Convert mouse position to (big_board_index, small_cell_index)
    mx, my = mouse_pos
    
    # Which big board?
    big_col = (mx - Margin) // big_cell_size
    big_row = (my - Margin) // big_cell_size
    
    if not (0 <= big_col < 3 and 0 <= big_row < 3):
        return None, None
    
    big_idx = big_row * 3 + big_col
    
    # Which small cell within that board?
    local_x = mx - (Margin + big_col * big_cell_size)
    local_y = my - (Margin + big_row * big_cell_size)
    
    small_col = local_x // small_cell_size
    small_row = local_y // small_cell_size
    
    if not (0 <= small_col < 3 and 0 <= small_row < 3):
        return None, None
    
    small_idx = small_row * 3 + small_col
    
    return big_idx, small_idx

# Initial draw
draw_board()
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Check for 'R' key to reset
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset_game()
            
        # Only allow moves if game is not over
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            pos = pygame.mouse.get_pos()
            big_idx, small_idx = get_clicked_position(pos)
            
            if big_idx is not None and small_idx is not None:
                # Check if this is a valid move
                if spot == -1 or spot == big_idx:  # Can play anywhere or must play here
                    if big_idx not in elem_spots:  # Board not won yet
                        if board_data[big_idx][small_idx] not in ["X", "O"]:  # Cell empty
                            # Make the move
                            board_data[big_idx][small_idx] = player
                            prev_spot = big_idx
                            spot = small_idx
                            turn += 1
                            
                            # Check if small board is won
                            if check_small_win(board_data, prev_spot):
                                elem_spots.append(prev_spot)
                                entire_board_data[prev_spot] = player
                                # Clear the board and show winner
                                for j in range(9):
                                    board_data[prev_spot][j] = " "
                            
                            # Check if large board is won
                            if check_large_win(entire_board_data):
                                game_over = True
                                winner = player
                            # Check for tie
                            elif check_tie():
                                game_over = True
                                winner = None
                            
                            # Check if next board is available
                            if spot in elem_spots:
                                spot = -1  # Can play anywhere
                            
                            # Switch player
                            player = "O" if player == "X" else "X"
                            
                            needs_redraw = True
    
    # Only redraw when something changed
    if needs_redraw:
        draw_board()
        pygame.display.flip()
        needs_redraw = False
    
    clock.tick(60)

pygame.quit()