import re
import pygame

pygame.init()

#Variables
screen_width = 300
screen_height = 300
bg_color = (235,201,52)
grid_line_color = (0,0,0)
line_width = 5
markers = []
clicked = False
pos = []
player = 1
cross_color = (6,71,17)
circle_color = (255,0,0)

#Display Screen
pygame.display.set_caption("TicTacToe")
screen = pygame.display.set_mode((screen_width, screen_height))

#Functions
def draw_grid():
    screen.fill(bg_color)
    pygame.draw.line(screen, grid_line_color, (0,100), (300,100), line_width)
    pygame.draw.line(screen, grid_line_color, (0,200), (300,200), line_width)
    pygame.draw.line(screen, grid_line_color, (100,0), (100,300), line_width)
    pygame.draw.line(screen, grid_line_color, (200,0), (200,300), line_width)

def draw_markers():
    x_pos = 0
    for x in markers:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(screen, cross_color, (x_pos*100 + 15, y_pos*100 + 15), (x_pos*100 + 85, y_pos*100 + 85), line_width)
                pygame.draw.line(screen, cross_color, (x_pos*100 + 15, y_pos*100 + 85), (x_pos*100 + 85, y_pos*100 + 15), line_width)
            if y == -1:
                pygame.draw.circle(screen, circle_color, (x_pos*100 + 50, y_pos*100 + 50), 38, line_width) 
            y_pos += 1
        x_pos += 1           


for i in range(3):
    row = [0]*3
    markers.append(row)







#Game Loop
exit_game = False

while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked = False   
            pos = pygame.mouse.get_pos()     
            cell_x = pos[0]
            cell_y = pos[1]
            if markers[cell_x // 100][cell_y // 100] == 0:
                markers[cell_x // 100][cell_y // 100] = player
                player *= -1
  
    draw_grid()
    draw_markers()
    pygame.display.update()

pygame.quit()
quit()           