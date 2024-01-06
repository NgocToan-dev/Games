from controller.game_setting import GameSetting
from resources.enums import enum


class GameLevel(GameSetting):
    levels = [enum['level']['easy'], enum['level']['medium'], enum['level']['hard']]
    # tuple of x, y position for each level
    levels_buttons = {}

    def __init__(self, window):
        super().__init__(window)
        self.create_level_button(self.levels[0], 400, 300)
        self.create_level_button(self.levels[1], 400, 350)
        self.create_level_button(self.levels[2], 400, 400)

    def create_level_button(self, level, x, y):
        text = self.font.render(level, True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (x, y)
        self.window.blit(text, textRect)
        self.levels_buttons[level] = textRect
