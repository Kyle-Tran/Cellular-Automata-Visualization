import pygame
import numpy as np
import random


class Grid:
    def __init__(self, width, height, scale, border):
        self.scale = scale

        self.rows = int(width / scale)
        self.columns = int(height / scale)
        self.size = (self.rows, self.columns)

        self.curr_array = np.ndarray(shape=self.size)
        self.border = border # Lines between cells

    def conway(self, dead, live, surface):
        # updates cells
        for x in range(self.rows):
            for y in range(self.columns):
                x_pos, y_pos = x * self.scale, y * self.scale
                if self.curr_array[x][y] == 1:
                    pygame.draw.rect(surface, live,
                                     [x_pos, y_pos, self.scale - self.border, self.scale - self.border])
                else:
                    pygame.draw.rect(surface, dead,
                                     [x_pos, y_pos, self.scale - self.border, self.scale - self.border])

    def update(self):
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

        # update array
        self.curr_array = new_array

    def get_neighbors(self, x, y):
        neighbors = 0
        # check 8 cells around current cell
        for n in range(-1, 2):
            for m in range(-1, 2):
                if not (n == m == 0): # Ignore self during check
                    # Since field is finite, stitch edges to yield toroidal array
                    x_edge = (x + n + self.rows) % self.rows
                    y_edge = (y + m + self.columns) % self.columns
                    neighbors += self.curr_array[x_edge][y_edge]
        return neighbors

    def click(self, pos):
        x, y = int(pos[0]/self.scale), int(pos[1]/self.scale)
        if self.curr_array[x][y] == 1:
            self.curr_array[x][y] = 0
        else:
            self.curr_array[x][y] = 1


    def random_field(self):
        for x in range(self.rows):
            for y in range(self.columns):
                self.curr_array[x][y] = random.randint(0, 1)
                # self.curr_array[x][y] = random.choices([0, 1], [9, 1])[0] # 90% of spawning dead
