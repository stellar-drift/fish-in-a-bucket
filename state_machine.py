import random

class FishState:
    def __init__(self):
        self.state = "idle"
        self.state_timer = 0        # timer for current state
        self.hooked_duration = 0    # timer for being hooked

    def get_state(self):
        return self.state

    def update(self, dt):
        self.state_timer += dt

        # transition from hooked to idle
        if self.state == "hooked" and self.state_timer >= self.hooked_duration:
            self.change_state("idle")

    def change_state(self, new_state):
        self.state = new_state
        self.state_timer = 0

        if new_state == "hooked":
            self.hooked_duration = random.uniform(2.0, 7.0)    # (second) use a random time duration for how long the fish stays hooked

