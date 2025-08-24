# this script handles animations

import math

class Animation:
    def __init__(self, amp_x, amp_y, freq_x, freq_y, speed):
        self.amp_x = amp_x      # x-axis amplitude (motion wave height)
        self.amp_y = amp_y      # y-axis amplitude
        self.freq_x = freq_x    # x-axis frequency multiplier (wave frequency)
        self.freq_y = freq_y    # y-axis frequency multiplier
        self.speed = speed
        self.time = 0

    def update(self, dt, start_x, start_y, direction):      # returns new x & y position given a base position
        self.time += dt

        offset_x = self.amp_x * math.sin(self.time * self.speed * self.freq_x) * direction    # horizontal movement
        offset_y = self.amp_y * math.sin(self.time * self.speed * self.freq_y)                # vertical movement

        new_position = (start_x + offset_x), (start_y + offset_y)

        return new_position


class FishAnimation(Animation):        # fish animation houses the bobbing effect
    def __init__(self, speed, amp_x=30, amp_y=15, freq_x=1.0, freq_y=0.5):
        super().__init__(amp_x=amp_x, amp_y=amp_y, freq_x=freq_x, freq_y=freq_y, speed=speed)




