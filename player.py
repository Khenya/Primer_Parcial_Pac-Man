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
        next_x = self.center_x + self.change_x
        next_y = self.center_y + self.change_y
        
        # print(self.body.position)
        # print(self.center_x,self.center_y)       
        if self.change_x != 0 or self.change_y != 0:
            self.body.velocity = (self.change_x * SPEED, self.change_y * SPEED)
        else:
            self.body.velocity = (0, 0)

        # Sincronizar posición del sprite con el cuerpo de pymunk
        self.center_x = self.body.position.x
        self.center_y = self.body.position.y   
        
        # # Consultar si hay un cubo en la dirección en la que se moverá el enemigo
        # if not self.check_obstacle(next_x, self.center_y):
        #     self.center_x = next_x
        #     self.body.position = (self.center_x, self.center_y)
        #     self.center_y = next_y
        #     # print("choque")
        
    
    def check_obstacle(self, x, y):
        # Consultar si hay un cuadrado
        hit_shape = self.space.point_query_nearest((x, y), 0.5, pymunk.ShapeFilter())
        return hit_shape is not None and hit_shape.shape.body.body_type == pymunk.Body.STATIC
