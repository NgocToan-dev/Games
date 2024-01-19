

import pygame
from controller.game_level import GameLevel
from controller.game_session import GameSession
from model.Player import Player


# Game logic

player = Player()

# Create window for player to choose game options before starting game
pygame.init()

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Snake Game")
game_setting = GameLevel(window)

pygame.display.update()

# capture mouse click
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Get mouse position
            mouse_pos = pygame.mouse.get_pos()
            game_level = ""
            for level in game_setting.levels:
                if game_setting.levels_buttons[level].collidepoint(mouse_pos):
                    game_level = level
                    break
            game_session = GameSession(window, player, game_level)
            game_session.run_game()                

            break

