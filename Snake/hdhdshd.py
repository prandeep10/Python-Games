import pygame as pg

pg.init()

screen = pg.display.set_mode((900,600))
pg.display.set_caption("SNAKE")

game_over = False

while not game_over:
    if pg.key == pg.QUIT:
        game_over = True

screen.fill(255,255,255)
pg.draw.rect( screen, (255,0,0), [45,55], 10)   
pg.display.update()

pg.quit()
quit()      
