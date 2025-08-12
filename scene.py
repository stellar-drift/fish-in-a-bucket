
import pygame
import sys


def run_scene(screen, clock):
    running = True

    # constants
    WIDTH = 480
    HEIGHT = 270
    SIZE = (WIDTH, HEIGHT)
    FIRST_HOLD_FRAMES = 300
    HOLD_FRAMES = 300  # number of frames to pause (fps)

    # list filenames
    filenames = [
        "assets/background/pier_day.png",
        "assets/background/pier_dusk.png",
        "assets/background/pier_night.png",
        "assets/background/pier_twilight.png"
    ]

    # fade control variables
    first_hold = 0
    is_first_fade = False
    hold_counter = 0  # used to pause at full opacity


    # animation indexing
    images = [load_and_scale(f, SIZE) for f in filenames]       # use list comprehension; for each index in list, call the function
    current_idx = 0
    alpha = 0  # initialize alpha at 0 (fully transparent)
    base = images[current_idx]
    overlay = images[(current_idx + 1) % len(images)]


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # transition logic
        if not is_first_fade:      # handle first image upon run; if true, then...
            first_hold += 1     # add 1
            if first_hold > FIRST_HOLD_FRAMES:
                is_first_fade = True       # begin fade cycle
        else:       # only fade once the initial hold is done
            # fade overlay in
            if alpha < 255:     # if alpha is translucent
                alpha += 3      # fade in speed
            else:
                hold_counter += 1       # hold at full opacity

            # transition logic; after hold frames, switch to next images
            if hold_counter > HOLD_FRAMES:
                hold_counter = 0
                alpha = 0
                current_idx = (current_idx + 1) % len(images)
                base = images[current_idx]
                overlay = images[(current_idx + 1) % len(images)]



        # draw logic
        screen.blit(base, (0, 0))  # draw base layer
        overlay.set_alpha(alpha)  # apply the new alpha to the overlay
        screen.blit(overlay, (0, 0))  # draw the fade layer

        pygame.display.flip()  # show the image on the screen
        clock.tick(60)  # cap rate at 60fps



# helper function for loading and scaling images
def load_and_scale(filename, size):
    img = pygame.image.load(filename).convert()
    return pygame.transform.scale(img, size)








if __name__ == "__main__":
    import pygame

    pygame.init()
    screen = pygame.display.set_mode((480, 270))
    clock = pygame.time.Clock()

    run_scene(screen, clock)
