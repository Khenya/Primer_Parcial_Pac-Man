import arcade
import math


class Player(arcade.Sprite):
    def __init__(self, image, scale, center_x, center_y):
        super().__init__(image, scale, center_x=center_x, center_y=center_y)
        self.change_x = 0
        self.change_y = 0
    
    def update(self):
        self.center_x += -self.change_x
        self.center_y += self.change_y

    
