import sys, pygame, grid, os

# Center environment, initialize pygame
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

# Initialize Field
info = pygame.display.Info()
width, height = info.current_w, info.current_h - 50
size = (width, height)
screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)

# Create Grid
scalar = 80
border = 1
Grid = grid.Grid(width, height, scalar, border)
# Grid.random_field()

# Colors
black = (0, 0, 0)
blue = (1, 33, 105)
white = (255, 255, 255)

# speed between generations
clock = pygame.time.Clock()
speed = 30

screen.fill(black)

def game():
    generation = 0
    while True:
        pygame.display.set_caption("Conway's Game Of Life - Generation " + str(generation))
        clock.tick(speed)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                button = event.button
                if button == 1:  # change cell state with left click
                    pos = pygame.mouse.get_pos()
                    Grid.click(pos)
                elif button == 3:  # iterate through next generation right click
                    Grid.update()
                    generation += 1
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        Grid.conway(dead=white, live=blue, surface=screen)
        #Grid.update()
        pygame.display.update()


if __name__ == '__main__':
    game()
