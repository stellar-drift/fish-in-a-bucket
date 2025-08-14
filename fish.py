import pygame
import math
import random

class Fish(pygame.sprite.Sprite):
    # class constructor
    def __init__(self, image_path, size):
        super().__init__()      # call constructor of superclass Sprite

        # load and scale sprite
        self.og_img = pygame.image.load(image_path).convert_alpha()      # surface attribute / the sprite's visual
        self.og_img = pygame.transform.scale(self.og_img, size)          # scale the image size
        self.image = self.og_img

        # rect and random starting position
        self.rect = self.image.get_rect(center=(
            random.randint(0, 480), random.randint(150, 245)))      # attribute defines where the image is on screen

        self.start_x = self.rect.centerx    # get initial x position
        self.start_y = self.rect.centery    # get initial y position

        # initial facing
        self.direction = random.choice([1, -1])
        if self.direction == -1:
            self.image = pygame.transform.flip(self.og_img, True, False)

        # bobbing parameters
        self.amp_x = 30
        self.amp_y = 15
        self.speed = 2
        self.time = 0


    def update(self, dt):       # sprite logic per frame
        self.time += dt

        # horizontal bobbing relative to start_x
        offset_x = self.amp_x * math.sin(self.time * self.speed) * self.direction
        self.rect.centerx = self.start_x + offset_x

        # vertical bobbing relative to start_y
        self.rect.centery = self.start_y + self.amp_y * math.sin(self.time * self.speed * 0.5)
