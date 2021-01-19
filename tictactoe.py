import pygame as pg



# function to check if won

# function to check if draw

# pygame allow clickable interface

# game loop:
    # alternate between X and O
    # after each placement, check if player wins


#initialize pygame
pg.init()


# drawing window
display = pg.display.set_mode([500, 500])



#game loop until quit
running = True
while running:

    #if user quits
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    
    #background colour
    display.fill((255, 255, 255))

    #update display
    pg.display.flip()

pg.quit()

