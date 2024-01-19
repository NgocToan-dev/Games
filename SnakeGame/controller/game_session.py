import time
import pygame
from controller.game_setting import GameSetting
from model.Game import Game
from model.Player import Player


# Inherit from GameSetting class
class GameSession(GameSetting):
    def __init__(self, window, player: Player, level):
        super().__init__(window)
        self.player = player
        self.game = Game(self.window_width, self.window_height, level)

    def run_game(self):
        # Game logic
        running = True
        while running:
            # Check if the game is over
            if self.game.is_game_over():
                self.end_game()
                running = False
                break

            # Handle events
            for event in pygame.event.get():
                self.game.handle_event(event)
            self.game.update()

            # Update player score
            if self.game.check_is_eaten_food():
                self.player.updateScore()

            # Render graphics
            self.window.fill((0, 0, 0))

            # Draw barriers
            self.render_objects_graphic()

            # Draw score
            self.render_player_score()
            
            self.render_vision_distant()

            # Update the display
            pygame.display.update()

            # Add a delay to control the game's frame rate
            time.sleep(0.1)

    def render_vision_distant(self):
        # light up the vision distant nad draw it on the screen
        vision_distant = pygame.Surface((self.game.snake.vision_distance, self.game.snake.vision_distance))
        vision_distant.fill((255, 255, 255))
        vision_distant.set_alpha(100)
        self.window.blit(vision_distant, (self.game.snake.x, self.game.snake.y))
        
        
    """
    The render_objects_graphic() method is responsible for drawing the game objects on the screen.
    """

    def render_objects_graphic(self):
        self.window.fill((0, 0, 0))

        # Draw barriers
        for barrier in self.game.barriers:
            for segment in barrier.segments:
                pygame.draw.rect(
                    self.window,
                    (255, 255, 255),
                    (*segment, self.game.snake.width, self.game.snake.height),
                )

        # Draw wall
        for segment in self.game.wall.segments:
            pygame.draw.rect(
                self.window,
                (255, 255, 255),
                (*segment, self.game.snake.width, self.game.snake.height),
            )

        # Draw snake
        for segment in self.game.snake.body:
            pygame.draw.rect(
                self.window,
                (255, 255, 255),
                (*segment, self.game.snake.width, self.game.snake.height),
            )

        # Draw food
        pygame.draw.rect(
            self.window,
            (255, 0, 0),
            (
                self.game.food.x,
                self.game.food.y,
                self.game.snake.width,
                self.game.snake.height,
            ),
        )

    def render_player_score(self):
        score_text = self.font.render(
            f"Score: {self.player.score}", True, (255, 255, 255)
        )
        self.window.blit(score_text, (10, 10))

    def end_game(self):
        game_over_text = self.font.render(
            f"Game Over! Your score was: {self.player.score}", True, (255, 255, 255)
        )
        self.window.blit(
            game_over_text,
            (
                self.window_width // 2 - game_over_text.get_width() // 2,
                self.window_height // 2 - game_over_text.get_height() // 2,
            ),
        )
        pygame.display.update()
        time.sleep(2)  # Wait for 2 seconds before closing the game
