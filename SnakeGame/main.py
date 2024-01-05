import pygame
import time
import random
from model.Food import Food
from model.Game import Game
from model.Player import Player
from model.Snake import Snake

# Initialize pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")
# Initialize Pygame font
pygame.font.init()
font = pygame.font.Font(None, 36)

# Game logic
snake = Snake(50, 50, 10, 10, 10)
player = Player()
# Initialize food and snake
food = Food(
    random.randint(0, window_width - snake.width),
    random.randint(0, window_height - snake.height),
    10,
    10,
    window_width,
    window_height,
)
game = Game(snake, player, food, window_width, window_height)

running = True
game_over = False
while running and not game.is_game_over():
    for event in pygame.event.get():
        game.handle_event(event)
    game.update()
    
    # Render graphics
    window.fill((0, 0, 0))

    # Draw snake
    for segment in snake.body:
        pygame.draw.rect(window, (255, 255, 255), (*segment, snake.width, snake.height))

    # Draw food
    pygame.draw.rect(window, (255, 0, 0), (food.x, food.y, snake.width, snake.height))
    # Draw score
    score_text = font.render(f"Score: {player.score}", True, (255, 255, 255))
    window.blit(score_text, (10, 10))  # Draw score at position (10, 10)

    # Update the display
    pygame.display.update()

    # Add a delay to control the game's frame rate
    time.sleep(0.1)

# Game over
if game.is_game_over():
    game_over_text = font.render(
        f"Game Over! Your score was: {player.score}", True, (255, 255, 255)
    )
    window.blit(
        game_over_text,
        (
            window_width // 2 - game_over_text.get_width() // 2,
            window_height // 2 - game_over_text.get_height() // 2,
        ),
    )
    pygame.display.update()
    time.sleep(2)  # Wait for 2 seconds before closing the game
