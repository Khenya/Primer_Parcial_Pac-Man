import arcade

class Player(arcade.Sprite):
    def __init__(self, image, scale, center_x, center_y):
        super().__init__(image, scale, center_x=center_x, center_y=center_y)
        self.change_x = 0
        self.change_y = 0
        self.direction = "right"
    
    def update(self):
        self.center_x += -self.change_x
        self.center_y += self.change_y

class Character:
    def __init__(self, x, y, life, size) -> None:
        self.x = x
        self.y = y
        self.life = life
        self.size = size

class Point(Character):
    def __init__(self, x, y, size, color) -> None:
        super().__init__(x,y,5, size)
        self.color = color 

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.size, self.color)
        