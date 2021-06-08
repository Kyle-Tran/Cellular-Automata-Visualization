import sys, pygame, os, grid
import numpy as np


def conway_game(colorList, random):
    """
    Creates field for Conway's Game of Life
    """

    ####################
    # Initialize field #
    ####################
    screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
    # screen = pygame.display.set_mode(size_monitor, pygame.RESIZABLE)
    screen.fill(black)
    conway.update(colorList[0], colorList[1], surface=screen)
    conway.transition()
    if random == "y" or random == "Y":
        conway.random_field()

    #############
    # Game Loop #
    #############
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
            pygame.display.set_caption("Conway's Game Of Life - Generation " + str(generation))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                button = event.button
                if button == 1:  # change cell state with left click
                    pos = pygame.mouse.get_pos()
                    conway.click(pos)
                elif button == 3:  # iterate through next generation once with right click
                    conway.transition()
                    generation += 1
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        conway.update(colorList[0], colorList[1], surface=screen)
        pygame.display.update()


def rps_game(colorList, random):
    """
    Creates field for ternary/quinary multi-state world
    """

    ####################
    # Initialize field #
    ####################
    screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
    # screen = pygame.display.set_mode(size_monitor, pygame.RESIZABLE)
    screen.fill(black)
    rps.update(colorList[0], colorList[1], colorList[2], colorList[3], colorList[4], surface=screen)
    rps.transition()
    if random == "y" or random == "Y":
        rps.random_field()

    #############
    # Game Loop #
    #############
    generation = 0
    while True:
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
            pygame.display.set_caption(
                "Rock, Paper, Scissors, Lizard, Spock Cellular Automata - Generation " + str(generation))

        # Similar as reset above, but randomizes field using command Ctrl + T
        if (keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]) and keys[pygame.K_t]:
            rps.reset()
            rps.random_field()
            generation = 0
            pygame.display.set_caption(
                "Rock, Paper, Scissors, Lizard, Spock Cellular Automata - Generation " + str(generation))

        for event in pygame.event.get():
            # Rock = -1, White (background) = 0, Paper = 1, Scissors = 2, Lizard = 3, Spock = 4
            if event.type == pygame.MOUSEBUTTONDOWN:
                button, choice = event.button, 0  # default 0
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

        rps.update(colorList[0], colorList[1], colorList[2], colorList[3], colorList[4], surface=screen)
        pygame.display.update()


def langtons_ant():
    """
    Creates field for Langton's ant
    """

    ####################
    # Initialize field #
    ####################
    # screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
    screen = pygame.display.set_mode(size_monitor, pygame.RESIZABLE)
    screen.fill(black)
    langton.reset(screen)
    langton.transition(screen)

    #############
    # Game Loop #
    #############
    generation = 0
    while True:
        pygame.display.set_caption(
            "Langston's Ant - Generation " + str(generation))
        # clock.tick(fps)  # Comment out for fastest performance
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
                button, choice = event.button, 'N'  # default orientation is North
                if keys[pygame.K_UP]:  # Hold up arrow for North
                    choice = "N"
                if keys[pygame.K_RIGHT]:  # Hold up arrow for East
                    choice = "E"
                if keys[pygame.K_DOWN]:  # Hold up arrow for South
                    choice = "S"
                if keys[pygame.K_LEFT]:  # Hold up arrow for West
                    choice = "W"

                if button == 1:  # place ant in new location
                    pos = pygame.mouse.get_pos()
                    generation = 0
                    pygame.display.set_caption(
                        "Langston's Ant - Generation " + str(generation))
                    langton.click(pos, choice, screen)
                elif button == 3:  # iterate through next generation once right click
                    langton.transition(screen)
                    generation += 1
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def random_color():
    """
    Creates 3-tuple representing RGB value (r, g, b)
    """
    return tuple(np.random.choice(range(256), size=3))


if __name__ == '__main__':
    """
    Main loop to initialize each game
    Make your own changes here
    """

    #####################
    # Variables to edit #
    #####################
    "*** COLORS ***"
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
    # add anymore more colors you would like

    "*** COLOR LISTS/RULES***"
    # Input color selection into following lists for each game mode
    conway_colors = [white, duke_blue]  # [dead color, live color]
    rps_colors = [rock, paper, scissors, lizard, spock]  # make sure list is of length 5

    # Change rules for Langton's Ant here
    # Use only R's and L's
    langton_rules = "LLRR"
    langton_colors = [random_color() for _ in range(len(langton_rules))]  # random RGB color for each rule

    # # Option to make only black and white colors for each rule
    # # Example: R = black, L = White
    # langton_colors = []
    # color_dict = {"R": black, "L": white}
    # for i in langton_rules:
    #     langton_colors.append(color_dict[i])

    "*** GAME SPEED ***"
    clock = pygame.time.Clock()
    # Speed between generations
    # Recommend number between 1 < x < 60
    fps = 60

    "*** OTHER OPTIONS ***"

    # Scales monitor resolution down by factor of scalar
    # Recommended 30-60 for average CPU and 10-20 for powerful CPU (Conway / RPS)
    # Recommend 1-10 for more complex Langton's ant
    scalar = 40

    # Percent of random cells that are live for Conway's Game of Life (0 < x < 1)
    # Recommend value between 0.1 < x < 0.5
    percentRandom = .4
    ################################################################################

    ##########################################
    # Game settings - CAN IGNORE BELOW ITEMS #
    ##########################################

    # Center environment, initialize pygame
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()

    # Setup window for current display resolution
    info = pygame.display.Info()
    width, height = info.current_w, info.current_h - 50  # Includes toolbar
    size_monitor = (width, height)

    # Selection option
    mode, rand, numColors, border = "", "", None, None
    while mode != "1" and mode != "2" and mode != "3":
        mode = input("Select mode (1: Conway's Game of Life; 2: Rock Paper Scissors Cellular Automata; "
                     "3: Langton's Ant):  ")
    if mode == "2":  # Choose between 3- or 5-state multi-world
        while numColors != "t" and numColors != "T" and numColors != "q" and numColors != "Q":
            numColors = input("Select Ternary of Quinary (t/q): ")
    if mode != "3":  # Don't generate random field for Langton's Ant
        while rand != "y" and rand != "n" and rand != "Y" and rand != "N":
            rand = input("Would you like a randomly generated field? (y/n): ")
    while border != "y" and border != "n" and border != "Y" and border != "N":
        border = input("Would you like cell borders? (y/n): ")

    border = 1 if border == "y" or border == "Y" else 0
    numColors = 3 if numColors == "t" or numColors == "T" else 5

    # Call game creation functions
    if mode == "1":
        conway = grid.Conway(width, height, scalar, border, percentRandom)
        conway_game(conway_colors, rand)
    elif mode == "2":
        rps = grid.RPS(width, height, scalar, border, numColors)
        rps_game(rps_colors, rand)
    elif mode == "3":
        langton = grid.Langton(width, height, scalar, border, langton_colors, langton_rules)
        langtons_ant()
