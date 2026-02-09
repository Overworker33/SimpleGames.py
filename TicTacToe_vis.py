import pygame
pygame.init()
BG = (250, 250, 250)
Black = (0, 0, 0)
Red = (255, 0, 0)
Width = 640
Height = 640
Margin = 64
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Tic Tac Toe")
board_text_font = pygame.font.SysFont("Arial", 100)
text_font = pygame.font.SysFont("Arial", 50)
clock = pygame.time.Clock()

def draw_text_centered(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    rect = img.get_rect(center=(x, y))
    screen.blit(img, rect)

def check_win(b, _player):
    wins = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    for line in wins:
        if all(b[i] == _player for i in line): 
            return line
    return None

def get_cell_center(index):
    row = index // 3
    col = index % 3
    x = Margin + col * cell_size + cell_size // 2
    y = Margin + row * cell_size + cell_size // 2
    return (x, y)

def draw_board():
    #Draw the entire board - call only when needed
    screen.fill(BG)
    pygame.draw.rect(screen, Black, [Margin+10, Margin+10, (Width - 2*Margin)-12, (Height - 2*Margin)-12])
    
    if WIN:
        text = f"Player {player} wins!"
        win_text = text_font.render(text, True, Black)
        win_rect = win_text.get_rect(center=(Width//2, 30))
        screen.blit(win_text, win_rect)
    
    # Draw grid
    for row in range(3):
        for col in range(3):
            x = Margin + col * cell_size + line_width
            y = Margin + row * cell_size + line_width
            pygame.draw.rect(screen, BG, [x, y, cell_size - line_width, cell_size - line_width])
    
    # Draw X's and O's
    for row in range(3):
        for col in range(3):
            board_index = row * 3 + col
            if board[board_index] != "-":
                center_x = Margin + col * cell_size + cell_size // 2
                center_y = Margin + row * cell_size + cell_size // 2
                draw_text_centered(board[board_index], board_text_font, Black, center_x, center_y)
    
    # Draw winning line
    if winning_line:
        start_pos = get_cell_center(winning_line[0])
        end_pos = get_cell_center(winning_line[2])
        pygame.draw.line(screen, Red, start_pos, end_pos, 8)

player = "X"
board = ["-","-","-","-","-","-","-","-","-"]
cell_size = (Width - 2*Margin) // 3
line_width = 10
WIN = False
winning_line = None
needs_redraw = True  # Flag to track if we need to redraw

# Initial draw
draw_board()
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and WIN == False:
            pos = pygame.mouse.get_pos()
            column = (pos[0] - Margin) // cell_size
            row = (pos[1] - Margin) // cell_size
            
            if 0 <= column < 3 and 0 <= row < 3:
                board_index = row * 3 + column
                
                if board[board_index] == "-":
                    board[board_index] = player
                    win_line = check_win(board, player)
                    if win_line:
                        WIN = True
                        winning_line = win_line
                    else:
                        player = "O" if player == "X" else "X"
                    
                    needs_redraw = True  # Mark that we need to redraw
    
    # Only redraw if something changed
    if needs_redraw:
        draw_board()
        pygame.display.flip()
        needs_redraw = False
    
    clock.tick(60)

pygame.quit()