
import math


class FishAnimation:        # fish animation houses the bobbing effect
    def __init__(self, amp_x=30, amp_y=15, speed=2):
        self.amp_x = amp_x
        self.amp_y = amp_y
        self.speed = speed
        self.time = 0

    def update(self, dt, start_x, start_y, direction):      # returns new x & y position given a base position
        self.time += dt

        offset_x = self.amp_x * math.sin(self.time * self.speed) * direction    # horizontal movement
        offset_y = self.amp_y * math.sin(self.time * self.speed * 0.5)          # vertical movement

        new_position = start_x + offset_x, start_y + offset_y

        return new_position

