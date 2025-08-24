
import pygame
import random
from Scene import Scene
from Fish import Fish
from Bucket import Bucket
from Animation import FishAnimation
from StateMachine import FishState


def main():
    pygame.init()

    SIZE_BG = (480, 270)
    SIZE_FH = (17,11)

    screen = pygame.display.set_mode(SIZE_BG)    # set window size
    clock = pygame.time.Clock()     # Clock object to control frame rate and track time between frames

    # load images
    idle_image = pygame.image.load("assets/images/fish/fish_idle.png").convert_alpha()
    hooked_image = pygame.image.load("assets/images/fish/fish_hooked.png").convert_alpha()

    # image dictionary
    state_imgs = {
        "idle": idle_image,
        "hooked": hooked_image
    }

    # objects
    scene = Scene(SIZE_BG)
    bucket = Bucket()
    fish_list = []
    for i in range(random.randint(1,11)):
        fish_list.append(
            Fish(
                size=SIZE_FH,
                state_machine_cls=FishState,
                state_imgs=state_imgs,
                animation_instance=FishAnimation(speed=random.uniform(0.5,5.0))
            )
        )



    all_fish = pygame.sprite.Group(fish_list)    # sprite group/container for managing multiple sprites
    one_bucket = pygame.sprite.GroupSingle(bucket)

    total_collected = 0

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
                    if fish.mouse_up(event.pos):
                        caught_fish = bucket.check_collection(pygame.sprite.Group(fish))  # check and hold count, only when fish is dropped
                        if caught_fish > 0:
                            total_collected += caught_fish
                            print(f"You collected {total_collected} fish so far! You won't go hungry this time!!")
                        break
            elif event.type == pygame.MOUSEMOTION:
                for fish in all_fish:
                    fish.mouse_motion(event.pos)


        scene.update()          # update background animation
        scene.draw(screen)      # draw background

        all_fish.update(dt)     # update fish
        all_fish.draw(screen)   # draw fish on top

        one_bucket.update()
        one_bucket.draw(screen)

        pygame.display.flip()



# main guard
if __name__ == "__main__":
    main()