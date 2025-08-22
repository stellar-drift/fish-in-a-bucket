

import pygame
import random
from Scene import Scene
from Fish import Fish
from Animation import FishAnimation
from state_machine import FishState


pygame.init()

SIZE_BG = (480, 270)
SIZE_FH = (17,11)

screen = pygame.display.set_mode(SIZE_BG)    # set window size
clock = pygame.time.Clock()     # Clock object to control frame rate and track time between frames

# load images
idle_image = pygame.image.load("assets/fish/fish_idle.png").convert_alpha()
hooked_image = pygame.image.load("assets/fish/fish_hooked.png").convert_alpha()

# image dictionary
state_imgs = {
    "idle": idle_image,
    "hooked": hooked_image
}

# objects
scene = Scene(SIZE_BG)
sprite_list = []
for i in range(random.randint(1,11)):
    sprite_list.append(
        Fish(
            size=SIZE_FH,
            state_machine_cls=FishState,
            state_imgs=state_imgs,
            animation_cls=FishAnimation
        )
    )

all_fish = pygame.sprite.Group(sprite_list)    # sprite group/container for managing multiple sprites


# run/draw/quit logic
running = True
while running:
    dt = clock.tick(60) / 1000
    for event in pygame.event.get():        # loop through all events in the event queue
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:  # when mouse is pressed...
            for fish in all_fish:       # ... for each sprite in the group...
                fish.mouse_down(event.pos)      # ... pass current mouse position to object method
        elif event.type == pygame.MOUSEBUTTONUP:
            for fish in all_fish:
                fish.mouse_up(event.pos)
        elif event.type == pygame.MOUSEMOTION:
            for fish in all_fish:
                fish.mouse_motion(event.pos)


    scene.update()          # update background animation
    scene.draw(screen)      # draw background

    all_fish.update(dt)     # update fish
    all_fish.draw(screen)   # draw fish on top

    pygame.display.flip()