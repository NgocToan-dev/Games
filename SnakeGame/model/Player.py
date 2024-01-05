from model.Food import Food
from model.Snake import Snake


class Player:
    def __init__(self):
        self.score = 0

    def updateScore(self):
        self.score += 1
