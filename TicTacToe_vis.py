import pygame

pygame.init()

BG = (250, 250, 250)
Black = (0, 0, 0)

Width = 640
Hight = 640

screen = pygame.display.set_mode((Width, Hight))


#screen.fill(BG)

pygame.display.set_caption("Tic Tac Toe")

board_text_font = pygame.font.SysFont("Arial", 45)#, #bold = True)
clock = pygame.time.Clock()

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))

def draw_board():
    pass 

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG)

    draw_board()

    pygame.display.flip()

    clock.tick(60)

pygame.quit()