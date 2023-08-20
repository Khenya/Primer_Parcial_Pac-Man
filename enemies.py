import arcade

class Enemies(arcade.Sprite):
    def __init__(self, image, scale, center_x, center_y):
        super().__init__(image, scale, center_x=center_x, center_y=center_y)
        self.change_x = 0
        self.change_y = 0
    
    def update(self):
        # TODO hacer su logica fantasamas
        pass