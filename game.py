import pygame
import numpy
import time
import random

from PIL import Image

def input():
    pass

def update():
    pass

def render():
    pass

def scale_to_width(dimensions, width):
    height = (width * dimensions[1]) / dimensions[0]
    return (width, height)

def main():

    screen_size = (1920, 1080)
    camera_offset = 0
    tile_dims = 120
    grid = []

    pygame.init()
    display = pygame.display.set_mode((1920, 1080))
    map = numpy.asarray(Image.open('map_generation/map.png').convert('L'))

    for i in range(-tile_dims, screen_size[0]+1, tile_dims):
        for j in range(-tile_dims, screen_size[1]+1, tile_dims):
            grid.append((i, j))

    dirt = pygame.image.load('tiles/dirt_01.png')
    copper = pygame.image.load('tiles/copper.png')

    for i in range(tile_dims):
        for cell in grid:
            display.blit(copper, (cell[0]+camera_offset, cell[1]))
        camera_offset += 1
        pygame.display.update()

    # while True:
    #     input()
    #     update()
    #     render()

if __name__ == "__main__":
    main()
