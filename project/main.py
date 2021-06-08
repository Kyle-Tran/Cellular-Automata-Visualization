import sys, pygame, os
import grid
import numpy as np


def conway_game(dead, live, random):
    # Initialize field
    screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
    # screen = pygame.display.set_mode(size, pygame.RESIZABLE)
    screen.fill(black)
    conway.update(dead, live, surface=screen)
    conway.transition()
    if random == "y" or random == "Y":
        conway.random_field()

    generation = 0
    while True:
        pygame.display.set_caption("Conway's Game Of Life - Generation " + str(generation))
        clock.tick(fps)
        keys = pygame.key.get_pressed()

        # Continually iterates through generations while space is held
        if keys[pygame.K_SPACE]:
            conway.transition()
            generation += 1

        # Resets field and generation to 0 using command Ctrl + R
        if (keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]) and keys[pygame.K_r]:
            conway.reset()
            generation = 0
            pygame.display.set_caption("Conway's Game Of Life - Generation " + str(generation))

        # Similar as reset above, but randomizes field using command Ctrl + T
        if (keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]) and keys[pygame.K_t]:
            conway.reset()
            conway.random_field()
            generation = 0
            pygame.display.set_caption("Rock, Paper, Scissors Cellular Automata - Generation " + str(generation))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                button = event.button
                if button == 1:  # change cell state with left click
                    pos = pygame.mouse.get_pos()
                    conway.click(pos)
                elif button == 3:  # iterate through next generation once right click
                    conway.transition()
                    generation += 1
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        conway.update(dead, live, surface=screen)
        pygame.display.update()


def rps_game(rock, paper, scissors, lizard, spock, random):
    # Initialize field
    screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
    # screen = pygame.display.set_mode(size, pygame.RESIZABLE)
    screen.fill(black)
    # rps.update(rock=orange, paper=light_blue, scissors=red, surface=screen)
    # rps.update(rock=p1, paper=p2, scissors=p3, surface=screen)
    rps.update(rock, paper, scissors, lizard, spock, surface=screen)
    rps.transition()
    if random == "y" or random == "Y":
        rps.random_field()

    generation = 0
    while True:
        # pygame.display.set_caption("Rock, Paper, Scissors Cellular Automata - Generation " + str(generation))
        pygame.display.set_caption(
            "Rock, Paper, Scissors, Lizard, Spock Cellular Automata - Generation " + str(generation))

        clock.tick(fps)
        keys = pygame.key.get_pressed()

        # Continually iterates through generations while space is held
        if keys[pygame.K_SPACE]:
            rps.transition()
            generation += 1

        # Resets field and generation to 0 using command Ctrl + R
        if (keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]) and keys[pygame.K_r]:
            rps.reset()
            generation = 0
            # pygame.display.set_caption("Rock, Paper, Scissors Cellular Automata - Generation " + str(generation))
            pygame.display.set_caption(
                "Rock, Paper, Scissors, Lizard, Spock Cellular Automata - Generation " + str(generation))

        # Similar as reset above, but randomizes field using command Ctrl + T
        if (keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]) and keys[pygame.K_t]:
            rps.reset()
            rps.random_field()
            generation = 0
            # pygame.display.set_caption("Rock, Paper, Scissors Cellular Automata - Generation " + str(generation))
            pygame.display.set_caption(
                "Rock, Paper, Scissors, Lizard, Spock Cellular Automata - Generation " + str(generation))

        for event in pygame.event.get():
            # Rock = -1, White = 0, Paper = 1, Scissors = 2, Lizard = 3, Spock = 4
            if event.type == pygame.MOUSEBUTTONDOWN:
                button, choice = event.button, 0
                if keys[pygame.K_1]:  # Hold 1 for rock
                    choice = -1
                if keys[pygame.K_2]:  # Hold 2 for paper
                    choice = 1
                if keys[pygame.K_3]:  # Hold 3 for scissors
                    choice = 2
                if keys[pygame.K_4]:  # Hold 4 for lizard
                    choice = 3
                if keys[pygame.K_5]:  # Hold 5 for Spock
                    choice = 4

                if button == 1:  # change cell state with left click
                    pos = pygame.mouse.get_pos()
                    rps.click(pos, choice)
                elif button == 3:  # iterate through next generation once right click
                    rps.transition()
                    generation += 1
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # rps.update(rock=orange, paper=light_blue, scissors=red, surface=screen)
        # rps.update(rock=p1, paper=p2, scissors=p3, surface=screen)
        rps.update(rock, paper, scissors, lizard, spock, surface=screen)
        pygame.display.update()


def langtons_ant():
    # Initialize field
    # screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
    screen = pygame.display.set_mode(size, pygame.RESIZABLE)
    screen.fill(light_blue)
    langton.reset(screen)
    langton.transition(screen)

    generation = 0
    while True:
        pygame.display.set_caption(
            "Langston's Ant - Generation " + str(generation))
        # clock.tick(fps)
        keys = pygame.key.get_pressed()

        # Continually iterates through generations while space is held
        if keys[pygame.K_SPACE]:
            langton.transition(screen)
            generation += 1

        # Resets field and generation to 0 using command Ctrl + R
        if (keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]) and keys[pygame.K_r]:
            langton.reset(screen)
            generation = 0
            pygame.display.set_caption(
                "Langston's Ant - Generation " + str(generation))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                button, choice = event.button, 'N'
                if keys[pygame.K_UP]:
                    choice = "N"
                if keys[pygame.K_RIGHT]:
                    choice = "E"
                if keys[pygame.K_DOWN]:
                    choice = "S"
                if keys[pygame.K_LEFT]:
                    choice = "W"

                if button == 1:  # change cell state with left click
                    pos = pygame.mouse.get_pos()
                    langton.click(pos, choice, screen)
                elif button == 3:  # iterate through next generation once right click
                    langton.transition(screen)
                    generation += 1
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def random_color():
    return tuple(np.random.choice(range(256), size=3))


if __name__ == '__main__':
    # Colors
    black = (0, 0, 0)
    duke_blue = (1, 33, 105)
    white = (255, 255, 255)

    orange = (255, 127, 0)
    light_blue = (31, 120, 180)
    red = (228, 26, 28)

    rock = (239, 187, 255)
    paper = (216, 150, 255)
    scissors = (190, 41, 236)
    lizard = (128, 0, 128)
    spock = (102, 0, 102)

    # Center environment, initialize pygame
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()

    # Setup window for different displays
    info = pygame.display.Info()
    width, height = info.current_w, info.current_h - 50
    size = (width, height)

    # fps between generations
    clock = pygame.time.Clock()
    fps = 60  # Speed between generations
              # Recommend number between 1 < x < 60

    # Selections
    mode, random, border = "", "", None
    while mode != "1" and mode != "2" and mode != "3":
        mode = input("Select mode (1: Conway's Game of Life; 2: Rock Paper Scissors Cellular Automata; "
                     "3: Langton's Ant):  ")
    if mode != "3":
        while random != "y" and random != "n" and random != "Y" and random != "N":
            random = input("Would you like a randomly generated field? (y/n): ")
    while border != "y" and border != "n" and border != "Y" and border != "N":
        border = input("Would you like cell borders? (y/n): ")
    if border == "y" or border == "Y":
        border = 1
    else:
        border = 0

    scalar = 4  # Scales monitor resolution down by factor of scalar
                 # Recommended 30-60 for average CPU and 10-20 for powerful CPU)
    percentRandom = .4  # Percent of random cells that are live (0 < x < 1)
                        # Recommend value between 0.1 < x < 0.5
    numColors = 3  # 3 for ternary, 5 for quinary

    rules = "LLRRRLRLRLLR"
    colors = [random_color() for _ in range(len(rules))]
    # colors = [black, white]
    # colors = []
    # color_dict = {"R": black, "L": white}
    # for i in rules:
    #     colors.append(color_dict[i])

    conway = grid.Conway(width, height, scalar, border, percentRandom)
    rps = grid.RPS(width, height, scalar, border, numColors)
    langton = grid.Langton(width, height, scalar, border, colors, rules)

    if mode == "1":
        conway_game(white, duke_blue, random)
    elif mode == "2":
        rps_game(rock, paper, scissors, lizard, spock, random)
    elif mode == "3":
        langtons_ant()
