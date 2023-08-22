import arcade
import random
import pymunk

from player import Player
from enemies import Enemies

# constantes
WIDTH = 600
HEIGHT = 600
TITLE = "PAC-MAN"
SPEED = 1

class PacMan(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.game_over = False
        self.winer = False
        self.score = 0
        # self.FONT = arcade.load_font("font_name/MunroNarrow-vaO4.ttf")

        # crear espacio de Pymunk
        self.space = pymunk.Space()
        self.space.gravity = (0, 0)  

        # Lista de sprites para dibujar
        self.sprites = arcade.SpriteList()

        # Crear al jugador y agregarlo a la lista de sprites
        self.player = Player(
            "img/player.png", 
            0.7, 
            0, 
            580, 
            space=self.space
        )
        self.sprites.append(self.player)

        # Crear al enemigo y agregarlo a la lista de sprites
        self.enemies = Enemies(
            "img/enemies.png",  
            0.7, 
            center_x=100, 
            center_y=305,
            space=self.space
        )
        self.sprites.append(self.enemies)

        # Crear fondo
        # Calcular el tamaño del cuadrado
        self.tamano_cuadrado = 100
        # Calcular la cantidad de filas y columnas
        self.filas = 4
        self.columnas = 4
        # Calcular el espacio entre los cuadrados
        self.espacio_x = (WIDTH - (self.columnas * self.tamano_cuadrado)) // (self.columnas + 1)
        self.espacio_y = (HEIGHT - (self.filas * self.tamano_cuadrado)) // (self.filas + 1)

        # Calcular la posición inicial
        self.x_inicial = self.espacio_x + self.tamano_cuadrado // 2 + 5
        self.y_inicial = self.espacio_y + self.tamano_cuadrado // 2 + 5
        
        for fila in range(self.filas):
            for columna in range(self.columnas):
                x = self.espacio_x + (columna * (self.tamano_cuadrado + self.espacio_x))
                y = self.espacio_y + (fila * (self.tamano_cuadrado + self.espacio_y))           
                # Crear el cuerpo y la forma del cuadrado
                cubo_body = pymunk.Body(body_type=pymunk.Body.STATIC)
                cubo_body.position = x, y
                forma = pymunk.Poly.create_box(cubo_body, (self.tamano_cuadrado, self.tamano_cuadrado))
                forma.friction = 0.0       
                # Agregar el cuerpo y la forma al espacio
                self.space.add(cubo_body, forma)

        # Crear puntos
        self.point = arcade.SpriteList()
        # Calcular el espacio entre los puntos en la fila
        point_spacing_x = 40
        # Crear puntos en la fila
        for fila in range(5):
            start_y = HEIGHT + 35 - self.tamano_cuadrado // 2 - fila * 140 
            for i in range(15):
                point = arcade.SpriteSolidColor(5, 5, arcade.color.AMBER)
                point.center_x = 20 + i * point_spacing_x
                point.center_y = start_y
                self.point.append(point)
                self.sprites.append(point)
        
        # Crear puntos en las columnas
        for columna in range(5):
            start_x = 20
            start_y = 25  
            for i in range(15):
                point = arcade.SpriteSolidColor(5, 5, arcade.color.AMBER)
                point.center_x = start_x + columna * 140 
                point.center_y = start_y + i * 40
                self.point.append(point)
                self.sprites.append(point)
            
        # musica
        # self.come= arcade.load_sound("musica/pacman_sound.ogg")
        # self.fail= arcade.load_sound("musica/game_over_sound.ogg")
    
    # def play(self):
    #     self.sound.play(pan=self.pan, volume=self.volume)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.UP:
            self.player.change_y = SPEED
            self.player.direction = "up"
        if symbol == arcade.key.DOWN:
            self.player.change_y = -SPEED
            self.player.direction = "down"
        if symbol == arcade.key.LEFT:
            self.player.change_x = SPEED
            self.player.direction = "left"
        if symbol == arcade.key.RIGHT:
            self.player.change_x= -SPEED
            self.player.direction = "right"

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol in (arcade.key.UP, arcade.key.DOWN):
            self.player.change_x = 0
        if symbol in (arcade.key.LEFT, arcade.key.RIGHT):
            self.player.change_y = 0

    def on_update(self, delta_time: float):   
        self.space.step(delta_time)
        # perder
        if arcade.check_for_collision(self.enemies, self.player):
            self.game_over = True
             # arcade.play_sound(self.fail,1)
            return
        # ganar
        if len(self.point) == 0:
            self.winer = True
            return

        # Obtener las coordenadas actuales del jugador
        current_x = self.player.center_x
        current_y = self.player.center_y

        # Calcular las coordenadas después del movimiento
        next_x = current_x + self.player.change_x
        next_y = current_y + self.player.change_y

        # Verificar colisiones con bloques estáticos
        hit_shape_x = self.space.point_query_nearest((next_x, current_y), 0.2, pymunk.ShapeFilter())
        hit_shape_y = self.space.point_query_nearest((next_y, current_y), 0.2, pymunk.ShapeFilter())

        if hit_shape_x is not None and hit_shape_x.shape.body.body_type == pymunk.Body.STATIC:
            self.player.change_x = 0
            # print("collition")
        if hit_shape_y is not None and hit_shape_y.shape.body.body_type == pymunk.Body.STATIC:
            self.player.change_y = 0
            # print("choque")
            
        self.enemies.update()
        self.sprites.update()
        self.update_point()

    # puntos
    def update_point(self):
        for p in self.point:
            if arcade.check_for_collision(p, self.player):
                p.remove_from_sprite_lists()
                self.score += 1
            
    def on_draw(self):
        arcade.start_render()

        # perder y ganar
        if self.game_over:
            arcade.draw_text("GAME OVER", WIDTH / 2, HEIGHT / 2, arcade.color.ALABAMA_CRIMSON, 36, anchor_x="center", anchor_y="center")
            # button_sprite.play()
        elif self.winer:
            arcade.draw_text("WINNER", WIDTH / 2, HEIGHT / 2, arcade.color.GOLD, 36, anchor_x="center", anchor_y="center")
           
        # pac man
        for sprite in  self.sprites:
            if isinstance(sprite, Player):
                if sprite.direction == "up":
                    sprite.angle = 90
                elif sprite.direction == "down":
                    sprite.angle = 270
                elif sprite.direction == "left":
                    sprite.angle = 180
                else:
                    sprite.angle = 0

        # Dibujar los cuadrados
        for fila in range(self.filas):
            for columna in range(self.columnas):
                x = self.x_inicial + (columna * (self.tamano_cuadrado + self.espacio_x))
                y = self.y_inicial + (fila * (self.tamano_cuadrado + self.espacio_y))
                
                arcade.draw_rectangle_outline(x, y, self.tamano_cuadrado, self.tamano_cuadrado, arcade.color.BLUE,5)
        
        # score
        arcade.draw_text(f"Score: {self.score}", 15, HEIGHT - 20)
        self.sprites.draw()   
        
def main():
    app = PacMan()
    arcade.run()

if __name__ == "__main__":
    main()
