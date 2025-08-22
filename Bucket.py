import pygame


class Bucket(pygame.sprite.Sprite):
    def __init__(self):
            super().__init__()

            self.image = pygame.image.load('assets/fish_bucket.png').convert_alpha()    # load image
            self.image = pygame.transform.scale(self.image, (36,34))        # overwrite with scaled down image
            self.rect = self.image.get_rect(center=(350,80))   # attribute defines where the image is on screen


    def check_collection(self, fish_list):        # checks all fish to see if they've passed the point of destruction; removes fish that have and returns count
        fish_collected = 0
        for fish in fish_list.sprites()[:]:     # iterate over a copy of the list
            if self.rect.colliderect(fish.rect):   # check collision
                fish.kill()     # remove from all groups
                fish_collected += 1
                print("This fish is a has been!")
        return fish_collected


