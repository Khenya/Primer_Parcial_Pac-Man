import arcade
import pymunk

# constantes
WIDTH = 600
HEIGHT = 600
SPEED = 1.5
class Enemies(arcade.Sprite):
    def __init__(self, image, scale, center_x, center_y, space):
        super().__init__(image, scale)
        self.center_x = center_x
        self.center_y = center_y
        self.change_x = SPEED
        
        mass = 1.0
        moment = pymunk.moment_for_box(mass, (self.width, self.height))
        self.body = pymunk.Body(mass, moment)
        self.body.position = (center_x, center_y)
        
        # Crear una forma de pymunk para el enemigo
        shape = pymunk.Poly.create_box(self.body, (self.width, self.height))
        shape.elasticity = 0.0
        shape.friction = 0.0
        self.shape = shape

        # Agregar el cuerpo y la forma a la space de pymunk
        space.add(self.body, self.shape)
        

    def update(self):
        self.center_x += self.change_x
        if self.left < 0 or self.right > WIDTH:
            self.change_x *= -1
        self.body.position = (self.center_x, self.center_y)


