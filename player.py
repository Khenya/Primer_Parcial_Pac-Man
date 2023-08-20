import arcade
WIDTH = 800
HEIGHT = 600
SPEED = 1

class Player(arcade.Sprite):
    def __init__(self, image, scale, center_x, center_y):
        super().__init__(image, scale, center_x=center_x, center_y=center_y)
        self.change_x = 0
        self.change_y = 0
        self.direction = "right"
    
    def update(self):
        if self.right < 0:
            self.left = WIDTH
        elif self.left > WIDTH:
            self.right = 0
        if self.top < 0:
            self.bottom = HEIGHT
        elif self.bottom > HEIGHT:
            self.top = 0

        self.center_x += -self.change_x
        self.center_y += self.change_y

class Character:
    def __init__(self, x, y, life, size) -> None:
        self.x = x
        self.y = y
        self.life = life
        self.size = size

        