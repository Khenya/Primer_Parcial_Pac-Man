import arcade
import pymunk

# constantes
WIDTH = 600
HEIGHT = 600
SPEED = 1
class Enemies(arcade.Sprite):
    def __init__(self, image, scale, center_x, center_y, space):
        super().__init__(image, scale)
        self.center_x = center_x
        self.center_y = center_y
        self.change_x = SPEED
        self.space = space 
        self.body = None
        self.shape = None
        self.create_physics_body()

    def create_physics_body(self):
        mass = 1.0
        moment = pymunk.moment_for_box(mass, (self.width, self.height))
        self.body = pymunk.Body(mass, moment)
        self.body.position = (self.center_x, self.center_y)
        
        # Crear una forma de pymunk para el enemigo
        self.shape = pymunk.Poly.create_box(self.body, (self.width, self.height))
        self.shape.elasticity = 0.0
        self.shape.friction = 0.0
        self.space.add(self.body, self.shape)

    def update(self):
        next_x = self.center_x + self.change_x
        if self.left < 0 or self.right > WIDTH:
            self.change_x *= -1  
            next_x = self.center_x + self.change_x

        if not self.check_obstacle(next_x, self.center_y):
            self.center_x = next_x
            self.body.position = (self.center_x, self.center_y)

    def check_obstacle(self, x, y):
        hit_shape = self.space.point_query_nearest((x, y), 0.5, pymunk.ShapeFilter())
        return hit_shape is not None and hit_shape.shape.body.body_type == pymunk.Body.STATIC