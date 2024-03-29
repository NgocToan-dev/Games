class Snake:
    def __init__(self, x, y, width, height, velocity):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = velocity
        self.direction = "right"
        self.vision_distance = 100
        self.body = [(self.x, self.y), (self.x - 10, self.y), (self.x - 20, self.y)]

    def move(self):
        if self.direction == "left":
            self.x -= self.velocity
        elif self.direction == "right":
            self.x += self.velocity
        elif self.direction == "up":
            self.y -= self.velocity
        elif self.direction == "down":
            self.y += self.velocity

        self.grow()

    def move_without_wall(self, window_width, window_height):
        if self.direction == "left":
            self.x -= self.velocity
            if self.x < 0:
                self.x = window_width - self.width
        elif self.direction == "right":
            self.x += self.velocity
            if self.x > window_width - self.width:
                self.x = 0
        elif self.direction == "up":
            self.y -= self.velocity
            if self.y < 0:
                self.y = window_height - self.height
        elif self.direction == "down":
            self.y += self.velocity
            if self.y > window_height - self.height:
                self.y = 0

        self.grow()

    def grow(self):
        self.body.insert(0, (self.x, self.y))

    def eat(self, food):
        if (
            self.x <= food.x + 10
            and self.x >= food.x - 10
            and self.y <= food.y + 10
            and self.y >= food.y - 10
        ):
            return True
        return False

    def check_collision(self):
        if self.body[0] in self.body[1:]:
            return True
        return False

    def check_wall_collision(self, wall):
        if self.body[0] in wall.segments:
            return True
        return False

    def check_barrier_collision(self, barrier):
        if self.body[0] in barrier.segments:
            return True
        return False
