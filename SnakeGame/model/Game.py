import pygame
from model.Food import Food
from model.Player import Player
from model.Snake import Snake
from model.Wall import Wall


class Game:
    def __init__(
        self,
        snake: Snake,
        player: Player,
        food: Food,
        wall: Wall,
        barriers,
        window_width,
        window_height,
    ):
        self.player = player
        self.food = food
        self.snake = snake
        self.wall = wall
        self.barriers = barriers
        self.window_width = window_width
        self.window_height = window_height
        self.game_over = False

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

    def update(self):
        self.snake.move()
        if (
            self.snake.check_collision()
            or self.snake.check_wall_collision(self.wall)
            or any(self.snake.check_barrier_collision(barrier) for barrier in self.barriers)
        ):
            self.game_over = True
        if self.snake.eat(self.food):
            self.player.updateScore()
            self.food.relocate(self.wall, self.barriers)
            self.snake.body.insert(0, (self.snake.x, self.snake.y))
        else:
            self.snake.body.pop()

    def is_game_over(self):
        return self.game_over
