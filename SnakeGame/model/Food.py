import random


class Food:
    def __init__(self, x, y, width, height, window_width, window_height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.window_width = window_width
        self.window_height = window_height

    def relocate(self, wall, barriers):
        while True:
            self.x = random.randint(0, self.window_width - self.width)
            self.y = random.randint(0, self.window_height - self.height)
            if (self.x, self.y) not in wall.segments and any(
                (self.x, self.y) not in barrier.segments for barrier in barriers
            ):
                break
