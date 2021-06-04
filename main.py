import sys, pygame, grid, os

# Center environment, initialize pygame
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

# Setup window for different displays
info = pygame.display.Info()
width, height = info.current_w, info.current_h - 50
size = (width, height)
screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
# screen = pygame.display.set_mode(size, pygame.RESIZABLE)

# Create Grid
scalar = 40
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

# Initialize field
screen.fill(black)
Grid.update(dead=white, live=blue, surface=screen)
Grid.transition()

def game():
    generation = 0
    while True:
        pygame.display.set_caption("Conway's Game Of Life - Generation " + str(generation))
        clock.tick(speed)
        keys = pygame.key.get_pressed()

        # Continually iterates through generations while space is held
        if keys[pygame.K_SPACE]:
            Grid.transition()
            generation += 1

        # Resets board and generation to 0 using command Ctrl + R
        if (keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]) and keys[pygame.K_r]:
            Grid.reset()
            generation = 0
            pygame.display.set_caption("Conway's Game Of Life - Generation " + str(generation))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                button = event.button
                if button == 1:  # change cell state with left click
                    pos = pygame.mouse.get_pos()
                    Grid.click(pos)
                elif button == 3:  # iterate through next generation once right click
                    Grid.transition()
                    generation += 1
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        Grid.update(dead=white, live=blue, surface=screen)
        pygame.display.update()


if __name__ == '__main__':
    game()
