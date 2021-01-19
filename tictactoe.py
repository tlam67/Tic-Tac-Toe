########################################
# Written by Tristan Lam for 
# Junior Developer application at Tuq
#######################################



import pygame as pg #import pygame for GUI


# initialize pygame and the 2d array to form the backend of the board
pg.init()

grid = []
for row in range(3):
    grid.append([])
    for column in range(3):
        grid[row].append(0)


# XO tracks whose turn it is, represented by 0 and 1
XO: int = 0

# initialize width and height of window
HEIGHT: int = 500
WIDTH: int = 500

# constants for commonly used colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# create the display and set title
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Tic Tac Toe")


# takes in a pygame display and draws the tic tac toe board
def initialize_board(display):
    # get surface of display and fill white
    background = pg.Surface(display.get_size())
    background = background.convert()
    background.fill(WHITE)

    #draw 2 vertical lines
    pg.draw.line(background, BLACK, ((WIDTH // 3), 0), ((WIDTH // 3), HEIGHT), 2)
    pg.draw.line(background, BLACK, (2 * (WIDTH //3), 0), (2 * (WIDTH // 3), HEIGHT), 2)

    #draw 2 horizontal lines
    pg.draw.line(background, BLACK, (0, (HEIGHT // 3)), (WIDTH, (HEIGHT // 3)), 2)
    pg.draw.line(background, BLACK, (0, 2 * (HEIGHT // 3)), (WIDTH, 2 * (HEIGHT // 3)), 2)

    #return the display of the board
    return background


# takes in x and y coordinates of a mouse click and returns which cell was clicked
def click_position(x, y):
    
    #find the row
    if y < HEIGHT // 3:
        row = 0
    elif HEIGHT // 3 <= y <= 2 * (HEIGHT // 3):
        row = 1
    else:
        row = 2
    
    #find the column
    if x < WIDTH // 3:
        col = 0
    elif WIDTH // 3 <= x <= 2 * (WIDTH // 3):
        col = 1
    else:
        col = 2

    return (row, col)

# takes in the board, finds the position of the mouse click, and updates the backend array accordingly
def click_board(board):
    #get the mouse coordinates
    (mouseX, mouseY) = pg.mouse.get_pos()

    #get the row and column (cell) of the mouse click
    (row, col) = click_position(mouseX, mouseY)

    #using turn tracker
    global grid, XO

    #update the backend array
    if grid[row][col] == 0:
        if XO == 0:
            grid[row][col] = "X"
            XO = 1
        else:
            grid[row][col] = "O"
            XO = 0


# checks if the game has been won 
def has_won():

    #checking win by row
    for row in range(3):
        if grid[row][0] == grid[row][1] == grid[row][2] and grid[row][0] != 0:
            return True
    
    #checking win by column
    for col in range(3):
        if grid[0][col] == grid[1][col] == grid[2][col] and grid[0][col] != 0:
            return True

    #checking win by diagonal
    if grid[0][0] == grid[1][1] == grid[2][2] and grid[1][1] != 0:
        return True

    #checking win by diagonal
    if grid[0][2] == grid[1][1] == grid[2][0] and grid[1][1] != 0:
        return True
    
    return False

#checks if the game is a draw
def is_draw():
    for row in grid:
        for val in row:
            if val == 0:
                return False
    return True


# displays msg telling which player won or if the match was a draw
def display_game_state(won, draw):
    global XO

    #print winner message
    if won:
        if XO == 1:
            msg = "X has won!"
        else:
            msg = "O has won!"
    
    if draw:
        msg = "Draw!"

    #use pygame font to display text on board
    font = pg.font.Font(None, 24)
    text = font.render(msg, 1, (10, 10, 10))
    board.fill((250, 250, 250)) 
    board.blit(text, ((WIDTH // 2) - 30, 50))


# updates the board in the GUI to reflect new placement of pieces
def display_move(row, col, board):

    #find the center of the cell
    center_x = ((WIDTH // 3) * col) + (WIDTH // 6)
    center_y = ((HEIGHT // 3) * row) + (HEIGHT // 6)

    global XO

    #draw either circle or x in the center
    if XO == 0:
        pg.draw.circle(board, BLACK, (center_x, center_y), 44, 2)
    else:
        pg.draw.line(board, BLACK, (center_x - 50, center_y - 50), (center_x + 50, center_y + 50))
        pg.draw.line(board, BLACK, (center_x - 50, center_y + 50), (center_x + 50, center_y - 50))


# initialize board and gameloop
board = initialize_board(screen)
running = True

#gameloop
while running:
    
    #listening for pygame events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            click_board(board)
            (mouseX, mouseY) = pg.mouse.get_pos()
            (row, col) = click_position(mouseX, mouseY)
            display_move(row, col, board)
            print(grid)
            if has_won():
                screen.fill(WHITE)
                display_game_state(True, False)
            elif is_draw():
                screen.fill(WHITE)
                display_game_state(False, True)
            

        screen.blit(board, (0,0))
        pg.display.flip()

pg.quit()

