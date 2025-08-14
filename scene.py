import pygame


class Scene:
    def __init__(self, size):
        self.WIDTH, self.HEIGHT = size
        self.FIRST_HOLD_FRAMES = 300
        self.HOLD_FRAMES = 300

        # list filenames
        filenames = [
            "assets/background/pier_day.png",
            "assets/background/pier_dusk.png",
            "assets/background/pier_night.png",
            "assets/background/pier_twilight.png"
        ]

        # animation variables
        self.images = [load_and_scale(f, size) for f in filenames]       # use list comprehension; for each index in list, call the function
        self.current_idx = 0
        self.alpha = 0
        self.base = self.images[self.current_idx]
        self.overlay = self.images[(self.current_idx + 1) % len(self.images)]

        # fade control variables
        self. first_hold = 0
        self.is_first_fade = False
        self.hold_counter = 0  # used to pause at full opacity


    def update(self):

        # transition logic
        if not self.is_first_fade:      # handle first image upon run; if true, then...
            self.first_hold += 1     # add 1
            if self.first_hold > self.FIRST_HOLD_FRAMES:
                self.is_first_fade = True       # begin fade cycle
        else:       # only fade once the initial hold is done
            # fade overlay in
            if self.alpha < 255:     # if alpha is translucent
                self.alpha += 3      # fade in speed
            else:
                self.hold_counter += 1       # hold at full opacity

            # transition logic; after hold frames, switch to next images
            if self.hold_counter > self.HOLD_FRAMES:
                self.hold_counter = 0
                self.alpha = 0
                self.current_idx = (self.current_idx + 1) % len(self.images)
                self.base = self.images[self.current_idx]
                self.overlay = self.images[(self.current_idx + 1) % len(self.images)]


    def draw(self, screen):     # draw logic
        screen.blit(self.base, (0, 0))  # draw base layer
        self.overlay.set_alpha(self.alpha)  # apply the new alpha to the overlay
        screen.blit(self.overlay, (0, 0))  # draw the fade layer



# helper function for loading and scaling images
def load_and_scale(filename, size):
    img = pygame.image.load(filename).convert()
    return pygame.transform.scale(img, size)



if __name__ == "__main__":
    import pygame

    pygame.init()
    screen = pygame.display.set_mode((480, 270))
    clock = pygame.time.Clock()

    scene = Scene((480, 270))
    running = True
    while running:
        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        scene.update()
        scene.draw(screen)

        pygame.display.flip()

    pygame.quit()
