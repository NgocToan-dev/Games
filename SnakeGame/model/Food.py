import random


class Food:
    def __init__(self, x, y, width, height, window_width, window_height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.window_width = window_width
        self.window_height = window_height

    def relocate(self):
        self.x = random.randint(0, self.window_width - self.width)
        self.y = random.randint(0, self.window_height - self.height)
