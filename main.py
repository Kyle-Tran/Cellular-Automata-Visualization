import pygame
import grid
from win32api import GetSystemMetrics

pygame.init()
width, height = GetSystemMetrics(0), GetSystemMetrics(1)
size = (width, height)

pygame.display.set_caption("CONWAY'S GAME OF LIFE")
screen = pygame.display.set_mode(size)

scalar = 40
offset = 1

Grid = grid.Grid(width, height, scalar, offset)

black = (0, 0, 0)
blue = (0, 14, 71)
white = (255, 255, 255)

run = True
while run:
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    Grid.conway(off_color=white, on_color=blue, surface=screen)
    pygame.display.update()

pygame.quit()
