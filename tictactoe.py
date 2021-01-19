import pygame as pg





# function to check if won

# function to check if draw

# pygame allow clickable interface

# game loop:
    # alternate between X and O
    # after each placement, check if player wins


#initialize pygame
pg.init()



board = []


for row in range(3):
    board.append([])
    for column in range(3):
        board[row].append(0)



HEIGHT: int = 500
WIDTH: int = 500
MARGIN: int = 10

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pg.display.set_mode((WIDTH, HEIGHT))

pg.display.set_caption("Tic Tac Toe")


def initialize_board(display):
    background = pg.Surface(display.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    pg.draw.line(background, (0,0,0), ((WIDTH // 3), 0), ((WIDTH // 3), HEIGHT), 2)
    pg.draw.line(background, (0,0,0), (2 * (WIDTH //3), 0), (2 * (WIDTH // 3), HEIGHT), 2)

    pg.draw.line(background, (0,0,0), (0, (HEIGHT // 3)), (WIDTH, (HEIGHT // 3)), 2)
    pg.draw.line(background, (0,0,0), (0, 2 * (HEIGHT // 3)), (WIDTH, 2 * (HEIGHT // 3)), 2)

    return background




board = initialize_board(screen)

running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            print("click")
        
        screen.blit(board, (0,0))
        pg.display.flip()

pg.quit()

