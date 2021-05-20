import pygame
import numpy
import time
import random
import sys

from PIL import Image
from pygame.locals import *

pygame.init()

class Pytherload:
    def __init__(self):

        self.map = numpy.asarray(Image.open('map_generation/map.png').convert('L'))

        self.screen_size = (1920, 1080)
        self.display = pygame.display.set_mode(self.screen_size)
        self.clock = pygame.time.Clock()
        self.dirt = pygame.image.load('tiles/dirt_01.png').convert()
        self.copper = pygame.image.load('tiles/copper.png').convert()

        self.direction = None

        self.camera_offset = [0, 0]
        self.tile_dims = 120
        self.grid = []

        self.pressed_keys = []

        self.init_grid()

    def init_grid(self):
        for i in range(-self.tile_dims, self.screen_size[0]+1, self.tile_dims):
            for j in range(-self.tile_dims, self.screen_size[1]+1, self.tile_dims):
                self.grid.append((i, j))

    def get_input(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_UP:
                    self.pressed_keys.append('up')
                if event.key == pygame.K_DOWN:
                    self.pressed_keys.append('down')
                if event.key == pygame.K_LEFT:
                    self.pressed_keys.append('left')
                if event.key == pygame.K_RIGHT:
                    self.pressed_keys.append('right')
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.pressed_keys.remove('up')
                if event.key == pygame.K_DOWN:
                    self.pressed_keys.remove('down')
                if event.key == pygame.K_LEFT:
                    self.pressed_keys.remove('left')
                if event.key == pygame.K_RIGHT:
                    self.pressed_keys.remove('right')

    def update(self):
        if len(self.pressed_keys) > 0:
            direction = self.pressed_keys[-1]
            if direction == 'up':
                if self.camera_offset[1] + 1 < 0:
                    self.camera_offset[1] = (self.camera_offset[1] + 1) % -self.tile_dims
                else:
                    self.camera_offset[1] = (self.camera_offset[1] + 1) % self.tile_dims
            elif direction == 'down':
                if self.camera_offset[1] - 1 < 0:
                    self.camera_offset[1] = (self.camera_offset[1] - 1) % -self.tile_dims
                else:
                    self.camera_offset[1] = (self.camera_offset[1] - 1) % self.tile_dims
            elif direction == 'left':
                if self.camera_offset[0] + 1 < 0:
                    self.camera_offset[0] = (self.camera_offset[0] + 1) % -self.tile_dims
                else:
                    self.camera_offset[0] = (self.camera_offset[0] + 1) % self.tile_dims
            elif direction == 'right':
                if self.camera_offset[0] - 1 < 0:
                    self.camera_offset[0] = (self.camera_offset[0] - 1) % -self.tile_dims
                else:
                    self.camera_offset[0] = (self.camera_offset[0] - 1) % self.tile_dims

    def render(self):
        for cell in self.grid:
            self.display.blit(self.copper, (cell[0]+self.camera_offset[0], cell[1]+self.camera_offset[1]))
        pygame.display.update()

if __name__ == "__main__":

    game = Pytherload()

    while True:
        game.get_input()
        game.update()
        game.render()
        game.clock.tick(144)
