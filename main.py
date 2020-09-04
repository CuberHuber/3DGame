import math

import pygame
from settings import *
from player import Player
from map import world_map
import math
from ray_casting import ray_casting


pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player = Player()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    player.movement()
    screen.fill(BlACK)

    pygame.draw.rect(screen, SKY, (0, 0, WIDTH, HALF_HEIGHT))
    pygame.draw.rect(screen, SAND, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    ray_casting(screen=screen, player_pos=player.pos, player_angle=player.angle)

    # pygame.draw.circle(screen, GREEN, (int(player.x), int(player.y)), 12)
    # pygame.draw.line(screen, GREEN, player.pos, (player.x + WIDTH * math.cos(player.angle),
    #                                              player.y + WIDTH * math.sin(player.angle)))
    # for x,y in world_map:
    #     pygame.draw.rect(screen, DARKGRAY, (x, y, TILE, TILE), 2)

    pygame.display.flip()
    clock.tick(FPS)