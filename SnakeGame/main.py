import pygame
import time
import random
from model.Food import Food
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

# Initialize food and snake
food = Food(
    random.randint(0, window_width - snake.width),
    random.randint(0, window_height - snake.height),
    10,
    10,
)

running = True
game_over = False
# Set initial direction
direction = "right"
while running and not game_over:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake.direction != "right":
                snake.direction = "left"
            elif event.key == pygame.K_RIGHT and snake.direction != "left":
                snake.direction = "right"
            elif event.key == pygame.K_UP and snake.direction != "down":
                snake.direction = "up"
            elif event.key == pygame.K_DOWN and snake.direction != "up":
                snake.direction = "down"

    # Update game logic
    snake.move()

    # Check if snake has collided with itself
    if snake.check_collision():
        game_over = True

    # Check if snake has eaten food
    if snake.eat(food):
        food.relocate(window_width, window_height)
        snake.body.insert(0, (snake.x, snake.y))
    else:
        snake.body.pop()

    # Render graphics
    window.fill((0, 0, 0))

    # Draw snake
    for segment in snake.body:
        pygame.draw.rect(window, (255, 255, 255), (*segment, snake.width, snake.height))

    # Draw food
    pygame.draw.rect(window, (255, 0, 0), (food.x, food.y, snake.width, snake.height))
    # Draw score
    score_text = font.render(f"Score: {snake.score}", True, (255, 255, 255))
    window.blit(score_text, (10, 10))  # Draw score at position (10, 10)

    # Update the display
    pygame.display.update()

    # Add a delay to control the game's frame rate
    time.sleep(0.1)

# Game over
if game_over:
    game_over_text = font.render(
        f"Game Over! Your score was: {snake.score}", True, (255, 255, 255)
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
