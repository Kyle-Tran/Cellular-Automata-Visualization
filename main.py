import sys, pygame, grid, os

# Center environment, initialize pygame
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

# Initialize Field
info = pygame.display.Info()
width, height = info.current_w, info.current_h - 50
size = (width, height)

pygame.display.set_caption("Conway's Game Of Life")
screen = pygame.display.set_mode(size, pygame.RESIZABLE)

# Create Grid
scalar = 40
border = 1
Grid = grid.Grid(width, height, scalar, border)
Grid.random_field()

# Colors
black = (0, 0, 0)
blue = (1, 33, 105)
white = (255, 255, 255)

while True:
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    Grid.conway(dead=white, live=blue, surface=screen)
    pygame.display.update()
