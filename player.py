import arcade
import pymunk

# constantes
WIDTH = 600
HEIGHT = 600
SPEED = 1

class Player(arcade.Sprite):
    def __init__(self, image, scale, center_x, center_y, space):
        super().__init__(image, scale, center_x=center_x, center_y=center_y)
        self.change_x = 0
        self.change_y = 0
        self.direction = "right"
        mass = 1.0
        moment = pymunk.moment_for_box(mass, (self.width, self.height))
        self.body = pymunk.Body(mass, moment)
        self.body.position = (center_x, center_y)

        # Crear una forma de pymunk para el jugador
        shape = pymunk.Poly.create_box(self.body, (self.width, self.height))
        shape.elasticity = 0.0
        shape.friction = 0.0
        self.shape = shape

        # Agregar el cuerpo y la forma a la space de pymunk
        space.add(self.body, self.shape)
    
    def update(self):
    #     print(self.body.position)
    #     print(self.center_x,self.center_y)       
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

        self.body.position = (self.center_x, self.center_y)
        self.body.position = (self.center_x, self.center_y)

        # cordinar sprite con shape
        self.center_x = self.body.position.x
        self.center_y = self.body.position.y

    
        
