

import pygame
import sys


def run_scene(screen, clock):
    running = True

    # image scale width and height
    width = 480
    height = 270

    # load and scale backdrop images:
    day = pygame.image.load("assets/pier_day.png").convert()  # use .convert() to same 'pixel format' as display -- draws faster
    day = pygame.transform.scale(day, (width, height))  # scale image for window size

    dusk = pygame.image.load("assets/pier_dusk.png").convert()
    dusk = pygame.transform.scale(dusk, (width, height))

    night = pygame.image.load("assets/pier_night.png").convert()
    night = pygame.transform.scale(night, (width, height))

    twilight = pygame.image.load("assets/pier_twilight.png").convert()
    twilight = pygame.transform.scale(twilight, (width, height))

    # variables for fade control
    transition_stage = "start"  # initialize fade to dusk
    alpha = 0  # initialize alpha at 0 (fully transparent)
    hold_counter = 0  # used to pause at full opacity
    HOLD_FRAMES = 180  # number of frames to pause (fps)
    fading = True  # toggle to start fading

    # initialize base and overlay to valid images
    base = day
    overlay = dusk

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # hold day image before starting the first fade
        if transition_stage == "start":  # if stage is at start
            hold_counter += 1  # increment pause counter
            if hold_counter > HOLD_FRAMES:  # if counter tries to surpass constant value
                transition_stage = "dusk"  # set stage to dusk
                overlay = dusk  # set overlay to dusk
                fading = True  # toggle fading
                alpha = 0  # reset alpha to transparent
                hold_counter = 0  # reset counter

        # transition logic
        elif fading:
            if alpha < 255:  # if image is transparent
                alpha += 3  # increase opacity (adjust for speed)
            else:
                hold_counter += 1  # increment counter
                if hold_counter > HOLD_FRAMES:  # if the counter value is equal or greater than the frames constant
                    hold_counter = 0  # reset counter
                    alpha = 0  # and reset alpha value to transparent

                    # update base and overlay
                    if transition_stage == "dusk":  # if the transition stage is dusk
                        base = dusk
                        overlay = night
                        transition_stage = "night"
                    elif transition_stage == "night":  # if the transition stage is night
                        base = night
                        overlay = twilight
                        transition_stage = "twilight"
                    elif transition_stage == "twilight":
                        base = twilight
                        overlay = day
                        transition_stage = "day"
                    elif transition_stage == "day":
                        base = day
                        overlay = dusk
                        transition_stage = "dusk"  # restart loop

        screen.blit(base, (0, 0))  # draw base layer
        overlay.set_alpha(alpha)  # apply the new alpha to the overlay
        screen.blit(overlay, (0, 0))  # draw the fade layer

        pygame.display.flip()  # show the image on the screen
        clock.tick(60)  # cap rate at 60fps


if __name__ == "__main__":
    import pygame

    pygame.init()
    screen = pygame.display.set_mode((480, 270))
    clock = pygame.time.Clock()

    run_scene(screen, clock)
