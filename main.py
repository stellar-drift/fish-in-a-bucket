

import pygame
from scene import Scene
from fish import Fish
import random

pygame.init()
pygame.init()

SIZE_BG = (480, 270)
SIZE_FH = (17, 11)



screen = pygame.display.set_mode(SIZE_BG)        # set window size
clock = pygame.time.Clock()     # Clock object to control frame rate and track time between frames

scene = Scene(SIZE_BG)
fish = Fish("assets/fish.png", size = SIZE_FH)

# sprite group for updates/drawing
all_fish = pygame.sprite.Group(fish)


# run/draw/quit logic
running = True
while running:
    dt = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    scene.update()          # update background animation
    scene.draw(screen)      # draw background

    all_fish.update(dt)     # update fish
    all_fish.draw(screen)   # draw fish on top

    pygame.display.flip()