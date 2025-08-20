

import pygame
from Scene import Scene
from Fish import Fish
from Animation import FishAnimation
from state_machine import FishState


pygame.init()

SIZE_BG = (480, 270)
SIZE_FH = (17, 11)
DROP_LIM = 150

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

scene = Scene(SIZE_BG)
fish = Fish(
    size=SIZE_FH,
    state_machine_cls=FishState,
    state_imgs=state_imgs,
    animation_cls=FishAnimation)

all_fish = pygame.sprite.Group(fish)    # sprite group for updates/drawing

# run/draw/quit logic
running = True
while running:
    dt = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            fish.mouse_down(event.pos)
        elif event.type == pygame.MOUSEBUTTONUP:
            fish.mouse_up(event.pos)
        elif event.type == pygame.MOUSEMOTION:
            fish.mouse_motion(event.pos)

    scene.update()          # update background animation
    scene.draw(screen)      # draw background

    all_fish.update(dt)     # update fish
    all_fish.draw(screen)   # draw fish on top

    pygame.display.flip()