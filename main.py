

import pygame
from scene import run_scene

pygame.init()
screen = pygame.display.set_mode((480, 270))        # set window size
clock = pygame.time.Clock()     # create a Clock object to control frame rate and track time between frames

run_scene(screen, clock)