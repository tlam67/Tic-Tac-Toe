import pygame as pg





# function to check if won

# function to check if draw

# pygame allow clickable interface

# game loop:
    # alternate between X and O
    # after each placement, check if player wins


#initialize pygame
pg.init()



grid = []


for row in range(3):
    grid.append([])
    for column in range(3):
        grid[row].append(0)



XO: int = 0

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


def click_position(x, y):
    if y < HEIGHT // 3:
        row = 0
    elif HEIGHT // 3 <= y <= 2 * (HEIGHT // 3):
        row = 1
    else:
        row = 2

    if x < WIDTH // 3:
        col = 0
    elif WIDTH // 3 <= x <= 2 * (WIDTH // 3):
        col = 1
    else:
        col = 2

    return (row, col)


def click_board(board):
    (mouseX, mouseY) = pg.mouse.get_pos()

    (row, col) = click_position(mouseX, mouseY)

    global grid, XO

    if grid[row][col] == 0:
        if XO == 0:
            grid[row][col] = "X"
            XO = 1
        else:
            grid[row][col] = "O"
            XO = 0
    else:
        print("space taken")

    print(grid)





def print_position():
    (mouseX, mouseY) = pg.mouse.get_pos()
    (row, col) = click_position(mouseX, mouseY)
    print("Row: {}".format(row))
    print("Col: {}".format(col))



board = initialize_board(screen)

running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            click_board(board)
            print_position()

        screen.blit(board, (0,0))
        pg.display.flip()

pg.quit()

