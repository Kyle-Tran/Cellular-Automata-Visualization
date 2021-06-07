import pygame
import numpy as np
import random


class Conway:
    def __init__(self, width, height, scale, border, percentRandom):
        self.scale = scale

        self.rows = int(width / scale)
        self.columns = int(height / scale)
        self.size = (self.rows, self.columns)

        self.curr_array = np.ndarray(shape=self.size)  # Field as 2d array
        self.border = border  # Lines between cells
        self.percentRandom = percentRandom

    def update(self, dead, live, surface):
        # updates cells to be dead or live
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
        # rules for transitions between generations
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
        neighbors = 0
        # check 8 cells around current cell
        for n in range(-1, 2):
            for m in range(-1, 2):
                if not (n == m == 0):  # Ignore self during check
                    # Since field is finite, stitch edges to yield toroidal array
                    x_edge = (x + n + self.rows) % self.rows
                    y_edge = (y + m + self.columns) % self.columns
                    neighbors += self.curr_array[x_edge][y_edge]
        return neighbors

    def click(self, pos):
        # Clicking on cell will change it's state from dead to live or vice versa
        x, y = int(pos[0] / self.scale), int(pos[1] / self.scale)
        if self.curr_array[x][y] == 1:
            self.curr_array[x][y] = 0
        else:
            self.curr_array[x][y] = 1

    def random_field(self):
        # Generates random field of cells
        for x in range(self.rows):
            for y in range(self.columns):
                # self.curr_array[x][y] = random.randint(0, 1)
                self.curr_array[x][y] = random.choices(
                    [0, 1], [1 - self.percentRandom, self.percentRandom])[0]  # Fills grid with percentRandom live cells

    def reset(self):
        # Clears entire field to all dead cells
        for x in range(self.rows):
            for y in range(self.columns):
                self.curr_array[x][y] = 0


class RPS:
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
        # updates cells to be dead or live
        for x in range(self.rows):
            for y in range(self.columns):
                x_pos, y_pos = x * self.scale, y * self.scale
                curr = self.curr_array[x][y]
                if -1 < curr < 1:  # Fix rounding error near 0
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
                elif curr == 3:
                    pygame.draw.rect(surface, lizard,
                                     [x_pos, y_pos, self.scale - self.border, self.scale - self.border])
                else:
                    pygame.draw.rect(surface, spock,
                                     [x_pos, y_pos, self.scale - self.border, self.scale - self.border])

    def transition(self):
        # rules for transitions between generations
        new_array = np.ndarray(shape=self.size)
        for x in range(self.rows):
            for y in range(self.columns):
                state = self.curr_array[x][y]
                # neighbors = self.get_neighbors(x, y, state)
                neighbors, dominating = self.get_neighbors(x, y, state)
                # print(dominating)
                if neighbors > 2:
                    new_array[x][y] = most_freq(dominating)
                else:
                    new_array[x][y] = state

        # update previous field with next generation's field
        self.curr_array = new_array

    def get_neighbors(self, x, y, state):
        total, num_dominating = 0, []
        # check 8 cells around current cell
        for n in range(-1, 2):
            for m in range(-1, 2):
                if not (n == m == 0):  # Ignore self during check
                    # Since field is finite, stitch edges to yield toroidal array
                    x_edge = (x + n + self.rows) % self.rows
                    y_edge = (y + m + self.columns) % self.columns
                    neighbor = self.curr_array[x_edge][y_edge]
                    if self.numColors == 3:
                        if (state == -1 and neighbor == 1) or (state == 1 and neighbor == 2) \
                                or (state == 2 and neighbor == -1):
                            total += 1
                            num_dominating.append(neighbor)
                    elif self.numColors == 5:
                        if (state == -1 and (neighbor == 3 or neighbor == 4)) or \
                                (state == 1 and (neighbor == 4 or neighbor == -1)) \
                                or (state == 2 and (neighbor == -1 or neighbor == 1)) \
                                or (state == 3 and (neighbor == 1 or neighbor == 2)) \
                                or (state == 4 and (neighbor == 2 or neighbor == 3)):
                            total += 1
                            num_dominating.append(neighbor)
        return total, num_dominating

    def click(self, pos, choice):
        # Clicking on cell will change it's state from dead to live or vice versa
        x, y = int(pos[0] / self.scale), int(pos[1] / self.scale)
        self.curr_array[x][y] = choice

    def random_field(self):
        # Generates random field of cells
        for x in range(self.rows):
            for y in range(self.columns):
                # self.curr_array[x][y] = random.randint(0, 1)
                if self.numColors == 3:
                    self.curr_array[x][y] = random.choices([-1, 1, 2])[0]
                elif self.numColors == 5:
                    self.curr_array[x][y] = random.choices([-1, 1, 2, 3, 4])[0]

    def reset(self):
        # Clears entire field to all dead cells
        for x in range(self.rows):
            for y in range(self.columns):
                self.curr_array[x][y] = 0


def most_freq(neighbors):
    return max(set(neighbors), key=neighbors.count)


class Langton:
    def __init__(self, width, height, scale, border, colors, rules):
        self.scale = scale

        self.rows = int(width / scale)
        self.columns = int(height / scale)
        self.size = (self.rows, self.columns)

        self.curr_array = np.ndarray(shape=self.size)  # Field as 2d array
        self.border = border  # Lines between cells

        # Colors [(x,y,z), ..., (xn,yn,zn)], Rules = "RL"
        self.rules = rules
        self.colors = colors
        #self.colorIdx = {i: colors[i] for i in range(len(colors))}  # {0:(x,y,z),..., n:(xn, yn, zn)}
        self.cyclic = {colors[i]: rules[i] for i in range(len(rules))}  # {(x,y,z):R, ... (xn,yn,zn):L}
        self.direction = "N"  # N, E, S, W
        self.ant = (-1, -1)
        self.spawn = (255, 255, 255)

    def update(self, surface):
        # updates cells to be dead or live
        ant_x, ant_y = self.scale*np.array(self.ant)
        pygame.draw.rect(surface, (255, 0, 0),
                         [ant_x, ant_y, self.scale - self.border, self.scale - self.border])
        for x in range(self.rows):
            for y in range(self.columns):
                x_pos, y_pos = x * self.scale, y * self.scale
                if self.curr_array[x][y] == 0:
                    pygame.draw.rect(surface, (255, 255, 255),
                                     [x_pos, y_pos, self.scale - self.border, self.scale - self.border])


    def transition(self):
        # rules for transitions between generations
        new_array = np.ndarray(shape=self.size)
        curr_xPos, curr_yPos = self.ant
        curr_color = self.curr_array[curr_xPos][curr_yPos]


    def get_neighbors(self, x, y):
        neighbors = 0
        # check 8 cells around current cell
        for n in range(-1, 2):
            for m in range(-1, 2):
                if not (n == m == 0):  # Ignore self during check
                    # Since field is finite, stitch edges to yield toroidal array
                    x_edge = (x + n + self.rows) % self.rows
                    y_edge = (y + m + self.columns) % self.columns
                    neighbors += self.curr_array[x_edge][y_edge]
        return neighbors

    def click(self, pos, direction):
        # Clicking on cell spawns ant in specified direction
        print("click, " + direction)
        if self.ant != (-1, -1):  # There is an ant on the field currently
            self.curr_array[self.ant[0]][self.ant[1]] = 0  # On clicking, deletes previous ant

        # Creates new ant
        x, y = int(pos[0]/self.scale), int(pos[1]/self.scale)
        self.ant = (x, y)
        self.curr_array[x][y] = -1
        self.direction = direction

    def reset(self):
        # Clears entire field to all dead cells
        for x in range(self.rows):
            for y in range(self.columns):
                self.curr_array[x][y] = 0
