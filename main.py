import arcade
import random
from player import Player, Point
from enemies import Enemies
# constantes
WIDTH = 800
HEIGHT = 576
TITLE = "PAC-MAN"
SPEED = 1
FONT = arcade.load_font("font_name/PublicPixel-z84yD.ttf")

class PacMan(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.game_over = False
        self.score = 0
        # sprite list para dibujar
        self.sprites = arcade.SpriteList()
        self.player = Player(
            "img/player.png", 
            1, 
            center_x=WIDTH / 2, 
            center_y=HEIGHT / 2
        )
        self.sprites.append(self.player)
        self.enemies = Enemies(
            "img/enemies.png",  
            1, 
            center_x=100, 
            center_y=300
        )
        self.sprites.append(self.enemies)
        self.point = arcade.SpriteList()

        for _ in range(23):
            point = arcade.SpriteSolidColor(5, 5, arcade.color.WHITE)
            point.center_x = random.randint(10, WIDTH - 10)
            point.center_y = random.randint(10, HEIGHT - 10)
            self.point.append(point)
            self.sprites.append(point)

        self.obstacle = arcade.SpriteSolidColor(100, 100, arcade.color.BLUE)
        self.obstacle.center_x = 100
        self.obstacle.center_y = 100

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
        if arcade.check_for_collision(self.enemies, self.player):
            self.game_over = True
            return
        elif arcade.check_for_collision(self.obstacle, self.player):
            if self.player.change_x > 0 and self.player.direction == "right":
                self.player.change_x = 0
            if self.player.change_x < 0 and self.player.direction == "left":
                self.player.change_x = 0
            if self.player.change_y > 0 and self.player.direction == "up":
                self.player.change_y = 0
            if self.player.change_y < 0 and self.player.direction == "down":
                self.player.change_y = 0
        
        self.enemies.update()
        self.sprites.update()
        self.update_point()
    
    def update_point(self):
        for p in self.point:
            if arcade.check_for_collision(p, self.player):
                p.remove_from_sprite_lists()
                self.score += 1
 
    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_outline(100, 100, 100, 100, arcade.color.BLUE, border_width= 4)
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
        if self.game_over:
            arcade.draw_text("GAME OVER", WIDTH / 2, HEIGHT / 2, arcade.color.ALABAMA_CRIMSON, 36, anchor_x="center", anchor_y="center")
        
        arcade.draw_text(f"Score: {self.score}", 10, HEIGHT - 40)
        
        self.sprites.draw()   
        
def main():
    app = PacMan()
    arcade.run()

if __name__ == "__main__":
    main()