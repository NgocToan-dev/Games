import random
import pygame
from model.Barrier import Barrier
from model.Food import Food
from model.Snake import Snake
from model.Wall import Wall
from resources.enums import enum


class Game:
    window_width = 800
    window_height = 600
    has_wall = False
    has_barrier = False

    def __init__(self, window_width, window_height, level):
        self.window_width = window_width
        self.window_height = window_height
        self.set_game_level(level)
        self.init_game()

    def init_game(self):
        self.snake = Snake(50, 50, 10, 10, 10)
        self.food = Food(
            random.randint(0, self.window_width - self.snake.width),
            random.randint(0, self.window_height - self.snake.height),
            10,
            10,
        )
        self.wall = self.create_wall()
        self.barriers = self.create_barrier()
        self.game_over = False
        self.is_eaten_food = False

    def set_game_level(self, level):
        self.level = level
        if level == enum["level"]["easy"]:
            self.has_wall = False
        elif level == enum["level"]["medium"]:
            self.has_wall = True
        elif level == enum["level"]["hard"]:
            self.has_wall = True
            self.has_barrier = True

    # Create wall
    def create_wall(self):
        if not self.has_wall:
            return Wall([])

        wall_segments = (
            [(x, 0) for x in range(0, self.window_width, 10)]
            + [(x, self.window_height - 10) for x in range(0, self.window_width, 10)]
            + [(0, y) for y in range(0, self.window_height, 10)]
            + [(self.window_width - 10, y) for y in range(0, self.window_height, 10)]
        )
        return Wall(wall_segments)

    # Create barrier
    def create_barrier(self):
        if not self.has_barrier:
            return []
        barrier1_segments = [
            (x, y) for x in range(100, 200, 10) for y in range(100, 200, 10)
        ]
        barrier1 = Barrier(barrier1_segments)

        barrier2_segments = [
            (x, y) for x in range(300, 400, 10) for y in range(300, 400, 10)
        ]
        barrier2 = Barrier(barrier2_segments)

        return [barrier1, barrier2]

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.control("left")
            elif event.key == pygame.K_RIGHT:
                self.control("right")
            elif event.key == pygame.K_UP:
                self.control("up")
            elif event.key == pygame.K_DOWN:
                self.control("down")

    def control(self, direction):
        if direction == "left" and self.snake.direction != "right":
            self.snake.direction = "left"
        elif direction == "right" and self.snake.direction != "left":
            self.snake.direction = "right"
        elif direction == "up" and self.snake.direction != "down":
            self.snake.direction = "up"
        elif direction == "down" and self.snake.direction != "up":
            self.snake.direction = "down"

    # Update game state
    def update(self):
        self.snake_move()
        self.check_game_over()
        self.snake_eat_food()

    # Move snake
    def snake_move(self):
        if not self.has_wall:
            self.snake.move_without_wall(self.window_width, self.window_height)
        else:
            self.snake.move()

    # Snake eat food and grow up
    def snake_eat_food(self):
        if self.snake.eat(self.food):
            self.is_eaten_food = True
            self.relocate(self.wall, self.barriers)
            self.snake.body.insert(0, (self.snake.x, self.snake.y))
        else:
            self.is_eaten_food = False
            self.snake.body.pop()

    # Check game over condition
    def check_game_over(self):
        if (
            self.snake.check_collision()
            or self.snake.check_wall_collision(self.wall)
            or (
                len(self.barriers) > 0
                and any(
                    self.snake.check_barrier_collision(barrier)
                    for barrier in self.barriers
                )
            )
        ):
            self.game_over = True

    # Relocate food to a random location that is not occupied by the snake or wall or barrier
    def relocate(self, wall, barriers):
        while True:
            self.food.x = random.randint(0, self.window_width - self.food.width)
            self.food.y = random.randint(0, self.window_height - self.food.height)
            if not self.has_wall:
                is_food_on_wall = False
            else:
                is_food_on_wall = (self.food.x, self.food.y) in wall.segments
            if not self.has_barrier:
                is_food_on_barrier = False
            else:
                is_food_on_barrier = any(
                    (self.food.x, self.food.y) in barrier.segments for barrier in barriers
                )
            if (not is_food_on_wall) and (not is_food_on_barrier):
                break

    def is_game_over(self):
        return self.game_over

    def check_is_eaten_food(self):
        return self.is_eaten_food
