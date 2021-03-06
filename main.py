import math
import pygame

from settings import *
from player import Player
from map import world_map
from ray_casting import ray_casting
from drawing import Drawing


pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
sc_map = pygame.Surface((WIDTH // MAP_SCALE, HEIGHT // MAP_SCALE))
clock = pygame.time.Clock()
player = Player()
drawing = Drawing(screen, sc_map)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    player.movement()
    screen.fill(BlACK)

    drawing.background()
    drawing.world(player_pos, player_angle)
    drawing.fps(clock)
    drawing.mini_map(player)

    pygame.display.flip()
    clock.tick(FPS)