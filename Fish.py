# this script handles the fish class


import pygame
import random

class Fish(pygame.sprite.Sprite):
    # class constructor
    def __init__(self, size, state_machine_cls, state_imgs, animation_instance, drop_limit_y=150):
        super().__init__()      # call constructor of superclass Sprite

        # components
        self.state_machine = state_machine_cls()    # state machine -- tracks logical state (idle, hooked, caught) and any timers
        self.animation = animation_instance         # controls animation independent of state

        # map each state to a scaled image for rendering
        self.state_imgs = {
            # dictionary comprehension = {key_expression: value_expression for item in iterable}
            state: pygame.transform.scale(img, size) for (state, img) in state_imgs.items()
        }

        # initial image, rect, and starting positions
        self.image = self.state_imgs[self.state_machine.get_state()]
        self.rect = self.image.get_rect(center=(
            random.randint(0, 480), random.randint(150, 245)))  # attribute defines where the image is on screen
        self.start_x = self.rect.centerx  # get initial x position
        self.start_y = self.rect.centery  # get initial y position
        self.direction = random.choice([1, -1])         # face direction (1 = right, -1 = left)
        self.direction = random.choice([1, -1])         # face direction (1 = right, -1 = left)
        if self.direction == -1:    # flip image if facing left
            self.image = pygame.transform.flip(self.image, True, False)

        # drag/drop -- tracks whether the mouse is dragging/dropping object
        self.dragging = False
        self.is_mouse_down = False
        self.drop_limit_y = drop_limit_y    # y limit for "dropping" the fish after drag
        self.dropping = False
        self.drop_target_y = None
        self.drop_speed = 200   # pixels per second


    def update(self, dt):       # wrapper for sprite update logic per frame
        self.state_machine.update(dt)       # update the state machine
        self._update_position(dt)
        self._update_image()
        self._bucket_drop(dt)

    def _update_position(self, dt):
        # update position using animation if not dragging
        if self.dragging:
            # mouse_motion() handles rect while dragging
            return
        elif self.dropping:
            self._handle_drop(dt)
        else:  # idle animation (if not dragging or dropping)
            new_x, new_y = self.animation.update(dt, self.start_x, self.start_y, self.direction)
            self.rect.centerx, self.rect.centery = new_x, new_y

    def _handle_drop(self, dt):
        dy = self.drop_speed * dt
        if self.rect.centery + dy >= self.drop_target_y:
            self.rect.centery = self.drop_target_y
            self.dropping = False
            self.start_x, self.start_y = self.rect.center
            self.state_machine.change_state("idle")
        else:
            self.rect.centery += dy

    def _update_image(self):
        img = self.state_imgs[self.state_machine.get_state()]    # update image based on current state
        if self.direction == -1:
            img = pygame.transform.flip(img, True, False)
        self.image = img

    def _bucket_drop(self, dt):
        state = self.state_machine.get_state()
        if state == "falling_into_bucket":
            self.rect.centery += 200*dt # fall speed
            if self.rect.top > 80:      # once the fish is "inside" the bucket, kill it
                self.kill()


    # mouse events: drag and click
    def mouse_down(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.is_mouse_down = True
            self.state_machine.change_state("hooked")   # change state to hooked
            self.dragging = True    # start dragging
            self.drag_offset = (self.rect.centerx - mouse_pos[0], self.rect.centery - mouse_pos[1])

    def mouse_up(self, mouse_pos):
        if self.dragging:
            if self.rect.centery < self.drop_limit_y:
                self.drop_target_y = random.randint(self.drop_limit_y, self.drop_limit_y + 50)
                self.dropping = True
            else:   # released below water line -- stay in place
                self.start_x, self.start_y = self.rect.center
                self.state_machine.change_state("idle")

            # reset drag state
            self.dragging = False
            self.is_mouse_down = False
            return True

        return False

    def mouse_motion(self, mouse_pos):
        if self.dragging:
            self.rect.center = (        # drag fish with mouse
                mouse_pos[0] + self.drag_offset[0],
                mouse_pos[1] + self.drag_offset[1])





# main guard
if __name__ == "__main__":
    import sys
    from Animation import FishAnimation
    from StateMachine import FishState

    pygame.init()
    screen = pygame.display.set_mode((480, 270))
    clock = pygame.time.Clock()

    # load images for test fish
    idle_image = pygame.image.load("assets/images/fish/fish_idle.png").convert_alpha()
    hooked_image = pygame.image.load("assets/images/fish/fish_hooked.png").convert_alpha()

    imgs_by_state = {
        "idle": idle_image,
        "hooked": hooked_image
    }

    # test fish
    fh_size = (17,11)
    test_fh = Fish(size=fh_size,
                   state_machine_cls=FishState,
                   state_imgs=imgs_by_state,
                   animation_instance=FishAnimation(speed=2),
                   drop_limit_y=150)

    all_fish = pygame.sprite.Group(test_fh)


    running = True
    while running:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                test_fh.mouse_down(event.pos)
            elif event.type == pygame.MOUSEBUTTONUP:
                test_fh.mouse_up(event.pos)
            elif event.type == pygame.MOUSEMOTION:
                test_fh.mouse_motion(event.pos)

        # draw fish
        all_fish.update(dt)
        screen.fill("#00000a")
        all_fish.draw(screen)

        pygame.display.flip()

    pygame.quit()
    sys.exit()
