import pygame


class GameSetting:
    window_width = 800
    window_height = 600
    
    def __init__(self, window):
        # Set up the game window
        self.window = window
        # Initialize Pygame font
        pygame.font.init()
        self.font = pygame.font.Font(None, 36)