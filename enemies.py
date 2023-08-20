import arcade
WIDTH = 800
HEIGHT = 600
SPEED = 2
class Enemies(arcade.Sprite):
    def __init__(self, image, scale, center_x, center_y):
        super().__init__(image, scale)
        self.center_x = center_x
        self.center_y = center_y
        self.change_x = SPEED

    def update(self):
        self.center_x += self.change_x
        if self.left < 0 or self.right > WIDTH:
            self.change_x *= -1

