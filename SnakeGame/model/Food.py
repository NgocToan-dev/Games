import random


class Food:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def relocate(self, window_width, window_height):
        self.x = random.randint(0, window_width - self.width)
        self.y = random.randint(0, window_height - self.height)
