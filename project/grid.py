import pygame, random
import numpy as np


class Conway:
    ###################################
    # Class for Conway's Game of Life #
    ###################################

    def __init__(self, width, height, scale, border, percentRandom):
        self.scale = scale

        self.rows = int(width / scale)
        self.columns = int(height / scale)
        self.size = (self.rows, self.columns)

        self.curr_array = np.ndarray(shape=self.size)  # Field as 2d array
        self.border = border  # Lines between cells
        self.percentRandom = percentRandom

    def update(self, dead, live, surface):
        """
        Updates cells color correlating to dead or live
        """
        for x in range(self.rows):
            for y in range(self.columns):
                x_pos, y_pos = x * self.scale, y * self.scale
                if self.curr_array[x][y] == 1:
                    pygame.draw.rect(surface, live,
                                     [x_pos, y_pos, self.scale - self.border, self.scale - self.border])
                else:
                    pygame.draw.rect(surface, dead,
                                     [x_pos, y_pos, self.scale - self.border, self.scale - self.border])

    def transition(self):
        """
        Rules for transitions between generations
        """
        new_array = np.ndarray(shape=self.size)
        for x in range(self.rows):
            for y in range(self.columns):
                state = self.curr_array[x][y]
                neighbors = self.get_neighbors(x, y)
                # Any live cell with two or three live neighbors survives.
                if state == 1 and (neighbors == 2 or neighbors == 3):
                    new_array[x][y] = 1
                # Any dead cell with three live neighbors becomes a live cell.
                elif state == 0 and neighbors == 3:
                    new_array[x][y] = 1
                # All other live cells die in the next generation.
                # Similarly, all other dead cells stay dead.
                else:
                    new_array[x][y] = 0

        # update previous field with next generation's field
        self.curr_array = new_array

    def get_neighbors(self, x, y):
        """
        Check state of 8 cells around current cell
        Returns number of live neighbors
        """
        neighbors = 0
        for n in range(-1, 2):
            for m in range(-1, 2):
                if not (n == m == 0):  # Ignore self during check
                    # Since field is finite, stitch edges to yield toroidal array
                    x_edge = (x + n + self.rows) % self.rows
                    y_edge = (y + m + self.columns) % self.columns
                    neighbors += self.curr_array[x_edge][y_edge]
        return neighbors

    def click(self, pos):
        """
        Clicking on cell will change it's state from dead to live or vice versa
        """
        x, y = int(pos[0] / self.scale), int(pos[1] / self.scale)
        if self.curr_array[x][y] == 1:
            self.curr_array[x][y] = 0
        else:
            self.curr_array[x][y] = 1

    def random_field(self):
        """
        Generates random field of cells
        """
        for x in range(self.rows):
            for y in range(self.columns):
                # self.curr_array[x][y] = random.randint(0, 1)
                self.curr_array[x][y] = random.choices(
                    [0, 1], [1 - self.percentRandom, self.percentRandom])[0]  # Fills grid with percentRandom live cells

    def reset(self):
        """
        Clears entire field to all dead cells
        """
        for x in range(self.rows):
            for y in range(self.columns):
                self.curr_array[x][y] = 0


class RPS:
    ###############################################
    # Class for ternary/quinary multi-state world #
    ###############################################

    # Rock = -1, White = 0, Paper = 1, Scissors = 2, Lizard = 3, Spock = 4
    def __init__(self, width, height, scale, border, numColors):
        self.scale = scale

        self.rows = int(width / scale)
        self.columns = int(height / scale)
        self.size = (self.rows, self.columns)

        self.curr_array = np.ndarray(shape=self.size)  # Field as 2d array
        self.border = border  # Lines between cells
        self.numColors = numColors

    def update(self, rock, paper, scissors, lizard, spock, surface):
        """
        Updates cells colors on field
        """
        for x in range(self.rows):
            for y in range(self.columns):
                x_pos, y_pos = x * self.scale, y * self.scale
                curr = self.curr_array[x][y]
                if -1 < curr < 1:  # Fix rounding error near 0 for numpy array
                    pygame.draw.rect(surface, (255, 255, 255),
                                     [x_pos, y_pos, self.scale - self.border, self.scale - self.border])
                elif curr == -1:
                    pygame.draw.rect(surface, rock,
                                     [x_pos, y_pos, self.scale - self.border, self.scale - self.border])
                elif curr == 1:
                    pygame.draw.rect(surface, paper,
                                     [x_pos, y_pos, self.scale - self.border, self.scale - self.border])
                elif curr == 2:
                    pygame.draw.rect(surface, scissors,
                                     [x_pos, y_pos, self.scale - self.border, self.scale - self.border])
                elif curr == 3 and self.numColors == 5:
                    pygame.draw.rect(surface, lizard,
                                     [x_pos, y_pos, self.scale - self.border, self.scale - self.border])
                elif curr == 4 and self.numColors == 5:
                    pygame.draw.rect(surface, spock,
                                     [x_pos, y_pos, self.scale - self.border, self.scale - self.border])

    def transition(self):
        """
        Updates current field with next generation field
        """
        new_array = np.ndarray(shape=self.size)
        for x in range(self.rows):
            for y in range(self.columns):
                state = self.curr_array[x][y]
                neighbors, dominating = self.get_neighbors(x, y, state)
                if neighbors > 2:  # if more than 2 cells dominate current cell, convert cell
                    # if current cell is touched by more than 2 cells of both dominating colors,
                    # then convert current cell to the dominant color with the greater frequency
                    # Example: Rock surrounded by 3 paper and 5 spock, rock becomes spock
                    new_array[x][y] = most_freq(dominating)
                else:  # otherwise cell stays the same
                    new_array[x][y] = state

        # update previous field with next generation's field
        self.curr_array = new_array

    def get_neighbors(self, x, y, state):
        """
        Rules for transitions between generations
        total: number of dominant neighbors
        num_dominating: list of dominant neighbors
        Example: state = rock, total = 8
                 num_dominating = [paper, paper, paper, spock, spock, spock, spock, spock]
        """

        total, num_dominating = 0, []
        # check 8 cells around current cell
        for n in range(-1, 2):
            for m in range(-1, 2):
                if not (n == m == 0):  # Ignore self during check
                    # Since field is finite, stitch edges to yield toroidal array
                    x_edge = (x + n + self.rows) % self.rows
                    y_edge = (y + m + self.columns) % self.columns
                    neighbor = self.curr_array[x_edge][y_edge]
                    if self.numColors == 3:  # Normal Rock, Paper, Scissor rules
                        if (state == -1 and neighbor == 1) or (state == 1 and neighbor == 2) \
                                or (state == 2 and neighbor == -1):
                            total += 1
                            num_dominating.append(neighbor)

                    elif self.numColors == 5:
                        # Rock (-1), Paper (1), Scissor(2), Lizard(3), Spock(4) rules
                        # Rock > Scissors, Lizard
                        # Paper > Rock, Spock
                        # Scissors > Paper, Lizard
                        # Lizard > Paper, Spock
                        # Spock > Scissors, Rock
                        if (state == -1 and (neighbor == 1 or neighbor == 4)) or \
                                (state == 1 and (neighbor == 2 or neighbor == 3)) \
                                or (state == 2 and (neighbor == -1 or neighbor == 4)) \
                                or (state == 3 and (neighbor == -1 or neighbor == 2)) \
                                or (state == 4 and (neighbor == 1 or neighbor == 3)):
                            total += 1
                            num_dominating.append(neighbor)
        return total, num_dominating

    def click(self, pos, choice):
        """
        Clicking on cell will change it's state to choice of color currently pressed (1-5)
        Default is white
        """
        x, y = int(pos[0] / self.scale), int(pos[1] / self.scale)
        self.curr_array[x][y] = choice

    def random_field(self):
        """
        Generates random field of cells
        """
        for x in range(self.rows):
            for y in range(self.columns):
                if self.numColors == 3:
                    self.curr_array[x][y] = random.choices([-1, 1, 2])[0]
                elif self.numColors == 5:
                    self.curr_array[x][y] = random.choices([-1, 1, 2, 3, 4])[0]

    def reset(self):
        """
        Clears entire field to all white cells
        """
        for x in range(self.rows):
            for y in range(self.columns):
                self.curr_array[x][y] = 0


def most_freq(neighbors):
    """
    Returns the dominant color with the greater frequency
    Example: num_dominating = [paper, paper, paper, spock, spock, spock, spock, spock]
             Returns: spock
    """
    return max(set(neighbors), key=neighbors.count)


class Langton:
    ###########################
    # Class for Langton's Ant #
    ###########################

    def __init__(self, width, height, scale, border, colors, rules):
        self.scale = scale

        self.rows = int(width / scale)
        self.columns = int(height / scale)
        self.size = (self.rows, self.columns)

        self.curr_array = np.ndarray(shape=self.size)  # Field as 2d array
        self.border = border  # Lines between cells

        self.direction = "N"  # N, E, S, W
        self.ant = (-1, -1)  # Ant current position on field

        # Colors [(x,y,z), ..., (xn,yn,zn)], Rules = "RL..."
        self.rules = rules
        self.colors = colors

    def transition(self, surface):
        """
        Updates cells colors on field between each transition
        """
        ant_xpos, ant_ypos = self.ant[0], self.ant[1]
        ant_xcoord, ant_ycoord = ant_xpos * self.scale, ant_ypos * self.scale

        if self.curr_array[ant_xpos][ant_ypos] == -1:  # curr cell is white (default)
            self.curr_array[ant_xpos][ant_ypos] = 0  # change cell to first color
            self.rotate(self.rules[0])  # rotate direction based on first rule

            # Update color of cell ant is currently on
            # Move ant forward in current direction
            # Draw ant on that forward cell
            pygame.draw.rect(surface, self.colors[0],
                             [ant_xcoord, ant_ycoord, self.scale - self.border, self.scale - self.border])
            self.move()
            pygame.draw.rect(surface, (255, 0, 0),
                             [self.ant[0] * self.scale, self.ant[1] * self.scale,
                              self.scale - self.border, self.scale - self.border])

        else:
            # updates value of cell to n+1 color
            # if end of color list, return to index 0
            update_idx = (int(self.curr_array[ant_xpos][ant_ypos]) + 1) % len(self.colors)
            self.curr_array[ant_xpos][ant_ypos] = update_idx

            # rotate direction based on rule of next color
            self.rotate(self.rules[update_idx])

            # Update color of cell ant is currently on
            # Move ant forward in current direction
            # Draw ant on that forward cell
            pygame.draw.rect(surface, self.colors[update_idx],
                             [ant_xcoord, ant_ycoord, self.scale - self.border, self.scale - self.border])
            self.move()
            pygame.draw.rect(surface, (255, 0, 0),
                             [self.ant[0] * self.scale, self.ant[1] * self.scale,
                              self.scale - self.border, self.scale - self.border])

    def move(self):
        """
        Changes ant's current location to cell 1 away in it's current direction
        """
        x, y = self.ant[0], self.ant[1]
        # Stitches field for when ant is at edge
        addx, addy = (x + 1) % self.rows, (y+1) % self.columns
        minusx, minusy = (x - 1) % self.rows, (y - 1) % self.columns
        if self.direction == "N":
            self.ant = (x, minusy)
        elif self.direction == "E":
            self.ant = (addx, y)
        elif self.direction == "S":
            self.ant = (x, addy)
        elif self.direction == "W":
            self.ant = (minusx, y)

    def rotate(self, rule):
        """
        Changes current direction based on rule
        """
        if rule == "R":
            if self.direction == "N":
                self.direction = "E"
            elif self.direction == "E":
                self.direction = "S"
            elif self.direction == "S":
                self.direction = "W"
            elif self.direction == "W":
                self.direction = "N"

        elif rule == "L":
            if self.direction == "N":
                self.direction = "W"
            elif self.direction == "E":
                self.direction = "N"
            elif self.direction == "S":
                self.direction = "E"
            elif self.direction == "W":
                self.direction = "S"

    def click(self, pos, direction, surface):
        """
        Clicking on cell spawns ant in specified direction
        """
        x, y = int(pos[0] / self.scale), int(pos[1] / self.scale)
        prev_x, prev_y = self.ant[0] * self.scale, self.ant[1] * self.scale
        new_x, new_y = x * self.scale, y * self.scale

        if self.ant != (-1, -1):  # There is an ant on the field currently
            # make sure previous cell where ant was can still update later
            # by making that cell empty (white)
            self.curr_array[self.ant[0], self.ant[1]] = -1
            # On clicking, deletes previous ant
            pygame.draw.rect(surface, (255, 255, 255),
                             [prev_x, prev_y, self.scale - self.border, self.scale - self.border])

        # Creates new ant in specified direction
        self.ant = (x, y)
        pygame.draw.rect(surface, (255, 0, 0),
                         [new_x, new_y, self.scale - self.border, self.scale - self.border])
        self.direction = direction

    def reset(self, surface):
        """
        Clears entire field to all dead cells
        """
        for x in range(self.rows):
            for y in range(self.columns):
                x_pos, y_pos = x * self.scale, y * self.scale
                self.curr_array[x][y] = -1  # initial field array to all empty (-1)
                pygame.draw.rect(surface, (255, 255, 255),
                                 [x_pos, y_pos, self.scale - self.border, self.scale - self.border])
