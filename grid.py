import pygame
import numpy as np
import random


class Conway:
    def __init__(self, width, height, scale, border):
        self.scale = scale

        self.rows = int(width / scale)
        self.columns = int(height / scale)
        self.size = (self.rows, self.columns)

        self.curr_array = np.ndarray(shape=self.size)  # Field as 2d array
        self.border = border  # Lines between cells

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
                self.curr_array[x][y] = random.randint(0, 1)
                # self.curr_array[x][y] = random.choices([0, 1], [9, 1])[0] # 90% of spawning dead

    def reset(self):
        # Clears entire field to all dead cells
        for x in range(self.rows):
            for y in range(self.columns):
                self.curr_array[x][y] = 0


class RPS:
    # Rock = -1, White = 0, Paper = 1, Scissors = 2
    def __init__(self, width, height, scale, border):
        self.scale = scale

        self.rows = int(width / scale)
        self.columns = int(height / scale)
        self.size = (self.rows, self.columns)

        self.curr_array = np.ndarray(shape=self.size)  # Field as 2d array
        self.border = border  # Lines between cells

    def update(self, rock, paper, scissors, surface):
        # updates cells to be dead or live
        for x in range(self.rows):
            for y in range(self.columns):
                x_pos, y_pos = x * self.scale, y * self.scale
                if -1 < self.curr_array[x][y] < 1:  # Fix rounding error near 0
                    pygame.draw.rect(surface, (255, 255, 255),
                                     [x_pos, y_pos, self.scale - self.border, self.scale - self.border])
                elif self.curr_array[x][y] == -1:
                    pygame.draw.rect(surface, rock,
                                     [x_pos, y_pos, self.scale - self.border, self.scale - self.border])
                elif self.curr_array[x][y] == 1:
                    pygame.draw.rect(surface, paper,
                                     [x_pos, y_pos, self.scale - self.border, self.scale - self.border])
                else:
                    pygame.draw.rect(surface, scissors,
                                     [x_pos, y_pos, self.scale - self.border, self.scale - self.border])

    def transition(self):
        # rules for transitions between generations
        new_array = np.ndarray(shape=self.size)
        for x in range(self.rows):
            for y in range(self.columns):
                state = self.curr_array[x][y]
                neighbors = self.get_neighbors(x, y, state)
                if neighbors > 2:
                    if state == -1:
                        new_array[x][y] = 1
                    elif state == 1:
                        new_array[x][y] = 2
                    else:
                        new_array[x][y] = -1
                else:
                    new_array[x][y] = state

        # update previous field with next generation's field
        self.curr_array = new_array

    def get_neighbors(self, x, y, state):
        total = 0
        # check 8 cells around current cell
        for n in range(-1, 2):
            for m in range(-1, 2):
                if not (n == m == 0):  # Ignore self during check
                    # Since field is finite, stitch edges to yield toroidal array
                    x_edge = (x + n + self.rows) % self.rows
                    y_edge = (y + m + self.columns) % self.columns
                    neighbor = self.curr_array[x_edge][y_edge]
                    if (state == -1 and neighbor == 1) or (state == 1 and neighbor == 2) \
                            or (state == 2 and neighbor == -1):
                        total += 1
        return total

    def click(self, pos, choice):
        # Clicking on cell will change it's state from dead to live or vice versa
        x, y = int(pos[0] / self.scale), int(pos[1] / self.scale)
        self.curr_array[x][y] = choice

    def random_field(self):
        # Generates random field of cells
        for x in range(self.rows):
            for y in range(self.columns):
                # self.curr_array[x][y] = random.randint(0, 1)
                self.curr_array[x][y] = random.choices([-1, 1, 2])[0]

    def reset(self):
        # Clears entire field to all dead cells
        for x in range(self.rows):
            for y in range(self.columns):
                self.curr_array[x][y] = 0

