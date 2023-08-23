import arcade
import pymunk

from player import Player
from enemies import Enemies

# constantes
WIDTH = 600
HEIGHT = 600
TITLE = "PAC-MAN"
SPEED = 50

class PacMan(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE)
        self.game_over = False
        self.winer = False
        self.score = 0
        self.eat_sound = arcade.Sound("music/pacman_sound.ogg")
        self.game_over_sound = arcade.Sound("music/game_over_sound.ogg")
        arcade.set_background_color(arcade.color.BLACK)
        # Font
        arcade.load_font("font_name/PublicPixel-z84yD.ttf")
        self.custom_font = "Public Pixel"
        # Crear espacio Pymunk
        self.space = pymunk.Space()
        self.space.gravity = (0, 0)  

        # Lista de sprites para dibujar
        self.sprites = arcade.SpriteList()

        # Crear al jugador y agregarlo a la lista de sprites
        self.player = Player(
            "img/player.png", 
            0.7, 
            WIDTH / 2, 
            HEIGHT / 2, 
            space=self.space
        )
        self.sprites.append(self.player)
        
        # Crear al enemigo 1 y agregarlo a la lista de sprites
        self.enemies = Enemies(
            "img/enemies.png",  
            0.7, 
            center_x=100, 
            center_y=305,
            space=self.space
        )
        self.sprites.append(self.enemies)

        # Crear al enemigo 2 y agregarlo a la lista de sprites
        self.enemies_2 = Enemies(
            "img/enemies2.png",
            0.045,
            center_x=20,
            center_y=445,
            space=self.space
        )
        self.sprites.append(self.enemies_2)
        
        # Crear al enemigo 3 y agregarlo a la lista de sprites
        self.enemies_3 = Enemies(
            "img/enemies3.png",
            0.013,
            center_x=300,
            center_y=585,
            space=self.space
        )
        self.sprites.append(self.enemies_3)

        # Crear al enemigo 4 y agregarlo a la lista de sprites
        self.enemies_4 = Enemies(
            "img/enemies4.png",
            0.05,
            center_x = 400,
            center_y = 165,
            space=self.space
        )
        self.sprites.append(self.enemies_4)

        # Crear al enemigo 5 y agregarlo a la lista de sprites
        self.enemies_5 = Enemies(
            "img/enemies5.png",
            0.05,
            center_x = 100,
            center_y = 25,
            space=self.space
        )
        self.sprites.append(self.enemies_5)

        # Crear los cubitos
        self.tamano_cuadrado = 100
        self.shapes = []
        for j in range(4):
            self.y = 95 + j * (self.tamano_cuadrado + 40)
            for i in range(4): 
                self.x = 95 + i * (self.tamano_cuadrado + 40)
                self.static_body = pymunk.Body(body_type=pymunk.Body.STATIC)
                self.static_body.position = (self.x, self.y)  
                self.shape = pymunk.Poly.create_box(self.static_body, (self.tamano_cuadrado, self.tamano_cuadrado))
                self.shape.friction = 0.0
                self.space.add(self.static_body, self.shape)
                self.shapes.append(self.shape)
        
        # Crear puntos
        self.point = arcade.SpriteList()
        # Crear puntos en la fila
        for fila in range(5):
            start_y = HEIGHT + 35 - self.tamano_cuadrado // 2 - fila * 140 
            for i in range(15):
                point = arcade.SpriteSolidColor(5, 5, arcade.color.AMBER)
                point.center_x = 20 + i * 40
                point.center_y = start_y
                self.point.append(point)
                self.sprites.append(point)

        # Crear columnas de puntos
        for columna in range(5):
            for i in range(15):
                point = arcade.SpriteSolidColor(5, 5, arcade.color.AMBER)
                point.center_x = 20 + columna * 140 
                point.center_y = 25 + i * 40
                self.point.append(point)
                self.sprites.append(point)

    def on_update(self, delta_time: float):   
        self.space.step(delta_time)
        # perder
        if arcade.check_for_collision(
            self.enemies, self.player) or  arcade.check_for_collision(
            self.enemies_2, self.player) or arcade.check_for_collision(
            self.enemies_3, self.player) or  arcade.check_for_collision(
            self.enemies_4, self.player) or  arcade.check_for_collision(
            self.enemies_5, self.player):
            self.game_over = True
            return
        # ganar
        if len(self.point) == 0:
            self.winer = True
            return
        
        self.sprites.update()
        self.update_point()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.UP:
            self.player.shape.body.velocity = (0, SPEED)
            self.player.direction = "up"
        if symbol == arcade.key.DOWN:
            self.player.shape.body.velocity = (0, -SPEED)
            self.player.direction = "down"
        if symbol == arcade.key.LEFT:
            self.player.shape.body.velocity = (-SPEED, 0)
            self.player.direction = "left"
        if symbol == arcade.key.RIGHT:
            self.player.shape.body.velocity = (SPEED, 0)
            self.player.direction = "right"

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol in (arcade.key.UP, arcade.key.DOWN):
            self.player.center_x = 0
        if symbol in (arcade.key.LEFT, arcade.key.RIGHT):
            self.player.center_y = 0
    
    def on_draw(self):
        arcade.start_render()
        # dibujar cuadrados
        for shape in self.shapes:  
            position = shape.body.position
            points = shape.get_vertices()
            adjusted_points = [(point[0] + position.x, point[1] + position.y) for point in points]
            
            arcade.draw_rectangle_outline(
                adjusted_points[0][0] - 50, adjusted_points[0][1] + 50,
                self.tamano_cuadrado, self.tamano_cuadrado,
                arcade.color.BLUE, border_width=5
            )    
        
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
        
        self.sprites.draw()      
        # perder y ganar
        if self.game_over:
            arcade.draw_text("GAME OVER", WIDTH / 2, HEIGHT / 2, arcade.color.ALABAMA_CRIMSON, 36, anchor_x="center", anchor_y="center", font_name = self.custom_font)
        elif self.winer:
            arcade.draw_text("WINNER", WIDTH / 2, HEIGHT / 2, arcade.color.GOLD, 36, anchor_x="center", anchor_y="center", font_name = self.custom_font)
        
        # score
        arcade.draw_text(f"Score: {self.score}", 15, HEIGHT - 20, font_name = self.custom_font)
            
    # puntos
    def update_point(self):
        for p in self.point:
            if arcade.check_for_collision(p, self.player):
                p.remove_from_sprite_lists()
                self.score += 1
                self.eat_sound.play()
  
def main():
    app = PacMan()
    arcade.run()

if __name__ == "__main__":
    main()
